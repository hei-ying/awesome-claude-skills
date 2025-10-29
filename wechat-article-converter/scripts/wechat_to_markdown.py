#!/usr/bin/env python3
"""
WeChat Article to Markdown Converter

This script fetches WeChat articles and converts them to Markdown format with:
- Article metadata (title, author, publish date)
- Full text content with proper formatting
- Images embedded as Base64 data URIs
"""

import requests
import re
import base64
from urllib.parse import urlparse
from datetime import datetime
import sys
import time


class WeChatArticleConverter:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def fetch_article(self):
        """Fetch the WeChat article HTML content"""
        try:
            response = self.session.get(self.url, timeout=30)
            response.raise_for_status()
            response.encoding = 'utf-8'
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching article: {e}", file=sys.stderr)
            return None

    def extract_metadata(self, html):
        """Extract article metadata"""
        metadata = {
            'title': '',
            'author': '',
            'publish_date': '',
            'account': ''
        }

        # Extract title
        title_match = re.search(r'<h1[^>]*class="rich_media_title"[^>]*>(.*?)</h1>', html, re.DOTALL)
        if title_match:
            metadata['title'] = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()

        # Extract author
        author_match = re.search(r'<span[^>]*class="rich_media_meta_nickname"[^>]*>(.*?)</span>', html, re.DOTALL)
        if not author_match:
            author_match = re.search(r'var\s+nickname\s*=\s*"([^"]+)"', html)
        if author_match:
            metadata['author'] = re.sub(r'<[^>]+>', '', author_match.group(1)).strip()

        # Extract publish date
        date_match = re.search(r'<span[^>]*class="rich_media_meta_text"[^>]*>(.*?)</span>', html, re.DOTALL)
        if not date_match:
            date_match = re.search(r'var\s+publish_time\s*=\s*"([^"]+)"', html)
        if date_match:
            metadata['publish_date'] = re.sub(r'<[^>]+>', '', date_match.group(1)).strip()

        return metadata

    def download_image_as_base64(self, img_url):
        """Download image and convert to Base64"""
        try:
            # Handle relative URLs
            if img_url.startswith('//'):
                img_url = 'https:' + img_url
            elif img_url.startswith('/'):
                img_url = 'https://mp.weixin.qq.com' + img_url

            response = self.session.get(img_url, timeout=15)
            response.raise_for_status()

            # Determine content type
            content_type = response.headers.get('Content-Type', 'image/jpeg')
            if 'image/' not in content_type:
                content_type = 'image/jpeg'

            # Convert to Base64
            base64_data = base64.b64encode(response.content).decode('utf-8')
            return f"data:{content_type};base64,{base64_data}"
        except Exception as e:
            print(f"Warning: Failed to download image {img_url}: {e}", file=sys.stderr)
            return img_url  # Fallback to original URL

    def extract_content(self, html):
        """Extract and convert article content to Markdown"""
        # Find the main content area
        content_match = re.search(r'<div[^>]*class="rich_media_content[^"]*"[^>]*>(.*?)</div>\s*(?:<script|<div[^>]*class="rich_media_tool)', html, re.DOTALL)
        if not content_match:
            return "Error: Could not extract article content"

        content = content_match.group(1)

        # Process images - convert to Base64
        def replace_image(match):
            img_tag = match.group(0)
            # Try to find data-src first (lazy loading), then src
            src_match = re.search(r'data-src="([^"]+)"', img_tag)
            if not src_match:
                src_match = re.search(r'src="([^"]+)"', img_tag)

            if src_match:
                img_url = src_match.group(1)
                base64_url = self.download_image_as_base64(img_url)
                # Get alt text if available
                alt_match = re.search(r'alt="([^"]*)"', img_tag)
                alt_text = alt_match.group(1) if alt_match else ""
                return f'\n![{alt_text}]({base64_url})\n'
            return ""

        content = re.sub(r'<img[^>]*>', replace_image, content)

        # Convert headings
        content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n# \1\n', content, flags=re.DOTALL)
        content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', content, flags=re.DOTALL)
        content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', content, flags=re.DOTALL)
        content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'\n#### \1\n', content, flags=re.DOTALL)

        # Convert bold and italic
        content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', content, flags=re.DOTALL)
        content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', content, flags=re.DOTALL)
        content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', content, flags=re.DOTALL)
        content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', content, flags=re.DOTALL)

        # Convert links
        content = re.sub(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', content, flags=re.DOTALL)

        # Convert line breaks and paragraphs
        content = re.sub(r'<br\s*/?>', '\n', content)
        content = re.sub(r'</p>\s*<p[^>]*>', '\n\n', content)
        content = re.sub(r'<p[^>]*>', '\n', content)
        content = re.sub(r'</p>', '\n', content)

        # Convert lists
        content = re.sub(r'<ul[^>]*>(.*?)</ul>', lambda m: self._convert_list(m.group(1), ordered=False), content, flags=re.DOTALL)
        content = re.sub(r'<ol[^>]*>(.*?)</ol>', lambda m: self._convert_list(m.group(1), ordered=True), content, flags=re.DOTALL)

        # Convert blockquotes
        content = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', lambda m: '\n> ' + m.group(1).strip().replace('\n', '\n> ') + '\n', content, flags=re.DOTALL)

        # Remove remaining HTML tags
        content = re.sub(r'<[^>]+>', '', content)

        # Decode HTML entities
        content = content.replace('&nbsp;', ' ')
        content = content.replace('&lt;', '<')
        content = content.replace('&gt;', '>')
        content = content.replace('&amp;', '&')
        content = content.replace('&quot;', '"')
        content = content.replace('&#39;', "'")

        # Clean up extra whitespace
        content = re.sub(r'\n{3,}', '\n\n', content)
        content = content.strip()

        return content

    def _convert_list(self, list_html, ordered=False):
        """Convert HTML list to Markdown"""
        items = re.findall(r'<li[^>]*>(.*?)</li>', list_html, re.DOTALL)
        result = '\n'
        for i, item in enumerate(items, 1):
            item = re.sub(r'<[^>]+>', '', item).strip()
            prefix = f'{i}. ' if ordered else '- '
            result += f'{prefix}{item}\n'
        return result + '\n'

    def convert_to_markdown(self):
        """Main conversion method"""
        print(f"Fetching article from: {self.url}")
        html = self.fetch_article()

        if not html:
            return None

        print("Extracting metadata...")
        metadata = self.extract_metadata(html)

        print("Converting content to Markdown...")
        content = self.extract_content(html)

        # Build Markdown document
        markdown = f"""# {metadata['title']}

**Author:** {metadata['author']}
**Published:** {metadata['publish_date']}
**Source:** {self.url}

---

{content}

---

*Converted to Markdown on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

        return markdown


def main():
    if len(sys.argv) < 2:
        print("Usage: python wechat_to_markdown.py <wechat_article_url> [output_file]")
        print("Example: python wechat_to_markdown.py https://mp.weixin.qq.com/s/xxxxx article.md")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    # Validate URL
    if 'mp.weixin.qq.com' not in url:
        print("Error: Please provide a valid WeChat article URL (mp.weixin.qq.com)")
        sys.exit(1)

    converter = WeChatArticleConverter(url)
    markdown = converter.convert_to_markdown()

    if markdown:
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(markdown)
            print(f"\nSuccessfully converted to: {output_file}")
        else:
            print("\n" + "="*80)
            print(markdown)
            print("="*80)
    else:
        print("Conversion failed!")
        sys.exit(1)


if __name__ == '__main__':
    main()
