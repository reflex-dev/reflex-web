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
        {'name': 'code_examples', 'type': 'string', 'optional': True},  # Preserve code examples
        {'name': 'headings', 'type': 'string[]'},
        {'name': 'path', 'type': 'string'},
        {'name': 'url', 'type': 'string'},
        {'name': 'components', 'type': 'string[]', 'optional': True},
        {'name': 'section', 'type': 'string'},
        {'name': 'subsection', 'type': 'string', 'optional': True},
    ]
}

# Common Reflex components for better detection
REFLEX_COMPONENTS = {
    'rx.text', 'rx.button', 'rx.input', 'rx.box', 'rx.flex', 'rx.image', 'rx.link',
    'rx.icon', 'rx.form', 'rx.table', 'rx.chart', 'rx.modal', 'rx.dialog', 'rx.select',
    'rx.slider', 'rx.switch', 'rx.checkbox', 'rx.radio', 'rx.textarea', 'rx.upload',
    'rx.progress', 'rx.badge', 'rx.card', 'rx.tooltip', 'rx.popover', 'rx.drawer',
    'rx.tabs', 'rx.accordion', 'rx.alert', 'rx.breadcrumb', 'rx.menu', 'rx.pagination',
    'rx.divider', 'rx.spacer', 'rx.center', 'rx.container', 'rx.stack', 'rx.hstack',
    'rx.vstack', 'rx.grid', 'rx.responsive_grid', 'rx.fragment', 'rx.cond', 'rx.foreach',
    'rx.moment', 'rx.html', 'rx.markdown', 'rx.code', 'rx.heading', 'rx.span',
    'rx.em', 'rx.strong', 'rx.kbd', 'rx.highlight', 'rx.color_picker', 'rx.debounce_input',
    'rx.editor', 'rx.data_table', 'rx.plotly', 'rx.recharts', 'rx.chakra', 'rx.radix'
}


class MarkdownProcessor:
    """Enhanced processor for markdown files with better component detection."""

    def __init__(self):
        self.md = Markdown(extensions=['meta', 'toc'])

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

    def extract_components(self, content: str) -> Set[str]:
        """Extract Reflex components mentioned in the content."""
        components = set()

        # Pattern to match rx.component_name or reflex.component_name
        component_pattern = r'(?:^|\s)(rx\.[a-zA-Z_][a-zA-Z0-9_]*|reflex\.[a-zA-Z_][a-zA-Z0-9_]*)'

        # Find all component mentions
        matches = re.findall(component_pattern, content, re.MULTILINE)

        for match in matches:
            # Normalize to rx.component format
            if match.startswith('reflex.'):
                match = 'rx.' + match[7:]  # Replace 'reflex.' with 'rx.'

            # Only include known components or ones that follow naming conventions
            if match in REFLEX_COMPONENTS or self._is_likely_component(match):
                components.add(match)

        # Also check for component names in headings and documentation
        for heading in self.extract_headings(content):
            heading_lower = heading.lower()
            for component in REFLEX_COMPONENTS:
                comp_name = component.replace('rx.', '')
                if comp_name in heading_lower or heading_lower.replace(' ', '_') == comp_name:
                    components.add(component)

        return components

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
        """Generate URL from file path."""
        relative_path = file_path.relative_to(docs_root)

        # Convert path to URL format
        url_parts = []
        for part in relative_path.parts[:-1]:  # Exclude filename
            url_parts.append(part)

        # Handle index files
        if file_path.name == 'index.md':
            url = '/' + '/'.join(url_parts) if url_parts else '/'
        else:
            # Remove .md extension
            filename = file_path.stem
            url_parts.append(filename)
            url = '/' + '/'.join(url_parts)

        return url

    def get_section_info(self, file_path: Path, docs_root: Path) -> tuple[str, Optional[str]]:
        """Extract section and subsection from file path."""
        relative_path = file_path.relative_to(docs_root)
        parts = relative_path.parts

        if len(parts) == 1:
            return 'root', None
        elif len(parts) == 2:
            return parts[0], None
        else:
            return parts[0], parts[1]

    def process_file(self, file_path: Path, docs_root: Path) -> Optional[Dict[str, Any]]:
        """Process a single markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Parse frontmatter
            post = frontmatter.loads(content)

            # Extract title
            title = post.metadata.get('title', file_path.stem.replace('-', ' ').title())

            # Process content
            clean_content = self.processor.clean_content(post.content)
            headings = self.processor.extract_headings(post.content)
            components = list(self.processor.extract_components(post.content))
            code_examples = self.processor.extract_code_examples(post.content)

            # Get path info
            url = self.get_url_from_path(file_path, docs_root)
            section, subsection = self.get_section_info(file_path, docs_root)

            # Create document
            doc = {
                'id': str(file_path.relative_to(docs_root)),
                'title': title,
                'content': clean_content,
                'headings': headings,
                'path': str(file_path.relative_to(docs_root)),
                'url': url,
                'section': section,
            }

            # Add optional fields
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

    def index_documents(self, docs_root: Path, batch_size: int = 100) -> bool:
        """Index all markdown files in the docs directory."""
        try:
            # Find all markdown files
            markdown_files = list(docs_root.rglob('*.md'))
            logger.info(f"Found {len(markdown_files)} markdown files")

            # Process files in batches
            documents = []
            processed = 0

            for file_path in markdown_files:
                doc = self.process_file(file_path, docs_root)
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

    # Initialize indexer
    indexer = TypesenseIndexer(TYPESENSE_CONFIG)

    # Create collection
    if not indexer.create_collection(force_recreate=args.force):
        logger.error("Failed to create collection")
        sys.exit(1)

    # Index documents
    if not indexer.index_documents(docs_path, batch_size=args.batch_size):
        logger.error("Failed to index documents")
        sys.exit(1)

    logger.info("Indexing process completed successfully!")


if __name__ == '__main__':
    main()
