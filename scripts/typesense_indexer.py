import os
import pathlib
import json
import re
import yaml
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Any, Optional
import typesense

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Your existing constants
ACRONYMS = {"AI", "API", "HTTP", "HTTPS", "SQL", "JSON", "XML", "CPU", "GPU", "OAuth", "CLI", "URL", "DNS", "IP", "UI", "MCP"}

CLUSTERS = {
    "All Content": [],
    "AI Builder": ["ai_builder"],
    "Hosting": ["hosting"],
    "Components": ["custom-components", "recipes"],
    "Enterprise": ["enterprise"],
    "API Reference": ["api-reference", "api-routes"],
    "Docs": ["advanced_onboarding", "assets", "authentication", "client_storage", "components", "database", "events", "getting_started", "library", "pages", "state", "state_structure", "styling", "ui", "utility_methods", "vars", "wrapping-react"],
    "Blog Posts": []
}

# Typesense configuration
TYPESENSE_CONFIG = {
    'nodes': [{
        'host': os.getenv('TYPESENSE_HOST'),
        'port': '443',
        'protocol': 'https'
    }],
    'api_key': os.getenv('TYPESENSE_ADMIN_API_KEY'),
    'connection_timeout_seconds': 60
}

# Simple collection schema - just what we need
COLLECTION_SCHEMA = {
    'name': 'docs',
    'fields': [
        {'name': 'id', 'type': 'string'},
        {'name': 'title', 'type': 'string'},
        {'name': 'content', 'type': 'string'},
        {'name': 'headings', 'type': 'string[]'},
        {'name': 'path', 'type': 'string'},
        {'name': 'url', 'type': 'string'},
        {'name': 'section', 'type': 'string'},
        {'name': 'subsection', 'type': 'string', 'optional': True},
        {'name': 'cluster', 'type': 'string'},
        {'name': 'is_blog', 'type': 'bool'},
        {'name': 'parts', 'type': 'string[]'},  # For breadcrumbs
    ],
}

