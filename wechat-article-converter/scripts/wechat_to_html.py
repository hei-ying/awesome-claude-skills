#!/usr/bin/env python3
"""
WeChat Article to HTML Converter

This script fetches WeChat articles and converts them to standalone HTML format with:
- Article metadata (title, author, publish date)
- Full text content with original formatting and styles
- Images embedded as Base64 data URIs
- Clean, styled output suitable for viewing or archiving
"""

import requests
import re
import sys
from datetime import datetime


class WeChatArticleToHTML:
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
            'publish_date': ''
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

    def extract_content(self, html):
        """Extract article content HTML"""
        # Find the main content area
        content_match = re.search(r'<div[^>]*class="rich_media_content[^"]*"[^>]*>(.*?)</div>\s*(?:<script|<div[^>]*class="rich_media_tool)', html, re.DOTALL)
        if not content_match:
            return None

        return content_match.group(1)

    def download_and_embed_images(self, html_content):
        """Download images and embed them as Base64 data URIs"""
        def replace_image(match):
            img_tag = match.group(0)
            # Try to find data-src first (lazy loading), then src
            src_match = re.search(r'data-src="([^"]+)"', img_tag)
            if not src_match:
                src_match = re.search(r'src="([^"]+)"', img_tag)

            if src_match:
                img_url = src_match.group(1)
                # Handle relative URLs
                if img_url.startswith('//'):
                    img_url = 'https:' + img_url
                elif img_url.startswith('/'):
                    img_url = 'https://mp.weixin.qq.com' + img_url

                try:
                    response = self.session.get(img_url, timeout=15)
                    response.raise_for_status()

                    # Determine content type
                    content_type = response.headers.get('Content-Type', 'image/jpeg')
                    if 'image/' not in content_type:
                        content_type = 'image/jpeg'

                    # Convert to Base64
                    import base64
                    base64_data = base64.b64encode(response.content).decode('utf-8')
                    data_uri = f"data:{content_type};base64,{base64_data}"

                    # Replace src with data URI
                    new_tag = re.sub(r'(data-)?src="[^"]*"', f'src="{data_uri}"', img_tag)
                    return new_tag
                except Exception as e:
                    print(f"Warning: Failed to download image {img_url}: {e}", file=sys.stderr)
                    return img_tag

            return img_tag

        # Process all images
        html_content = re.sub(r'<img[^>]*>', replace_image, html_content)
        return html_content

    def generate_html(self, metadata, content):
        """Generate complete standalone HTML document"""
        html_template = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="{metadata['author']}">
    <meta name="description" content="{metadata['title']}">
    <title>{metadata['title']}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif;
            font-size: 16px;
            line-height: 1.8;
            color: #333;
            background: #f5f5f5;
            padding: 20px;
        }}

        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: #fff;
            padding: 40px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border-radius: 8px;
        }}

        h1 {{
            font-size: 28px;
            font-weight: bold;
            line-height: 1.4;
            margin-bottom: 20px;
            color: #000;
            word-wrap: break-word;
        }}

        .metadata {{
            color: #888;
            font-size: 14px;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid #eee;
        }}

        .metadata span {{
            margin-right: 15px;
            display: inline-block;
        }}

        .content {{
            font-size: 16px;
            line-height: 1.8;
            word-wrap: break-word;
        }}

        .content p {{
            margin: 15px 0;
            text-align: justify;
        }}

        .content img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto;
            border-radius: 4px;
        }}

        .content h2 {{
            font-size: 22px;
            font-weight: bold;
            margin: 30px 0 15px 0;
            color: #000;
        }}

        .content h3 {{
            font-size: 20px;
            font-weight: bold;
            margin: 25px 0 12px 0;
            color: #000;
        }}

        .content h4 {{
            font-size: 18px;
            font-weight: bold;
            margin: 20px 0 10px 0;
            color: #000;
        }}

        .content strong {{
            font-weight: bold;
            color: #000;
        }}

        .content em {{
            font-style: italic;
        }}

        .content a {{
            color: #576b95;
            text-decoration: none;
            word-wrap: break-word;
        }}

        .content a:hover {{
            text-decoration: underline;
        }}

        .content blockquote {{
            margin: 20px 0;
            padding: 10px 20px;
            background: #f7f7f7;
            border-left: 4px solid #d0d0d0;
            color: #666;
        }}

        .content ul, .content ol {{
            margin: 15px 0;
            padding-left: 30px;
        }}

        .content li {{
            margin: 8px 0;
        }}

        .content pre {{
            background: #f6f6f6;
            padding: 15px;
            border-radius: 4px;
            overflow-x: auto;
            margin: 15px 0;
        }}

        .content code {{
            background: #f0f0f0;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 14px;
        }}

        .content table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}

        .content table th,
        .content table td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}

        .content table th {{
            background: #f5f5f5;
            font-weight: bold;
        }}

        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            font-size: 12px;
            color: #999;
            text-align: center;
        }}

        .footer a {{
            color: #576b95;
            text-decoration: none;
            word-wrap: break-word;
        }}

        @media print {{
            body {{
                background: #fff;
                padding: 0;
            }}

            .container {{
                box-shadow: none;
                padding: 20px;
            }}
        }}

        @media (max-width: 768px) {{
            body {{
                padding: 10px;
            }}

            .container {{
                padding: 20px;
            }}

            h1 {{
                font-size: 24px;
            }}

            .content {{
                font-size: 15px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{metadata['title']}</h1>
        <div class="metadata">
            <span><strong>作者:</strong> {metadata['author']}</span>
            <span><strong>发布时间:</strong> {metadata['publish_date']}</span>
        </div>
        <div class="content">
            {content}
        </div>
        <div class="footer">
            <p><strong>原文链接:</strong> <a href="{self.url}" target="_blank">{self.url}</a></p>
            <p>转换时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
    </div>
</body>
</html>"""
        return html_template

    def convert_to_html(self, output_file):
        """Main conversion method"""
        print(f"Fetching article from: {self.url}")
        html = self.fetch_article()

        if not html:
            return False

        print("Extracting metadata...")
        metadata = self.extract_metadata(html)

        print("Extracting content...")
        content = self.extract_content(html)

        if not content:
            print("Error: Could not extract article content")
            return False

        print("Downloading and embedding images...")
        content = self.download_and_embed_images(content)

        print("Generating HTML...")
        output_html = self.generate_html(metadata, content)

        print("Saving HTML file...")
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(output_html)
            print(f"\nSuccessfully converted to HTML: {output_file}")
            return True
        except Exception as e:
            print(f"Error saving HTML file: {e}", file=sys.stderr)
            return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python wechat_to_html.py <wechat_article_url> [output_file.html]")
        print("Example: python wechat_to_html.py https://mp.weixin.qq.com/s/xxxxx article.html")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "wechat_article.html"

    # Ensure output file has .html extension
    if not output_file.endswith('.html'):
        output_file += '.html'

    # Validate URL
    if 'mp.weixin.qq.com' not in url:
        print("Error: Please provide a valid WeChat article URL (mp.weixin.qq.com)")
        sys.exit(1)

    converter = WeChatArticleToHTML(url)
    success = converter.convert_to_html(output_file)

    if not success:
        print("Conversion failed!")
        sys.exit(1)


if __name__ == '__main__':
    main()
