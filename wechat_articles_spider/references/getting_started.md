# Getting Started with WeChat Articles Spider

## Installation

Install via pip:

```bash
pip install wechatarticles
```

## Prerequisites

- **Python Version**: Python 3.6.2 or higher
- **WeChat Account**: Personal WeChat account with access to target public accounts
- **Official Account Access**: Login access to mp.weixin.qq.com (for some features)
- **Browser**: Chrome or Firefox with Developer Tools

## Quick Start

### 1. Basic URL Collection

The simplest way to start is collecting article URLs from a public account:

```python
from wechatarticles import PublicAccountsWeb

# Your credentials (see Authentication guide)
cookie = "your_official_cookie"
token = "your_token"
nickname = "target_account_name"
biz = "account_biz_id"

# Initialize and fetch URLs
paw = PublicAccountsWeb(cookie=cookie, token=token)
article_data = paw.get_urls(nickname, biz=biz, begin="0", count="5")

print(article_data)
```

### 2. Get Engagement Metrics

Extract read counts and likes from articles:

```python
from wechatarticles import ArticlesInfo

# Your WeChat PC client credentials
appmsg_token = "your_appmsg_token"
cookie = "your_wechat_cookie"
article_url = "https://mp.weixin.qq.com/s/..."

# Initialize and fetch metrics
test = ArticlesInfo(appmsg_token, cookie)
read_num, like_num, old_like_num = test.read_like_nums(article_url)

print(f"Reads: {read_num}, Likes: {like_num}")
```

### 3. Download Article as HTML

Save articles for offline reading:

```python
from wechatarticles import Url2Html

url = "https://mp.weixin.qq.com/s/..."

# Create output folder structure first:
# account_name/
#   └── imgs/

uh = Url2Html()
res = uh.run(url, mode=4)
```

## Two Main Approaches

### Approach 1: Web → PC/Mobile
1. Retrieve article URLs from WeChat's web interface
2. Login to WeChat (PC or mobile) to gather engagement metrics

### Approach 2: PC/Mobile → Metrics
1. Login directly to WeChat to access all articles (500+)
2. Extract engagement data using the same credentials

## Important Constraints

- **No Automated Login**: Manual credential extraction required
- **Rate Limiting**: Use 5-10 second delays between requests
- **Account-Specific**: Credentials must be updated per public account
- **Learning Tool**: Not suitable for production deployment without modification

## Next Steps

1. **Authentication**: Follow the [Authentication Guide](authentication.md) to obtain required credentials
2. **API Reference**: Explore the [API Documentation](api.md) for detailed method information
3. **Examples**: See [Usage Examples](examples.md) for complete working code

## Rate Limiting Guidelines

Always implement delays between requests to avoid being blocked:

```python
import time
import random

# Between article requests
for url in article_urls:
    process_article(url)
    time.sleep(random.uniform(5, 10))  # 5-10 seconds
```

Longer delays between page requests are recommended to maintain access.
