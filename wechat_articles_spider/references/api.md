# API Reference

## Core Classes

### PublicAccountsWeb

Web-based interface for scraping WeChat public account articles.

#### Constructor

```python
from wechatarticles import PublicAccountsWeb

paw = PublicAccountsWeb(cookie=cookie, token=token)
```

**Parameters:**
- `cookie` (str): Official account cookie from mp.weixin.qq.com
- `token` (str): Authentication token from official account session

#### Methods

##### get_urls()

Retrieve article URLs with pagination support.

```python
article_data = paw.get_urls(
    nickname,
    biz=biz,
    begin="0",
    count="5"
)
```

**Parameters:**
- `nickname` (str): Target public account name
- `biz` (str): Business account identifier
- `begin` (str): Starting index for pagination (default: "0")
- `count` (str): Number of articles to retrieve (default: "5")

**Returns:**
- Dictionary containing article data including URLs, titles, and metadata

**Example:**
```python
articles = paw.get_urls("TechAccount", biz="MzAxMjQ...", begin="0", count="10")
for article in articles:
    print(article['url'], article['title'])
```

##### articles_nums()

Get total article count for a public account.

```python
total = paw.articles_nums(nickname)
```

**Parameters:**
- `nickname` (str): Public account name

**Returns:**
- Integer representing total published articles

**Example:**
```python
count = paw.articles_nums("TechAccount")
print(f"Total articles: {count}")
```

##### official_info()

Retrieve public account metadata and information.

```python
info = paw.official_info()
```

**Returns:**
- Dictionary with account details (name, description, verification status, etc.)

---

### ArticlesInfo

Extract engagement metrics and interaction data from articles.

#### Constructor

```python
from wechatarticles import ArticlesInfo

ai = ArticlesInfo(appmsg_token, cookie)
```

**Parameters:**
- `appmsg_token` (str): Token from WeChat PC client
- `cookie` (str): Cookie from WeChat PC client session

#### Methods

##### read_like_nums()

Get read count, likes, and historical like data for an article.

```python
read_num, like_num, old_like_num = ai.read_like_nums(article_url)
```

**Parameters:**
- `article_url` (str): Full WeChat article URL (https://mp.weixin.qq.com/s/...)

**Returns:**
- Tuple of three integers:
  - `read_num`: Current read/view count
  - `like_num`: Current like count
  - `old_like_num`: Previous like count

**Example:**
```python
url = "https://mp.weixin.qq.com/s/abc123..."
reads, likes, old_likes = ai.read_like_nums(url)
print(f"Reads: {reads}, Likes: {likes}, Previous Likes: {old_likes}")
```

##### comments()

Retrieve all comments for an article.

```python
comment_data = ai.comments(article_url)
```

**Parameters:**
- `article_url` (str): Full WeChat article URL

**Returns:**
- Dictionary or list containing comment information:
  - Comment text
  - Commenter information
  - Timestamps
  - Reply threads

**Example:**
```python
comments = ai.comments(url)
for comment in comments:
    print(f"{comment['user']}: {comment['text']}")
```

---

### Url2Html

Convert WeChat articles to offline HTML format with image preservation.

#### Constructor

```python
from wechatarticles import Url2Html

uh = Url2Html()
```

**No parameters required.**

#### Methods

##### run()

Download and convert article to HTML.

```python
result = uh.run(url, mode=4)
```

**Parameters:**
- `url` (str): WeChat article URL
- `mode` (int): Conversion mode (default: 4)
  - Different modes control image handling and HTML structure

**Returns:**
- Result dictionary with status and file paths

**Important Prerequisites:**
Before calling `run()`, create the following directory structure:
```
account_name/
  └── imgs/
```

**Example:**
```python
import os

# Setup directory structure
os.makedirs("MyAccount/imgs", exist_ok=True)

# Download article
uh = Url2Html()
result = uh.run("https://mp.weixin.qq.com/s/xyz...", mode=4)
print(result)
```

---

## Utility Functions

### get_history_urls()

Bulk collection of article URLs using historical article access.

```python
from wechatarticles.utils import get_history_urls

urls = get_history_urls(biz, uin, key, offset=0)
```

**Parameters:**
- `biz` (str): Public account business identifier
- `uin` (str): Your WeChat user ID
- `key` (str): Session authentication key (requires renewal)
- `offset` (int): Pagination offset (default: 0)

**Returns:**
- List of article URLs

**Usage Pattern:**
```python
# Collect all articles with pagination
all_urls = []
offset = 0
while True:
    urls = get_history_urls(biz, uin, key, offset)
    if not urls:
        break
    all_urls.extend(urls)
    offset += len(urls)
    time.sleep(random.uniform(5, 10))  # Rate limiting!
```

### verify_url()

Validate WeChat article URLs.

```python
from wechatarticles.utils import verify_url

is_valid = verify_url(url)
```

**Parameters:**
- `url` (str): URL to validate

**Returns:**
- Boolean indicating if URL is a valid WeChat article link

---

## Complete Workflow Example

### Collecting and Analyzing Articles

```python
import time
import random
from wechatarticles import PublicAccountsWeb, ArticlesInfo

# Step 1: Setup credentials
official_cookie = "your_official_cookie"
token = "your_token"
appmsg_token = "your_appmsg_token"
wechat_cookie = "your_wechat_cookie"

# Step 2: Initialize classes
paw = PublicAccountsWeb(cookie=official_cookie, token=token)
ai = ArticlesInfo(appmsg_token, wechat_cookie)

# Step 3: Get article URLs
nickname = "TechBlog"
biz = "MzAxMjQ..."
articles = paw.get_urls(nickname, biz=biz, begin="0", count="20")

# Step 4: Analyze each article
results = []
for article in articles:
    url = article['url']

    # Get engagement metrics
    reads, likes, old_likes = ai.read_like_nums(url)

    # Get comments
    comments = ai.comments(url)

    results.append({
        'title': article['title'],
        'url': url,
        'reads': reads,
        'likes': likes,
        'comment_count': len(comments) if comments else 0
    })

    # Rate limiting (important!)
    time.sleep(random.uniform(5, 10))

# Step 5: Process results
for result in results:
    print(f"{result['title']}: {result['reads']} reads, {result['likes']} likes")
```

## Rate Limiting Best Practices

⚠️ **Critical**: Always implement rate limiting to avoid being blocked.

```python
import time
import random

# Between article requests
time.sleep(random.uniform(5, 10))  # 5-10 seconds

# Between page requests
time.sleep(random.uniform(10, 15))  # 10-15 seconds

# Longer delays for bulk operations
time.sleep(random.uniform(15, 30))  # 15-30 seconds
```

## Error Handling

```python
try:
    reads, likes, old_likes = ai.read_like_nums(url)
except Exception as e:
    print(f"Error fetching metrics: {e}")
    # Handle authentication expiration
    # Re-extract credentials if needed
```

## Common Return Types

### Article Data Dictionary
```python
{
    'url': 'https://mp.weixin.qq.com/s/...',
    'title': 'Article Title',
    'date': '2025-01-15',
    'author': 'Author Name',
    # ... additional fields
}
```

### Comment Data Structure
```python
{
    'user': 'Username',
    'text': 'Comment text',
    'timestamp': 1234567890,
    'replies': []
}
```

## Next Steps

- See [Usage Examples](examples.md) for complete working code
- Review [Authentication Guide](authentication.md) for credential setup
- Check [Getting Started](getting_started.md) for basic patterns
