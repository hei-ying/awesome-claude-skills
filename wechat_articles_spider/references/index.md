# WeChat Articles Spider - Reference Index

## Overview
This skill provides comprehensive documentation for the wechat_articles_spider library, a Python tool for scraping WeChat Official Account articles and extracting engagement metrics.

## Reference Categories

### Getting Started
- [Getting Started Guide](getting_started.md) - Installation, prerequisites, and quick start

### Authentication
- [Authentication Guide](authentication.md) - How to obtain cookies, tokens, and required credentials

### API Reference
- [API Documentation](api.md) - Complete API reference for all classes and methods

### Examples
- [Usage Examples](examples.md) - Complete working examples for common use cases

## Quick Links

### Core Classes
- `PublicAccountsWeb` - Web-based article scraping
- `ArticlesInfo` - Engagement metrics extraction
- `Url2Html` - Offline HTML download
- `get_history_urls()` - Bulk URL collection

### Key Concepts
- **Rate Limiting**: 5-10 seconds between article requests recommended
- **Authentication**: Requires manual credential extraction from WeChat
- **Python Version**: Requires Python 3.6.2+

## Use Cases

1. **Article Collection**: Gather URLs from WeChat public accounts
2. **Engagement Analysis**: Track read counts, likes, and comments
3. **Content Archiving**: Download articles as offline HTML
4. **Historical Data**: Bulk extraction via history features

## Important Notes

- Manual parameter configuration required per account
- No automated WeChat login capability
- Suitable for learning purposes, not production deployment
- Rate limiting essential to prevent blocking
