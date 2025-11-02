# WeChat Articles Spider

## When to Use This Skill

Use this skill when you need to:
- **Scrape WeChat Official Accounts**: Collect article URLs from public accounts (公众号)
- **Track Engagement Metrics**: Extract read counts, likes, and comments from articles
- **Archive Content**: Download WeChat articles as offline HTML with images preserved
- **Historical Data Analysis**: Collect 500+ historical articles from an account
- **Monitor Content Performance**: Track article performance metrics over time
- **Research Projects**: Analyze WeChat content trends and engagement patterns

**Specific Triggers:**
- User mentions "WeChat articles," "公众号," or "WeChat Official Account"
- Need to scrape, download, or analyze WeChat content
- Extracting engagement data (reads, likes, comments) from WeChat
- Building WeChat content analysis or archiving tools

## Quick Reference

### Installation

```bash
pip install wechatarticles
```

**Requirements:** Python 3.6.2+

### Example 1: Collect Article URLs (5 lines)

```python
from wechatarticles import PublicAccountsWeb

paw = PublicAccountsWeb(cookie=official_cookie, token=token)
articles = paw.get_urls("AccountName", biz="biz_id", begin="0", count="5")
print(articles)
```

Collects the first 5 article URLs from a WeChat public account. Requires official account credentials.

### Example 2: Get Read Counts and Likes (4 lines)

```python
from wechatarticles import ArticlesInfo

ai = ArticlesInfo(appmsg_token, wechat_cookie)
reads, likes, old_likes = ai.read_like_nums(article_url)
print(f"Reads: {reads}, Likes: {likes}")
```

Extracts engagement metrics for a specific article. Requires WeChat PC client credentials.

### Example 3: Get Article Comments (3 lines)

```python
ai = ArticlesInfo(appmsg_token, wechat_cookie)
comments = ai.comments(article_url)
print(f"Total comments: {len(comments)}")
```

Retrieves all comments for an article.

### Example 4: Download Article as HTML (5 lines)

```python
import os
from wechatarticles import Url2Html

os.makedirs("MyAccount/imgs", exist_ok=True)
uh = Url2Html()
result = uh.run(article_url, mode=4)
```

Downloads article as offline HTML with images preserved. Creates directory structure automatically.

### Example 5: Bulk Historical Collection (4 lines)

```python
from wechatarticles.utils import get_history_urls

# Get 500+ articles from history
urls = get_history_urls(biz, uin, key, offset=0)
print(f"Found {len(urls)} articles")
```

Rapidly collects large numbers of historical article URLs.

### Example 6: Complete Analysis Workflow (15 lines)

```python
import time, random
from wechatarticles import PublicAccountsWeb, ArticlesInfo

paw = PublicAccountsWeb(cookie=official_cookie, token=token)
ai = ArticlesInfo(appmsg_token, wechat_cookie)

articles = paw.get_urls("AccountName", biz="biz_id", begin="0", count="10")

for article in articles:
    reads, likes, old_likes = ai.read_like_nums(article['url'])
    comments = ai.comments(article['url'])

    print(f"{article['title']}: {reads} reads, {likes} likes, {len(comments)} comments")

    # Rate limiting (critical!)
    time.sleep(random.uniform(5, 10))
```

Complete workflow: fetch articles, extract metrics, and analyze engagement. **Always include rate limiting!**

### Example 7: Safe Metrics with Retry Logic (8 lines)

```python
def safe_fetch_metrics(ai, url, max_retries=3):
    for attempt in range(max_retries):
        try:
            return ai.read_like_nums(url)
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(5)
            else:
                return None, None, None
```

Robust error handling with automatic retry for failed requests.

### Example 8: Pagination Pattern (7 lines)

```python
all_articles = []
begin, count = 0, 10

while True:
    batch = paw.get_urls(nickname, biz=biz, begin=str(begin), count=str(count))
    if not batch: break
    all_articles.extend(batch)
    begin += count
```

Fetch all articles using pagination.

### Example 9: Get Account Total (2 lines)

```python
total = paw.articles_nums("AccountName")
print(f"Total articles: {total}")
```

Quick way to get total article count for an account.

### Example 10: Rate Limiting Pattern (3 lines)

```python
import time, random

time.sleep(random.uniform(5, 10))  # 5-10 seconds between requests
```

**Critical**: Always use random delays (5-10 seconds) between article requests to avoid being blocked.

## Key Concepts

### Authentication Requirements

The library requires **manual credential extraction** - no automated login exists.

**Two Credential Sets:**

1. **Official Account Credentials** (for URL collection)
   - `official_cookie`: From mp.weixin.qq.com (F12 → Network → Cookie)
   - `token`: From official account session
   - Used by: `PublicAccountsWeb`

2. **WeChat Client Credentials** (for engagement metrics)
   - `appmsg_token`: From WeChat PC client (via Fiddler/packet capture)
   - `wechat_cookie`: From PC client session
   - Used by: `ArticlesInfo`, historical collection

**Credential Lifespan:**
- Cookies: 24-48 hours
- Tokens: 1-24 hours
- Must be refreshed when expired

### Core Classes

