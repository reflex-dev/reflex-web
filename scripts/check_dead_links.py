#!/usr/bin/env python3
"""
Dead link checker for the Reflex website.
Crawls the deployed site and checks for broken links.
"""

import argparse
import re
import sys
import time
from collections import deque
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


class DeadLinkChecker:
    def __init__(self, base_url, max_pages=None, timeout=10, delay=0.5):
        self.base_url = base_url.rstrip('/')
        self.domain = urlparse(base_url).netloc
        self.max_pages = max_pages
        self.timeout = timeout
        self.delay = delay
        
        self.visited_pages = set()
        self.checked_links = set()
        self.dead_links = []
        self.pages_to_visit = deque([base_url])
        
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; DeadLinkChecker/1.0)'
        })

    def is_internal_url(self, url):
        """Check if URL is internal to our domain."""
        parsed = urlparse(url)
        return parsed.netloc == self.domain or parsed.netloc == ''

    def normalize_url(self, url):
        """Normalize URL for comparison."""
        parsed = urlparse(url)
        normalized = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        if parsed.query:
            normalized += f"?{parsed.query}"
        return normalized

    def check_link(self, url, source_page):
        """Check if a single link is working."""
        if url in self.checked_links:
            return True
            
        self.checked_links.add(url)
        
        parsed = urlparse(url)
        if parsed.netloc in ['fonts.googleapis.com', 'fonts.gstatic.com']:
            return True
        
        try:
            response = self.session.head(url, timeout=self.timeout, allow_redirects=True)
            
            if response.status_code == 405:
                response = self.session.get(url, timeout=self.timeout, allow_redirects=True)
            
            if response.status_code == 403 and parsed.netloc in ['twitter.com', 'www.twitter.com', 'x.com', 'www.x.com']:
                print(f"Warning: Twitter/X link may be blocked by bot detection: {url}")
                return True
            
            if response.status_code >= 400:
                self.dead_links.append({
                    'url': url,
                    'status_code': response.status_code,
                    'source_page': source_page,
                    'error': f"HTTP {response.status_code}"
                })
                return False
                
        except requests.exceptions.RequestException as e:
            self.dead_links.append({
                'url': url,
                'status_code': None,
                'source_page': source_page,
                'error': str(e)
            })
            return False
            
        return True

    def extract_links(self, html, page_url):
        """Extract all links from HTML content."""
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        
        for tag in soup.find_all(['a', 'link', 'img', 'script']):
            url = None
            if tag.name == 'a':
                url = tag.get('href')
            elif tag.name == 'link':
                url = tag.get('href')
            elif tag.name == 'img':
                url = tag.get('src')
            elif tag.name == 'script':
                url = tag.get('src')
                
            if url:
                absolute_url = urljoin(page_url, url)
                if not absolute_url.startswith(('javascript:', 'mailto:', 'tel:')):
                    links.append(absolute_url)
                    
        return links

    def crawl_page(self, url):
        """Crawl a single page and extract links."""
        if url in self.visited_pages or (self.max_pages and len(self.visited_pages) >= self.max_pages):
            return []
            
        self.visited_pages.add(url)
        print(f"Crawling: {url}")
        
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            content_type = response.headers.get('content-type', '').lower()
            if 'text/html' not in content_type:
                return []
                
            links = self.extract_links(response.text, url)
            
            for link in links:
                self.check_link(link, url)
                
                if self.is_internal_url(link):
                    normalized = self.normalize_url(link)
                    if normalized not in self.visited_pages:
                        self.pages_to_visit.append(normalized)
            
            time.sleep(self.delay)
            return links
            
        except requests.exceptions.RequestException as e:
            print(f"Error crawling {url}: {e}")
            return []

    def run(self):
        """Run the dead link checker."""
        print(f"Starting dead link check for {self.base_url}")
        print(f"Max pages: {self.max_pages}, Timeout: {self.timeout}s")
        
        while self.pages_to_visit and (not self.max_pages or len(self.visited_pages) < self.max_pages):
            url = self.pages_to_visit.popleft()
            self.crawl_page(url)
        
        print(f"\nCrawl complete!")
        print(f"Pages visited: {len(self.visited_pages)}")
        print(f"Links checked: {len(self.checked_links)}")
        print(f"Dead links found: {len(self.dead_links)}")
        
        if self.dead_links:
            print("\n❌ DEAD LINKS FOUND:")
            for link_info in self.dead_links:
                print(f"  URL: {link_info['url']}")
                print(f"  Error: {link_info['error']}")
                print(f"  Found on: {link_info['source_page']}")
                print()
            return False
        else:
            print("\n✅ No dead links found!")
            return True


def main():
    parser = argparse.ArgumentParser(description='Check for dead links on a website')
    parser.add_argument('url', help='Base URL to start crawling from')
    parser.add_argument('--max-pages', type=int, default=500, help='Maximum pages to crawl')
    parser.add_argument('--timeout', type=int, default=10, help='Request timeout in seconds')
    parser.add_argument('--delay', type=float, default=0.5, help='Delay between requests')
    
    args = parser.parse_args()
    
    checker = DeadLinkChecker(
        base_url=args.url,
        max_pages=args.max_pages,
        timeout=args.timeout,
        delay=args.delay
    )
    
    success = checker.run()
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