class SimpleTypesenseIndexer:
    """Simplified indexer using your existing logic."""

    def __init__(self):
        self.client = typesense.Client(TYPESENSE_CONFIG)

    # Your existing helper functions - unchanged
    def smart_title_case(self, name: str) -> str:
        def fix_word(word: str) -> str:
            return word.upper() if word.upper() in ACRONYMS else word.capitalize()
        return " ".join(fix_word(w) for w in name.split())

    def clean_name(self, name: str) -> str:
        if name.lower().endswith(".md"):
            name = name[:-3]
        name = name.replace("_", " ").replace("-", " ").strip()
        return self.smart_title_case(name)

    def clean_markdown(self, text: str) -> str:
        text = re.sub(r"^---[\s\S]*?---\s*", "", text, flags=re.MULTILINE)
        text = re.sub(r"```[\s\S]*?```", "", text)
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        text = re.sub(r"<div[\s\S]*?</div>", "", text, flags=re.IGNORECASE)
        text = re.sub(r"`[^`]+`", "", text)
        text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
        text = re.sub(r"\n\s*\n+", "\n\n", text)
        return text.strip()

    def extract_headings(self, content: str) -> List[str]:
        """Extract headings from markdown content."""
        headings = []
        lines = content.split('\n')

        for line in lines:
            line = line.strip()
            if line.startswith('#'):
                heading_text = re.sub(r'^#+\s*', '', line)
                heading_text = re.sub(r'\{[^}]*\}', '', heading_text)
                if heading_text:
                    headings.append(heading_text.strip())

        return headings

    def summarize_markdown(self, md_path: str, max_lines: int = 10) -> str:
        """Your existing summarize function - simplified"""
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        cleaned = self.clean_markdown(content)
        lines = cleaned.splitlines()
        truncated_lines = lines[:max_lines]
        truncated_text = "\n".join(truncated_lines).strip()

        if len(truncated_lines) < max_lines:
            return truncated_text

        return truncated_text

    def name_from_url(self, url: str) -> str:
        parts = url.strip("/").split("/")
        if parts[0] == "docs":
            parts = parts[1:]
        if parts and parts[-1] == "low":
            parts[-1] = "low-level"
        readable = " ".join(part.replace("-", " ") for part in parts)
        return self.smart_title_case(readable)

    def process_doc_file(self, docs_path: str, file: str, root: str) -> Optional[dict]:
        """Your existing process_file function adapted for Typesense"""
        file_path = os.path.join(root, file)
        rel_path = os.path.relpath(file_path, docs_path)
        parts = pathlib.Path(rel_path).parts

        filename_no_ext = file.rsplit(".", 1)[0]

        # Build parts_clean
        parts_clean = []
        for i, p in enumerate(parts):
            is_last = i == len(parts) - 1
            if is_last:
                if filename_no_ext.endswith("-ll"):
                    parts_clean.append("Low Level")
                else:
                    parts_clean.append(self.clean_name(filename_no_ext))
            else:
                parts_clean.append(self.clean_name(p))

        # Build URL
        url_parts = [p.replace("_", "-").rsplit(".", 1)[0] for p in parts]
        if url_parts and url_parts[-1].endswith("-ll"):
            url_parts[-1] = url_parts[-1].replace("-ll", "/low")

        url = "/" + "/".join(url_parts)
        name = self.name_from_url(f"docs{url}")

        # Get content for full-text search
        full_content = self.summarize_markdown(file_path, max_lines=50)  # More content for search
        headings = self.extract_headings(open(file_path, 'r', encoding='utf-8').read())

        parent = parts[0] if parts else ""
        cluster = "Uncategorized"
        for cluster_name, folder_list in CLUSTERS.items():
            if parent in folder_list:
                cluster = cluster_name
                break

        return {
            "id": str(rel_path),
            "title": name,
            "content": full_content,
            "headings": headings,
            "path": str(rel_path),
            "url": f"docs{url}",
            "section": parent,
            "subsection": parts[1] if len(parts) > 1 else None,
            "cluster": cluster,
            "is_blog": False,
            "parts": parts_clean,
        }

    def extract_frontmatter(self, md_path: str) -> dict:
        """Your existing frontmatter extraction"""
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        match = re.match(r"---\n(.*?)\n---", content, re.DOTALL)
        if not match:
            return {}

        try:
            frontmatter = yaml.safe_load(match.group(1))
            return frontmatter
        except yaml.YAMLError:
            return {}

    def process_blog_file(self, blog_root: str, file: str, root: str) -> Optional[dict]:
        """Your existing blog processing adapted for Typesense"""
        file_path = os.path.join(root, file)
        fm = self.extract_frontmatter(file_path)

        if not fm or not all(k in fm for k in ("title", "author", "date", "description")):
            return None

        rel_path = os.path.relpath(file_path, blog_root)
        slug = pathlib.Path(file_path).stem.lower().replace("_", "-")
        url = f"/blog/{slug}"

        # Get full content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        full_content = self.clean_markdown(content)
        headings = self.extract_headings(content)

        return {
            "id": str(rel_path),
            "title": fm["title"],
            "content": full_content,
            "headings": headings,
            "path": str(rel_path),
            "url": url,
            "section": "Blog",
            "subsection": fm["author"],
            "cluster": "Blog Posts",
            "is_blog": True,
            "parts": ["Blog", fm["author"], fm["title"]],
        }

    def create_collection(self, force_recreate: bool = False) -> bool:
        """Create or recreate the collection."""
        try:
            try:
                self.client.collections['docs'].retrieve()
                if force_recreate:
                    logger.info("Deleting existing collection...")
                    self.client.collections['docs'].delete()
                else:
                    logger.info("Collection already exists. Use --force to recreate.")
                    return True
            except typesense.exceptions.ObjectNotFound:
                pass

            logger.info("Creating collection...")
            self.client.collections.create(COLLECTION_SCHEMA)
            logger.info("Collection created successfully.")
            return True

        except Exception as e:
            logger.error(f"Error creating collection: {e}")
            return False

    def index_documents(self, docs_path: str, blog_path: str, max_workers: int = 4, batch_size: int = 100) -> bool:
        """Index both docs and blog files"""
        try:
            # Process docs
            docs_files = []
            for root, _, files in os.walk(docs_path):
                for file in files:
                    if file.endswith(".md"):
                        docs_files.append((docs_path, file, root, False))

            # Process blog
            blog_files = []
            if os.path.exists(blog_path):
                for root, _, files in os.walk(blog_path):
                    for file in files:
                        if file.endswith(".md"):
                            blog_files.append((blog_path, file, root, True))

            all_files = docs_files + blog_files
            logger.info(f"Found {len(docs_files)} docs and {len(blog_files)} blog files")

            # Process files in parallel
            documents = []
            processed = 0

            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                # Submit all jobs
                futures = []
                for file_args in all_files:
                    future = executor.submit(self._process_file_wrapper, *file_args)
                    futures.append(future)

                # Collect results and batch index
                for future in as_completed(futures):
                    doc = future.result()
                    if doc:
                        documents.append(doc)
                        processed += 1

                        # Index batch when full
                        if len(documents) >= batch_size:
                            self._index_batch(documents)
                            documents = []
                            logger.info(f"Processed {processed}/{len(all_files)} files")

            # Index remaining documents
            if documents:
                self._index_batch(documents)
                logger.info(f"Processed {processed}/{len(all_files)} files")

            logger.info("Indexing completed successfully!")
            return True

        except Exception as e:
            logger.error(f"Error during indexing: {e}")
            return False

    def _process_file_wrapper(self, path: str, file: str, root: str, is_blog: bool) -> Optional[dict]:
        """Wrapper to route to correct processing function"""
        try:
            if is_blog:
                return self.process_blog_file(path, file, root)
            else:
                return self.process_doc_file(path, file, root)
        except Exception as e:
            logger.error(f"Error processing {file}: {e}")
            return None

    def _index_batch(self, documents: List[Dict[str, Any]]) -> None:
        """Index a batch of documents."""
        try:
            # Clean up documents - remove None values
            clean_docs = []
            for doc in documents:
                clean_doc = {k: v for k, v in doc.items() if v is not None}
                # Ensure required fields exist
                if 'subsection' not in clean_doc:
                    clean_doc['subsection'] = ""
                clean_docs.append(clean_doc)

            results = self.client.collections['docs'].documents.import_(
                clean_docs,
                {'action': 'upsert'}
            )

            # Check for errors
            for result in results:
                if not result.get('success', False):
                    logger.warning(f"Failed to index document: {result}")

        except Exception as e:
            logger.error(f"Error indexing batch: {e}")


