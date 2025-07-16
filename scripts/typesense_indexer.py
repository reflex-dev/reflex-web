#!/usr/bin/env python3
"""
Enhanced Typesense indexing script for Reflex documentation.

This script parses all markdown files in the docs folder and indexes them
to Typesense with improved component detection and content preservation.
"""

import os
import sys
import json
import re
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional, Set
import frontmatter
import typesense
from markdown import Markdown
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

TYPESENSE_CONFIG = {
    'nodes': [{
        'host': os.getenv('TYPESENSE_HOST'),
        'port': '443',
        'protocol': 'https'
    }],
    'api_key': os.getenv('TYPESENSE_ADMIN_API_KEY'),
    'connection_timeout_seconds': 60
}

# Enhanced collection schema with better component support
COLLECTION_SCHEMA = {
    'name': 'docs',
    'fields': [
        {'name': 'id', 'type': 'string'},
        {'name': 'title', 'type': 'string'},
        {'name': 'content', 'type': 'string'},
        {'name': 'code_examples', 'type': 'string', 'optional': True},
        {'name': 'headings', 'type': 'string[]'},
        {'name': 'path', 'type': 'string'},
        {'name': 'url', 'type': 'string'},
        {'name': 'components', 'type': 'string[]', 'optional': True},
        {'name': 'section', 'type': 'string'},
        {'name': 'subsection', 'type': 'string', 'optional': True},
        {'name': 'is_component', 'type': 'bool', 'optional': True},
        #
        {'name': 'weight', 'type': 'int32'},  # ← add this line
    ],
}

class MarkdownProcessor:
    """Enhanced processor for markdown files with better component detection."""

    def __init__(self):
        self.md = Markdown(extensions=['meta', 'toc'])
        self._component_names = None  # cache

    def _get_component_names_from_docs(self) -> List[str]:
            """Discover component slugs in docs/library → ['button', 'input', ...]."""
            if self._component_names is not None:
                return self._component_names

            repo_root = Path(__file__).parent.parent
            library_root = repo_root / 'docs' / 'library'
            names = set()

            if library_root.exists():
                for md_file in library_root.rglob('*.md'):
                    slug = md_file.stem
                    # strip “-ll”
                    if slug.endswith('-ll'):
                        slug = slug[:-3]
                    # add variants
                    names.add(slug)
                    names.add(slug.replace('-', '_'))
                    names.add(slug.replace('_', ''))
            else:
                logger.warning(f"Library docs directory not found: {library_root}")

            self._component_names = sorted(names)
            logger.info(f"Discovered {len(names)} components")
            return self._component_names

    def extract_components(self, content: str) -> Set[str]:
        """Find any of those components (with rx. prefix) in the markdown."""
        components = set()
        comp_names = self._get_component_names_from_docs()

        # look for either plain or rx.<name>
        for name in comp_names:
            # word boundary so we don’t match “button” inside “mybutton”
            pattern = rf'\b(?:rx\.)?{re.escape(name)}\b'
            for match in re.finditer(pattern, content):
                components.add(f"rx.{name}")

        return components

    def extract_headings(self, content: str) -> List[str]:
        """Extract headings from markdown content."""
        headings = []
        lines = content.split('\n')

        for line in lines:
            line = line.strip()
            if line.startswith('#'):
                heading_text = re.sub(r'^#+\s*', '', line)
                heading_text = re.sub(r'\{[^}]*\}', '', heading_text)  # Remove {#id} syntax
                if heading_text:
                    headings.append(heading_text.strip())

        return headings

    def _is_likely_component(self, name: str) -> bool:
        """Check if a name is likely a Reflex component."""
        if not name.startswith('rx.'):
            return False

        component_name = name[3:]  # Remove 'rx.' prefix

        # Component names should be lowercase with underscores
        # and not contain special characters
        return re.match(r'^[a-z][a-z0-9_]*$', component_name) is not None

    def extract_code_examples(self, content: str) -> str:
        """Extract code examples from markdown content."""
        code_blocks = []

        # Extract fenced code blocks
        code_pattern = r'```(?:[a-zA-Z]*\n)?(.*?)```'
        matches = re.findall(code_pattern, content, re.DOTALL)

        for match in matches:
            if match.strip():
                code_blocks.append(match.strip())

        # Extract inline code
        inline_code_pattern = r'`([^`]+)`'
        inline_matches = re.findall(inline_code_pattern, content)

        for match in inline_matches:
            if 'rx.' in match or 'reflex.' in match:
                code_blocks.append(match)

        return ' '.join(code_blocks)

    def clean_content(self, content: str) -> str:
        """Clean markdown content for better indexing."""
        # Remove frontmatter if present
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content = parts[2]

        # Convert to HTML and then extract text
        html = self.md.convert(content)
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()

        # Clean up whitespace
        text = re.sub(r'\n\s*\n', '\n\n', text)
        text = re.sub(r' +', ' ', text)

        return text.strip()


