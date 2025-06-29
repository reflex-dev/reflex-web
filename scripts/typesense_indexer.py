#!/usr/bin/env python3
"""
Typesense indexing script for Reflex documentation.

This script parses all markdown files in the docs folder and indexes them
to Typesense for search functionality.
"""

import os
import sys
import json
import re
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional
import frontmatter
import typesense
from markdown import Markdown
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

TYPESENSE_CONFIG = {
    'nodes': [{
        'host': 'z2mi3hyewokc16a4p-1.a1.typesense.net',
        'port': '443',
        'protocol': 'https'
    }],
    'api_key': os.getenv('TYPESENSE_ADMIN_API_KEY'),
    'connection_timeout_seconds': 60
}

COLLECTION_SCHEMA = {
    'name': 'docs',
    'fields': [
        {'name': 'id', 'type': 'string'},
        {'name': 'title', 'type': 'string'},
        {'name': 'content', 'type': 'string'},
        {'name': 'headings', 'type': 'string[]'},
        {'name': 'path', 'type': 'string'},
        {'name': 'url', 'type': 'string'},
        {'name': 'components', 'type': 'string[]', 'optional': True},
        {'name': 'section', 'type': 'string'},
        {'name': 'subsection', 'type': 'string', 'optional': True},
    ]
}


