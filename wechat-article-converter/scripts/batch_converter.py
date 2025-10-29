#!/usr/bin/env python3
"""
Batch WeChat Article Converter

This script processes multiple WeChat article URLs and converts them to Markdown, PDF, or HTML.
Supports all three formats and handles multiple articles efficiently.
"""

import sys
import os
from pathlib import Path
import argparse
from datetime import datetime
import time


def main():
    parser = argparse.ArgumentParser(
        description='Batch convert WeChat articles to Markdown, PDF, or HTML',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert URLs from a file to Markdown
  python batch_converter.py urls.txt --format markdown --output ./articles

  # Convert URLs to PDF
  python batch_converter.py urls.txt --format pdf --output ./pdfs

  # Convert URLs to HTML
  python batch_converter.py urls.txt --format html --output ./html

  # Convert directly provided URLs to all formats
  python batch_converter.py --urls "url1" "url2" "url3" --format all

  # URLs file format (one URL per line):
  https://mp.weixin.qq.com/s/xxxxx
  https://mp.weixin.qq.com/s/yyyyy
  https://mp.weixin.qq.com/s/zzzzz
        """
    )

    parser.add_argument(
        'input_file',
        nargs='?',
        help='File containing WeChat article URLs (one per line)'
    )
    parser.add_argument(
        '--urls',
        nargs='+',
        help='WeChat article URLs to convert (space-separated)'
    )
    parser.add_argument(
        '--format',
        choices=['markdown', 'pdf', 'html', 'all'],
        default='all',
        help='Output format (default: all)'
    )
    parser.add_argument(
        '--output',
        '-o',
        default='./output',
        help='Output directory (default: ./output)'
    )
    parser.add_argument(
        '--delay',
        type=float,
        default=2.0,
        help='Delay between requests in seconds (default: 2.0)'
    )

    args = parser.parse_args()

    # Get URLs from file or command line
    urls = []
    if args.input_file:
        if not os.path.exists(args.input_file):
            print(f"Error: Input file not found: {args.input_file}")
            sys.exit(1)
        with open(args.input_file, 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip() and 'mp.weixin.qq.com' in line]
    elif args.urls:
        urls = args.urls
    else:
        parser.print_help()
        sys.exit(1)

    if not urls:
        print("Error: No valid WeChat article URLs found")
        sys.exit(1)

    # Validate URLs
    valid_urls = [url for url in urls if 'mp.weixin.qq.com' in url]
    if len(valid_urls) < len(urls):
        print(f"Warning: Filtered out {len(urls) - len(valid_urls)} invalid URLs")

    urls = valid_urls

    # Create output directory
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get script directory
    script_dir = Path(__file__).parent

    print(f"\n{'='*80}")
    print(f"Batch WeChat Article Converter")
    print(f"{'='*80}")
    print(f"Total articles to convert: {len(urls)}")
    print(f"Output format: {args.format}")
    print(f"Output directory: {output_dir.absolute()}")
    print(f"Delay between requests: {args.delay}s")
    print(f"{'='*80}\n")

    # Track results
    results = {
        'success': [],
        'failed': []
    }

    # Process each URL
    for idx, url in enumerate(urls, 1):
        print(f"\n[{idx}/{len(urls)}] Processing: {url}")

        # Generate output filename based on index
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        base_name = f"article_{idx:03d}_{timestamp}"

        success = True

        # Convert to Markdown
        if args.format in ['markdown', 'all']:
            md_file = output_dir / f"{base_name}.md"
            print(f"  → Converting to Markdown...")

            import subprocess
            try:
                result = subprocess.run(
                    ['python', str(script_dir / 'wechat_to_markdown.py'), url, str(md_file)],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                if result.returncode == 0:
                    print(f"  ✓ Saved: {md_file}")
                else:
                    print(f"  ✗ Failed: {result.stderr}")
                    success = False
            except subprocess.TimeoutExpired:
                print(f"  ✗ Failed: Timeout")
                success = False
            except Exception as e:
                print(f"  ✗ Failed: {e}")
                success = False

        # Convert to PDF
        if args.format in ['pdf', 'all']:
            pdf_file = output_dir / f"{base_name}.pdf"
            print(f"  → Converting to PDF...")

            import subprocess
            try:
                result = subprocess.run(
                    ['python', str(script_dir / 'wechat_to_pdf.py'), url, str(pdf_file)],
                    capture_output=True,
                    text=True,
                    timeout=90
                )
                if result.returncode == 0:
                    print(f"  ✓ Saved: {pdf_file}")
                else:
                    print(f"  ✗ Failed: {result.stderr}")
                    success = False
            except subprocess.TimeoutExpired:
                print(f"  ✗ Failed: Timeout")
                success = False
            except Exception as e:
                print(f"  ✗ Failed: {e}")
                success = False

        # Convert to HTML
        if args.format in ['html', 'all']:
            html_file = output_dir / f"{base_name}.html"
            print(f"  → Converting to HTML...")

            import subprocess
            try:
                result = subprocess.run(
                    ['python', str(script_dir / 'wechat_to_html.py'), url, str(html_file)],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                if result.returncode == 0:
                    print(f"  ✓ Saved: {html_file}")
                else:
                    print(f"  ✗ Failed: {result.stderr}")
                    success = False
            except subprocess.TimeoutExpired:
                print(f"  ✗ Failed: Timeout")
                success = False
            except Exception as e:
                print(f"  ✗ Failed: {e}")
                success = False

        # Record result
        if success:
            results['success'].append(url)
        else:
            results['failed'].append(url)

        # Delay before next request (except for last item)
        if idx < len(urls):
            time.sleep(args.delay)

    # Print summary
    print(f"\n{'='*80}")
    print(f"Conversion Summary")
    print(f"{'='*80}")
    print(f"Total processed: {len(urls)}")
    print(f"Successful: {len(results['success'])}")
    print(f"Failed: {len(results['failed'])}")

    if results['failed']:
        print(f"\nFailed URLs:")
        for url in results['failed']:
            print(f"  - {url}")

    print(f"\nAll files saved to: {output_dir.absolute()}")
    print(f"{'='*80}\n")

    # Exit with error code if any conversions failed
    sys.exit(0 if not results['failed'] else 1)


if __name__ == '__main__':
    main()