class TypesenseIndexer:
    """Enhanced indexer for Typesense with better error handling and batch processing."""

    def __init__(self, config: Dict[str, Any]):
        self.client = typesense.Client(config)
        self.processor = MarkdownProcessor()

    def create_collection(self, force_recreate: bool = False) -> bool:
        """Create or recreate the collection."""
        try:
            # Check if collection exists
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

            # Create collection
            logger.info("Creating collection...")
            self.client.collections.create(COLLECTION_SCHEMA)
            logger.info("Collection created successfully.")
            return True

        except Exception as e:
            logger.error(f"Error creating collection: {e}")
            return False

    def get_url_from_path(self, file_path: Path, docs_root: Path) -> str:
        """Generate URL from file path, handling ‘-ll’ suffixes as ‘…/low’."""
        relative_path = file_path.relative_to(docs_root)

        # Build the URL path segments (excluding the filename for now)
        url_parts = list(relative_path.parts[:-1])

        # Handle index.md specially
        if file_path.name == 'index.md':
            # e.g. docs/foo/index.md → /foo/
            url = '/' + '/'.join(url_parts) if url_parts else '/'
        else:
            stem = file_path.stem  # filename without .md

            # If the filename ends with “-ll”, strip it and add a “low” segment
            if stem.endswith('-ll'):
                base = stem[:-3]           # remove the “-ll”
                url_parts.append(base)     # e.g. …/foo
                url_parts.append('low')    # then …/low
            else:
                url_parts.append(stem)     # normal case

            url = '/' + '/'.join(url_parts)

        # Ensure no trailing slash (unless it’s the root)
        if url != '/' and url.endswith('/'):
            url = url.rstrip('/')

        return url

    def format_display_name(self, name: str) -> str:
        # Basic title casing
        parts = name.replace('-', ' ').replace('_', ' ').split()
        title = ' '.join([p.upper() if p.lower() in {"ai", "ui", "api"} else p.capitalize() for p in parts])
        return title

    def create_breadcrumb(self, document: dict) -> str:
            """Create a breadcrumb string from document metadata."""
            parts = []

            # Add section
            section = document.get('section', '')
            if section:
                section_display = self.format_display_name(section)
                parts.append(section_display)

            # Add subsection
            subsection = document.get('subsection', '')
            if subsection:
                subsection_display = subsection.replace('-', ' ').replace('_', ' ').title()
                parts.append(subsection_display)

            # Add title if different from last part
            title = document.get('title', '')
            if title and (not parts or title.lower() != parts[-1].lower()):
                parts.append(title)

            return ' › '.join(parts)


    def get_section_info(self, file_path: Path, docs_root: Path) -> tuple[str, Optional[str]]:
        """Extract section and subsection from file path."""
        relative_path = file_path.relative_to(docs_root)
        parts = relative_path.parts

        if len(parts) == 1:
            return 'blog', None
        elif len(parts) == 2:
            return parts[0], None
        else:
            return parts[0], parts[1]


    def process_file(self, file_path: Path, content_root: Path, is_blog: bool = False) -> Optional[Dict[str, Any]]:
        """Process a single markdown file."""
        def normalize_slug(s: str) -> str:
            return s.replace('_', '-')

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)

            metadata = post.metadata
            rel_path = file_path.relative_to(content_root)

            if is_blog:
                # Blog logic
                slug = normalize_slug(file_path.stem)
                url_path = '/blog/' + slug
                section = 'Blog'
                subsection = metadata.get('author', None)

                title = metadata.get('title', '')
                if not title:
                    headings = self.processor.extract_headings(post.content)
                    title = headings[0] if headings else slug.replace('-', ' ').title()
            else:
                # Docs logic (matching your cleaner version)
                path_parts = [normalize_slug(p) for p in rel_path.parts[:-1]]  # Remove filename and normalize
                url_path = '/' + '/'.join(['docs'] + path_parts)

                stem = normalize_slug(file_path.stem)
                if file_path.name != 'index.md':
                    if stem.endswith('-ll'):
                        stem = stem[:-3]  # Remove -ll
                        url_path += '/' + stem + '/low'
                    else:
                        url_path += '/' + stem

                if url_path != '/' and url_path.endswith('/'):
                    url_path = url_path.rstrip('/')

                section = path_parts[0] if path_parts else 'docs'
                subsection = path_parts[1] if len(path_parts) > 1 else None

                # Title logic
                if file_path.stem.endswith('-ll'):
                    base = stem.replace('-', ' ').title()
                    default_title = f"{base} Low Level"
                else:
                    default_title = stem.replace('-', ' ').title()
                title = metadata.get('title', default_title)

            # Common processing
            clean_content = self.processor.clean_content(post.content)
            headings = self.processor.extract_headings(post.content)
            components = list(self.processor.extract_components(post.content))
            code_examples = self.processor.extract_code_examples(post.content)

            doc = {
                'id': str(rel_path),
                'title': title,
                'content': clean_content,
                'headings': headings,
                'path': str(rel_path),
                'url': url_path,
                'section': section,
                'is_component': 'library' in rel_path.parts,
                'weight': 2 if not is_blog else 1,
            }

            doc['breadcrumb'] = self.create_breadcrumb(doc)

            if code_examples:
                doc['code_examples'] = code_examples
            if components:
                doc['components'] = components
            if subsection:
                doc['subsection'] = subsection

            return doc

        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
            return None

    def index_documents(self, docs_root: Path, batch_size: int = 100, is_blog: bool = False) -> bool:
        """Index all markdown files in the docs directory."""
        try:
            # Find all markdown files
            markdown_files = list(docs_root.rglob('*.md'))
            logger.info(f"Found {len(markdown_files)} markdown files")

            # Process files in batches
            documents = []
            processed = 0

            for file_path in markdown_files:
                doc = self.process_file(file_path, docs_root, is_blog)
                if doc:
                    documents.append(doc)
                    processed += 1

                    # Index batch when full
                    if len(documents) >= batch_size:
                        self._index_batch(documents)
                        documents = []
                        logger.info(f"Processed {processed}/{len(markdown_files)} files")

            # Index remaining documents
            if documents:
                self._index_batch(documents)
                logger.info(f"Processed {processed}/{len(markdown_files)} files")

            logger.info("Indexing completed successfully!")
            return True

        except Exception as e:
            logger.error(f"Error during indexing: {e}")
            return False

    def _index_batch(self, documents: List[Dict[str, Any]]) -> None:
        """Index a batch of documents."""
        try:
            results = self.client.collections['docs'].documents.import_(
                documents,
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

    parser = argparse.ArgumentParser(description='Index Reflex documentation to Typesense')
    parser.add_argument('--docs-path', default='./docs', help='Path to docs directory')
    parser.add_argument('--blog-path', default='./blog', help='Path to blog directory')
    parser.add_argument('--force', action='store_true', help='Force recreate collection')
    parser.add_argument('--batch-size', type=int, default=100, help='Batch size for indexing')

    args = parser.parse_args()

    # Validate environment variables
    if not os.getenv('TYPESENSE_HOST'):
        logger.error("TYPESENSE_HOST environment variable is required")
        sys.exit(1)

    if not os.getenv('TYPESENSE_ADMIN_API_KEY'):
        logger.error("TYPESENSE_ADMIN_API_KEY environment variable is required")
        sys.exit(1)

    # Validate docs path
    docs_path = Path(args.docs_path)
    if not docs_path.exists():
        logger.error(f"Docs path does not exist: {docs_path}")
        sys.exit(1)

    # Validate blog path
    blog_path = Path(args.blog_path)
    if not blog_path.exists():
        logger.error(f"Blog path does not exist: {blog_path}")
        sys.exit(1)

    # Initialize indexer
    indexer = TypesenseIndexer(TYPESENSE_CONFIG)

    # Create collection
    if not indexer.create_collection(force_recreate=args.force):
        logger.error("Failed to create collection")
        sys.exit(1)

    # Index docs
    if not indexer.index_documents(docs_path, batch_size=args.batch_size):
        logger.error("Failed to index docs")
        sys.exit(1)

    # Index blog
    if not indexer.index_documents(blog_path, batch_size=args.batch_size, is_blog=True):
        logger.error("Failed to index blog")
        sys.exit(1)

    logger.info("Indexing process completed successfully!")


if __name__ == '__main__':
    main()