| Class | Purpose | Key Methods |
|-------|---------|-------------|
| `PublicAccountsWeb` | Web-based scraping | `get_urls()`, `articles_nums()`, `official_info()` |
| `ArticlesInfo` | Engagement metrics | `read_like_nums()`, `comments()` |
| `Url2Html` | HTML download | `run()` |
| `get_history_urls()` | Bulk collection | Returns list of URLs |

### Rate Limiting (Critical!)

⚠️ **Always implement rate limiting or you will be blocked:**

- **Between articles**: 5-10 seconds (random)
- **Between pages**: 10-15 seconds
- **Between batches**: 30-60 seconds

```python
time.sleep(random.uniform(5, 10))
```

### Common Parameters

- `nickname`: Public account display name
- `biz`: Business ID (found in article URLs: `?__biz=XXXXX`)
- `uin`: Your WeChat user ID
- `key`: Session key (expires frequently)
- `begin`/`count`: Pagination parameters (**must be strings**, not integers)

## Reference Documentation

### For Beginners

**Start Here:**
1. **[Getting Started](references/getting_started.md)** - Installation, prerequisites, quick start examples
2. **[Authentication Guide](references/authentication.md)** - Step-by-step credential extraction (F12, Fiddler)

**Contains:** Installation, two main approaches, basic examples, important constraints

### For API Users

**API Documentation:**
1. **[API Reference](references/api.md)** - Complete class and method documentation
   - `PublicAccountsWeb`: get_urls(), articles_nums(), official_info()
   - `ArticlesInfo`: read_like_nums(), comments()
   - `Url2Html`: run()
   - Utility functions: get_history_urls(), verify_url()

**Contains:** Parameters, return types, detailed examples, error handling

### For Implementation

**Working Examples:**
1. **[Usage Examples](references/examples.md)** - 5 complete working examples
   - Example 1: Basic URL collection
   - Example 2: Extract engagement metrics
   - Example 3: Bulk historical collection (with Excel export)
   - Example 4: Download as HTML
   - Example 5: Complete analysis pipeline (WeChatAnalyzer class)

**Contains:** Full code, output examples, common patterns (pagination, error recovery, batch processing)

### Complete Index

**[Reference Index](references/index.md)** - Overview of all documentation

## Working with This Skill

### For Beginners (First Time Users)

**Workflow:**
1. Read [Getting Started](references/getting_started.md) for installation
2. Follow [Authentication Guide](references/authentication.md) to extract credentials:
   - Open mp.weixin.qq.com → F12 → Network → Copy Cookie & Token
   - Install Fiddler → Login to WeChat PC → Capture `/mp/getappmsgext` → Extract appmsg_token
3. Try Quick Reference Example 1 (collect URLs)
4. Try Quick Reference Example 2 (get metrics)

**Key Tips:**
- Start with small batches (`count="5"`)
- Always use rate limiting (`time.sleep(random.uniform(5, 10))`)
- Credentials expire - refresh when you see auth errors

### For Intermediate Users (Building Tools)

**Workflow:**
1. Review [API Reference](references/api.md) for all available methods
2. Study [Usage Examples](references/examples.md) for complete workflows
3. Implement error handling (see Example 7: Safe Metrics with Retry)
4. Use pagination pattern (Example 8) for large-scale collection
5. Add logging and data persistence (JSON/Excel export)

**Key Tips:**
- Use try-except blocks for robust error handling
- Implement automatic credential refresh logic
- Log all operations for debugging
- Test with `count="5"` before scaling up

### For Advanced Users (Production Systems)

**Workflow:**
1. Study Example 5 in [Usage Examples](references/examples.md) (WeChatAnalyzer class)
2. Implement batch processing with breaks (Pattern 3 in examples.md)
3. Add monitoring and alerting for auth expiration
4. Build credential rotation system
5. Implement data warehousing (database storage)

**Key Tips:**
- Never hardcode credentials (use environment variables)
- Implement exponential backoff for rate limiting
- Monitor for API changes or blocks
- Build health checks and automatic recovery

## Important Constraints

1. **No Automated Login**: Credentials must be manually extracted via browser DevTools or packet capture
2. **Manual Configuration**: Each public account requires fresh credentials
3. **Rate Limiting Essential**: 5-10 seconds between requests or you'll be blocked
4. **Token Expiration**: Credentials expire (hours to days), must be refreshed
5. **Learning/Research Tool**: Not production-ready without significant modification
6. **Terms of Service**: Always respect WeChat's terms and rate limits

## Troubleshooting

### Authentication Errors
- **Symptom**: Empty responses, 403 errors
- **Solution**: Extract fresh credentials (tokens expire quickly)

### Rate Limiting / Blocks
- **Symptom**: Connection refused, slow responses
- **Solution**: Increase delays, use random intervals, take longer breaks

### Empty Responses
- **Symptom**: No data returned
- **Solution**: Verify credentials, check URL patterns, ensure account is public

### Missing Parameters
- **Symptom**: KeyError or parameter not found
- **Solution**: Verify all required params extracted correctly (`biz`, `uin`, `key`)

## Additional Resources

- **GitHub Repository**: https://github.com/wnma3mz/wechat_articles_spider
- **PyPI Package**: https://pypi.org/project/wechatarticles/
- **Python Version**: 3.6.2+ required

---

**Note**: This library is designed for learning and research purposes. Always respect WeChat's terms of service and implement appropriate rate limiting when scraping content.
