#!/usr/bin/env python3
"""
WeChat Article to PDF Converter

This script fetches WeChat articles and converts them to PDF format with:
- Article metadata (title, author, publish date)
- Full text content with original formatting and styles
- Images embedded as Base64 within the PDF
"""

import requests
import re
import sys
from datetime import datetime
from io import BytesIO


class WeChatArticleToPDF:
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

    def generate_pdf_html(self, metadata, content):
        """Generate complete HTML for PDF conversion"""
        html_template = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{metadata['title']}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif;
            font-size: 16px;
            line-height: 1.8;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
            background: #fff;
        }}
        h1 {{
            font-size: 28px;
            font-weight: bold;
            line-height: 1.4;
            margin-bottom: 20px;
            color: #000;
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
        }}
        .content {{
            font-size: 16px;
            line-height: 1.8;
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
        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            font-size: 12px;
            color: #999;
            text-align: center;
        }}
    </style>
</head>
<body>
    <h1>{metadata['title']}</h1>
    <div class="metadata">
        <span><strong>作者:</strong> {metadata['author']}</span>
        <span><strong>发布时间:</strong> {metadata['publish_date']}</span>
    </div>
    <div class="content">
        {content}
    </div>
    <div class="footer">
        <p>原文链接: {self.url}</p>
        <p>转换时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
</body>
</html>"""
        return html_template

    def convert_to_pdf(self, output_file):
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

        print("Generating PDF HTML...")
        pdf_html = self.generate_pdf_html(metadata, content)

        print("Converting to PDF...")
        try:
            # Try using weasyprint
            try:
                from weasyprint import HTML
                HTML(string=pdf_html).write_pdf(output_file)
                print(f"\nSuccessfully converted to PDF: {output_file}")
                return True
            except ImportError:
                print("\nWeasyPrint not found. Trying pdfkit...")

                # Try using pdfkit
                try:
                    import pdfkit
                    pdfkit.from_string(pdf_html, output_file)
                    print(f"\nSuccessfully converted to PDF: {output_file}")
                    return True
                except ImportError:
                    print("\npdfkit not found. Saving as HTML instead...")
                    html_file = output_file.replace('.pdf', '.html')
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(pdf_html)
                    print(f"\nSaved as HTML: {html_file}")
                    print("\nTo convert to PDF, install one of the following:")
                    print("  - WeasyPrint: pip install weasyprint")
                    print("  - pdfkit: pip install pdfkit (also requires wkhtmltopdf)")
                    return True

        except Exception as e:
            print(f"Error converting to PDF: {e}", file=sys.stderr)
            return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python wechat_to_pdf.py <wechat_article_url> [output_file.pdf]")
        print("Example: python wechat_to_pdf.py https://mp.weixin.qq.com/s/xxxxx article.pdf")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "wechat_article.pdf"

    # Ensure output file has .pdf extension
    if not output_file.endswith('.pdf'):
        output_file += '.pdf'

    # Validate URL
    if 'mp.weixin.qq.com' not in url:
        print("Error: Please provide a valid WeChat article URL (mp.weixin.qq.com)")
        sys.exit(1)

    converter = WeChatArticleToPDF(url)
    success = converter.convert_to_pdf(output_file)

    if not success:
        print("Conversion failed!")
        sys.exit(1)


if __name__ == '__main__':
    main()
