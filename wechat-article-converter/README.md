# WeChat Article Converter Skill

A Claude Code skill that converts WeChat public account articles to Markdown, PDF, or HTML format.

## Features

- ✅ Convert single WeChat articles to Markdown, PDF, or HTML
- ✅ Batch process multiple articles at once
- ✅ Preserve article metadata (title, author, publish date)
- ✅ Embed images as Base64 (no external dependencies)
- ✅ Maintain original formatting and styles
- ✅ Responsive HTML output with mobile support
- ✅ Support for `mp.weixin.qq.com` articles

## Installation

1. Install the skill in Claude Code (place in `.claude/skills/` directory)

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

For PDF support (optional):
```bash
# Option 1: WeasyPrint (recommended)
pip install weasyprint

# Option 2: pdfkit (requires wkhtmltopdf)
pip install pdfkit
```

## Quick Start

### Convert a Single Article

**To Markdown:**
```bash
python scripts/wechat_to_markdown.py "https://mp.weixin.qq.com/s/xxxxx" output.md
```

**To PDF:**
```bash
python scripts/wechat_to_pdf.py "https://mp.weixin.qq.com/s/xxxxx" output.pdf
```

**To HTML:**
```bash
python scripts/wechat_to_html.py "https://mp.weixin.qq.com/s/xxxxx" output.html
```

### Batch Convert Multiple Articles

1. Create a text file `urls.txt` with one URL per line:
```
https://mp.weixin.qq.com/s/article1
https://mp.weixin.qq.com/s/article2
https://mp.weixin.qq.com/s/article3
```

2. Run batch conversion:
```bash
# Convert to all formats (Markdown, PDF, and HTML)
python scripts/batch_converter.py urls.txt --format all --output ./articles

# Convert to Markdown only
python scripts/batch_converter.py urls.txt --format markdown --output ./markdown

# Convert to PDF only
python scripts/batch_converter.py urls.txt --format pdf --output ./pdfs

# Convert to HTML only
python scripts/batch_converter.py urls.txt --format html --output ./html
```

## Using with Claude Code

Once installed, you can ask Claude:

> "Convert this WeChat article to Markdown: https://mp.weixin.qq.com/s/xxxxx"

> "Convert this WeChat article to HTML"

> "Convert these 5 WeChat articles to PDF"

> "Batch convert all WeChat articles from urls.txt to all formats"

Claude will automatically use this skill and execute the appropriate conversion scripts.

## Output Format

### Markdown Output
- Clean, readable Markdown with preserved formatting
- Metadata header (title, author, date)
- Base64-embedded images
- Links and text formatting preserved

### PDF Output
- Styled layout matching WeChat's design
- Embedded images
- Metadata and source information
- Print-ready format

### HTML Output
- Standalone HTML document
- Responsive design with mobile support
- Embedded Base64 images
- Clean, styled layout
- Print-friendly CSS

## Advanced Options

### Batch Converter Options

```bash
python scripts/batch_converter.py [input_file] [options]

Options:
  --urls URL1 URL2 ...    Provide URLs directly (instead of file)
  --format FORMAT         Output format: markdown, pdf, html, or all (default: all)
  --output DIR            Output directory (default: ./output)
  --delay SECONDS         Delay between requests (default: 2.0)
```

### Examples

```bash
# Convert with custom delay
python scripts/batch_converter.py urls.txt --delay 3.0

# Convert URLs directly without file to all formats
python scripts/batch_converter.py --urls "url1" "url2" "url3" --format all

# Convert to HTML only
python scripts/batch_converter.py --urls "url1" "url2" --format html

# Organize output by format
python scripts/batch_converter.py urls.txt --format markdown --output ./markdown_articles
```

## Troubleshooting

**Missing dependencies:**
```bash
pip install -r requirements.txt
```

**PDF conversion not working:**
Install a PDF library:
```bash
pip install weasyprint
```

**Images not displaying:**
- Check your internet connection
- The script will fallback to image URLs if Base64 embedding fails

**Rate limiting issues:**
- Increase delay in batch processing: `--delay 5.0`
- Process smaller batches

## Requirements

- Python 3.7+
- `requests` library (required)
- `weasyprint` or `pdfkit` (optional, for PDF conversion)

## License

This skill is part of the Claude Code skill ecosystem.

## Support

For issues or questions, please refer to the Claude Code documentation or create an issue in the appropriate repository.