def main():
    """Main function to run the indexing process."""
    import argparse

    parser = argparse.ArgumentParser(description='Simple Typesense indexer for Reflex docs')
    parser.add_argument('--docs-path', default='./docs', help='Path to docs directory')
    parser.add_argument('--blog-path', default='./blog', help='Path to blog directory')
    parser.add_argument('--force', action='store_true', help='Force recreate collection')
    parser.add_argument('--batch-size', type=int, default=100, help='Batch size for indexing')
    parser.add_argument('--max-workers', type=int, default=4, help='Max worker threads')

    args = parser.parse_args()

    # Validate environment
    if not os.getenv('TYPESENSE_HOST'):
        logger.error("TYPESENSE_HOST environment variable is required")
        return False

    if not os.getenv('TYPESENSE_ADMIN_API_KEY'):
        logger.error("TYPESENSE_ADMIN_API_KEY environment variable is required")
        return False

    # Validate paths
    docs_path = pathlib.Path(args.docs_path)
    if not docs_path.exists():
        logger.error(f"Docs path does not exist: {docs_path}")
        return False

    blog_path = pathlib.Path(args.blog_path)
    # Blog path is optional
    if not blog_path.exists():
        logger.warning(f"Blog path does not exist: {blog_path} - skipping blogs")
        args.blog_path = None

    # Run indexing
    indexer = SimpleTypesenseIndexer()

    if not indexer.create_collection(force_recreate=args.force):
        return False

    success = indexer.index_documents(
        str(docs_path),
        str(blog_path) if blog_path.exists() else "",
        max_workers=args.max_workers,
        batch_size=args.batch_size
    )

    return success


if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
