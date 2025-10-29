---
name: wechat-article-converter
description: Convert WeChat articles (mp.weixin.qq.com) to Markdown, PDF, or HTML format with full content preservation including metadata, text, images (embedded as Base64), and formatting. Supports single article conversion or batch processing of multiple URLs.
---

# WeChat Article Converter

Convert WeChat public account articles to well-formatted Markdown, PDF, or HTML documents.

## Purpose

This skill enables conversion of WeChat articles (from mp.weixin.qq.com) into portable, readable formats. The converter preserves:
- Article metadata (title, author, publish date)
- Full text content with proper formatting
- All images embedded as Base64 data URIs
- Original styling and layout (for PDF output)

## When to Use This Skill

Use this skill when users request:
- Converting WeChat article links to Markdown, PDF, or HTML
- Downloading or saving WeChat articles
- Extracting content from mp.weixin.qq.com URLs
- Batch processing multiple WeChat articles
- Archiving WeChat public account content

## Key Capabilities

### Single Article Conversion

Convert individual WeChat articles to Markdown, PDF, or HTML format:

**For Markdown conversion:**
```bash
python scripts/wechat_to_markdown.py <article_url> [output_file.md]
```

**For PDF conversion:**
```bash
python scripts/wechat_to_pdf.py <article_url> [output_file.pdf]
```

**For HTML conversion:**
```bash
python scripts/wechat_to_html.py <article_url> [output_file.html]
```

### Batch Processing

Convert multiple WeChat articles at once:

```bash
python scripts/batch_converter.py urls.txt --format all --output ./articles
```

The batch converter supports:
- Reading URLs from a text file (one URL per line)
- Direct URL input via command line arguments
- Markdown, PDF, HTML, or all output formats
- Configurable delay between requests
- Progress tracking and error reporting

## Usage Instructions

### Prerequisites

Before using this skill, ensure Python dependencies are installed:

```bash
pip install -r requirements.txt
```

**Note:** PDF conversion requires either `weasyprint` (recommended) or `pdfkit` (requires additional wkhtmltopdf installation). If neither is available, the script will save as HTML instead.

### Converting a Single Article

When a user provides a WeChat article URL, follow these steps:

1. **Validate the URL** - Ensure it's from mp.weixin.qq.com
2. **Determine output format** - Ask if Markdown, PDF, HTML, or multiple formats are needed
3. **Choose appropriate script:**
   - For Markdown: Use `scripts/wechat_to_markdown.py`
   - For PDF: Use `scripts/wechat_to_pdf.py`
   - For HTML: Use `scripts/wechat_to_html.py`
4. **Execute the conversion** with the URL and desired output filename
5. **Verify the output** and inform the user of the result location

**Example workflow:**
```bash
# Convert to Markdown
python scripts/wechat_to_markdown.py "https://mp.weixin.qq.com/s/xxxxx" article.md

# Convert to PDF
python scripts/wechat_to_pdf.py "https://mp.weixin.qq.com/s/xxxxx" article.pdf

# Convert to HTML
python scripts/wechat_to_html.py "https://mp.weixin.qq.com/s/xxxxx" article.html
```

### Converting Multiple Articles

For batch processing:

1. **Prepare input** - Create a text file with URLs (one per line) or use command-line arguments
2. **Configure output** - Specify format (markdown, pdf, html, or all) and output directory
3. **Execute batch conversion** using `scripts/batch_converter.py`
4. **Review results** - Check the summary for successful and failed conversions

**Example workflows:**

```bash
# From a file with URLs
python scripts/batch_converter.py urls.txt --format markdown --output ./articles

# Convert to HTML
python scripts/batch_converter.py urls.txt --format html --output ./html

# Direct URL input with all formats
python scripts/batch_converter.py --urls "url1" "url2" "url3" --format all --output ./output

# With custom delay between requests
python scripts/batch_converter.py urls.txt --format pdf --delay 3.0
```

### Output Details

**Markdown output includes:**
- Article title as H1 heading
- Metadata block (author, publish date, source URL)
- Full article content with preserved formatting
- Images embedded as Base64 data URIs
- Conversion timestamp footer

**PDF output includes:**
- Styled HTML layout matching WeChat's visual design
- Embedded Base64 images
- Metadata header
- Source URL and conversion timestamp footer

**HTML output includes:**
- Clean, standalone HTML document
- Responsive design with mobile support
- Embedded Base64 images
- Styled layout with proper typography
- Metadata header and footer
- Print-friendly CSS

### Error Handling

Common issues and solutions:

1. **Network errors** - Retry with better network connection
2. **Invalid URLs** - Verify the URL is from mp.weixin.qq.com
3. **Image download failures** - Images may fall back to original URLs if Base64 embedding fails
4. **PDF conversion unavailable** - Install weasyprint or pdfkit, or accept HTML output as alternative

### Best Practices

1. **Respect rate limits** - Use appropriate delays in batch processing (default: 2 seconds)
2. **Check output** - Verify converted files contain expected content
3. **Organize output** - Use descriptive filenames or output directories
4. **Handle failures** - Review failed conversions and retry if needed

## Script Reference

### wechat_to_markdown.py

Converts a single WeChat article to Markdown format.

**Parameters:**
- `article_url` (required) - WeChat article URL
- `output_file` (optional) - Output filename (prints to stdout if omitted)

**Features:**
- Extracts metadata (title, author, date)
- Converts HTML to clean Markdown
- Downloads and embeds images as Base64
- Preserves links, formatting, lists, and blockquotes

### wechat_to_pdf.py

Converts a single WeChat article to PDF format.

**Parameters:**
- `article_url` (required) - WeChat article URL
- `output_file` (optional) - Output filename (defaults to wechat_article.pdf)

**Features:**
- Preserves original styling and layout
- Embeds images as Base64 within PDF
- Includes metadata and source attribution
- Requires weasyprint or pdfkit library

### wechat_to_html.py

Converts a single WeChat article to standalone HTML format.

**Parameters:**
- `article_url` (required) - WeChat article URL
- `output_file` (optional) - Output filename (defaults to wechat_article.html)

**Features:**
- Generates clean, standalone HTML document
- Responsive design with mobile support
- Embeds images as Base64
- Styled layout matching WeChat's design
- Print-friendly CSS included

### batch_converter.py

Processes multiple WeChat articles in batch mode.

**Parameters:**
- `input_file` (optional) - Text file with URLs (one per line)
- `--urls` (optional) - Space-separated URLs
- `--format` (optional) - Output format: markdown, pdf, html, or all (default: all)
- `--output` (optional) - Output directory (default: ./output)
- `--delay` (optional) - Delay between requests in seconds (default: 2.0)

**Features:**
- Batch processing with progress tracking
- Flexible input methods (file or command-line)
- Configurable output format (supports all three formats)
- Error tracking and summary report
- Rate limiting with configurable delays

## Dependencies

See `requirements.txt` for the complete list. Key dependencies:
- `requests` - HTTP requests and article fetching (required)
- `weasyprint` - High-quality PDF generation (optional, recommended)
- `pdfkit` - Alternative PDF generation (optional, requires wkhtmltopdf)

## Troubleshooting

**"Module not found" errors:**
Install dependencies: `pip install -r requirements.txt`

**PDF conversion shows warning:**
Install a PDF library: `pip install weasyprint`

**Images not loading:**
Check network connectivity. Script will preserve original URLs as fallback.

**Batch conversion timing out:**
Increase delay between requests: `--delay 5.0`