class MarkdownProcessor:
    """Process markdown files and extract searchable content."""
    
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
    
    def clean_content(self, content: str) -> str:
        """Clean markdown content for indexing."""
        content = re.sub(r'```[^`]*```', '', content, flags=re.DOTALL)
        
        content = re.sub(r'`[^`]*`', '', content)
        
        content = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', content)
        
        content = re.sub(r'[*_~`]', '', content)
        
        content = re.sub(r'<[^>]*>', '', content)
        
        content = re.sub(r'^---.*?---', '', content, flags=re.DOTALL | re.MULTILINE)
        
        content = re.sub(r'```python exec.*?```', '', content, flags=re.DOTALL)
        
        content = re.sub(r'```python demo.*?```', '', content, flags=re.DOTALL)
        
        content = re.sub(r'```python eval.*?```', '', content, flags=re.DOTALL)
        
        content = re.sub(r'\n\s*\n', '\n\n', content)
        content = content.strip()
        
        return content
    
    def process_file(self, file_path: Path, docs_root: Path) -> Optional[Dict[str, Any]]:
        """Process a single markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            metadata = post.metadata
            content = post.content
            
            rel_path = file_path.relative_to(docs_root)
            path_parts = list(rel_path.parts[:-1])  # Remove filename
            
            url_path = '/' + '/'.join(['docs'] + path_parts)
            if file_path.name != 'index.md':
                url_path += '/' + file_path.stem
            
            if url_path != '/' and url_path.endswith('/'):
                url_path = url_path.rstrip('/')
            
            title = metadata.get('title', '')
            if not title:
                headings = self.extract_headings(content)
                title = headings[0] if headings else file_path.stem.replace('-', ' ').replace('_', ' ').title()
            
            components = metadata.get('components', [])
            if isinstance(components, str):
                components = [components]
            
            headings = self.extract_headings(content)
            
            clean_content = self.clean_content(content)
            
            section = path_parts[0] if path_parts else 'docs'
            subsection = path_parts[1] if len(path_parts) > 1 else None
            
            document = {
                'title': title,
                'content': clean_content,
                'headings': headings,
                'path': str(rel_path),
                'url': url_path,
                'section': section,
            }
            
            if components:
                document['components'] = components
            
            if subsection:
                document['subsection'] = subsection
            
            return document
            
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
            return None


class TypesenseIndexer:
    """Handle Typesense indexing operations."""
    
    def __init__(self):
        self.client = typesense.Client(TYPESENSE_CONFIG)
    
    def recreate_collection(self):
        """Recreate the docs collection."""
        try:
            self.client.collections['docs'].delete()
            logger.info("Deleted existing 'docs' collection")
        except Exception as e:
            logger.info(f"Collection 'docs' doesn't exist or couldn't be deleted: {e}")
        
        self.client.collections.create(COLLECTION_SCHEMA)
        logger.info("Created new 'docs' collection")
    
    def index_documents(self, documents: List[Dict[str, Any]]):
        """Index documents to Typesense."""
        if not documents:
            logger.warning("No documents to index")
            return
        
        try:
            batch_size = 100
            for i in range(0, len(documents), batch_size):
                batch = documents[i:i + batch_size]
                for j, doc in enumerate(batch):
                    doc['id'] = str(i + j + 1)
                result = self.client.collections['docs'].documents.import_(batch)
                logger.info(f"Indexed batch {i//batch_size + 1}: {len(batch)} documents")
            
            logger.info(f"Successfully indexed {len(documents)} documents")
            
        except Exception as e:
            logger.error(f"Error indexing documents: {e}")
            raise


def verify_indexing_coverage(docs_root: Path, processed_files: List[Path], failed_files: List[tuple]) -> bool:
    """Verify that all markdown files were processed and indexed."""
    all_md_files = list(docs_root.rglob('*.md'))
    total_found = len(all_md_files)
    total_processed = len(processed_files)
    total_failed = len(failed_files)
    
    logger.info("=" * 60)
    logger.info("INDEXING COVERAGE VERIFICATION REPORT")
    logger.info("=" * 60)
    logger.info(f"Total markdown files found: {total_found}")
    logger.info(f"Successfully processed: {total_processed}")
    logger.info(f"Failed to process: {total_failed}")
    logger.info(f"Coverage: {(total_processed / total_found * 100):.1f}%")
    
    if failed_files:
        logger.error("FAILED FILES:")
        for file_path, error in failed_files:
            rel_path = file_path.relative_to(docs_root)
            logger.error(f"  - {rel_path}: {error}")
    
    attempted_files = set(processed_files + [f[0] for f in failed_files])
    missing_files = set(all_md_files) - attempted_files
    
    if missing_files:
        logger.error("FILES NOT ATTEMPTED:")
        for file_path in missing_files:
            rel_path = file_path.relative_to(docs_root)
            logger.error(f"  - {rel_path}")
    
    sections = {}
    for file_path in all_md_files:
        rel_path = file_path.relative_to(docs_root)
        section = rel_path.parts[0] if rel_path.parts else 'root'
        if section not in sections:
            sections[section] = {'total': 0, 'processed': 0, 'failed': 0}
        sections[section]['total'] += 1
        
        if file_path in processed_files:
            sections[section]['processed'] += 1
        elif file_path in [f[0] for f in failed_files]:
            sections[section]['failed'] += 1
    
    logger.info("\nSECTION BREAKDOWN:")
    for section, stats in sorted(sections.items()):
        coverage = (stats['processed'] / stats['total'] * 100) if stats['total'] > 0 else 0
        logger.info(f"  {section}: {stats['processed']}/{stats['total']} ({coverage:.1f}%) - {stats['failed']} failed")
    
    success = total_processed == total_found and total_failed == 0
    
    if success:
        logger.info("✅ ALL MARKDOWN FILES SUCCESSFULLY INDEXED!")
    else:
        logger.error("❌ INDEXING INCOMPLETE - Some files were not processed")
    
    logger.info("=" * 60)
    return success


def main():
    """Main indexing function with comprehensive verification."""
    repo_root = Path(__file__).parent.parent
    docs_root = repo_root / 'docs'
    
    if not docs_root.exists():
        logger.error(f"Docs directory not found: {docs_root}")
        sys.exit(1)
    
    logger.info(f"Starting indexing process for docs in: {docs_root}")
    
    processor = MarkdownProcessor()
    indexer = TypesenseIndexer()
    
    md_files = list(docs_root.rglob('*.md'))
    logger.info(f"Found {len(md_files)} markdown files")
    
    documents = []
    processed_files = []
    failed_files = []
    
    for md_file in md_files:
        try:
            doc = processor.process_file(md_file, docs_root)
            if doc:
                documents.append(doc)
                processed_files.append(md_file)
            else:
                failed_files.append((md_file, "process_file returned None"))
        except Exception as e:
            failed_files.append((md_file, str(e)))
            logger.error(f"Failed to process {md_file.relative_to(docs_root)}: {e}")
    
    logger.info(f"Processed {len(documents)} documents successfully")
    
    coverage_success = verify_indexing_coverage(docs_root, processed_files, failed_files)
    
    if not coverage_success:
        logger.error("Indexing coverage verification failed!")
        sys.exit(1)
    
    indexer.recreate_collection()
    indexer.index_documents(documents)
    
    try:
        search_result = indexer.client.collections['docs'].documents.search({
            'q': '*',
            'query_by': 'title',
            'per_page': 1
        })
        indexed_count = search_result['found']
        logger.info(f"Verification: {indexed_count} documents confirmed in Typesense")
        
        if indexed_count != len(documents):
            logger.error(f"Mismatch: Expected {len(documents)} but Typesense has {indexed_count}")
            sys.exit(1)
        
    except Exception as e:
        logger.error(f"Failed to verify indexed documents: {e}")
        sys.exit(1)
    
    logger.info("✅ Indexing completed successfully with full verification!")


if __name__ == '__main__':
    main()
