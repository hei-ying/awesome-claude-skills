# Usage Examples

## Complete Working Examples

### Example 1: Basic URL Collection

Extract article URLs from a public account webpage.

```python
import os
from pprint import pprint
from wechatarticles import PublicAccountsWeb

# Setup credentials
cookie = "your_official_cookie_here"
token = "your_token_here"
nickname = "target_account_name"
biz = "account_biz_identifier"

# Initialize scraper
paw = PublicAccountsWeb(cookie=cookie, token=token)

# Get first 5 articles
article_data = paw.get_urls(nickname, biz=biz, begin="0", count="5")
pprint(article_data)

# Alternative: Get total article count
total_articles = paw.articles_nums(nickname)
print(f"Total articles: {total_articles}")

# Alternative: Get account information
account_info = paw.official_info()
pprint(account_info)
```

**Output:**
```python
[
    {
        'url': 'https://mp.weixin.qq.com/s/abc123...',
        'title': 'Article Title',
        'date': '2025-01-15',
        # ... more fields
    },
    # ... more articles
]
```

---

### Example 2: Extract Engagement Metrics

Get read counts, likes, and comments from articles.

```python
import os
from pprint import pprint
from wechatarticles import ArticlesInfo

# Setup WeChat PC client credentials
appmsg_token = "your_appmsg_token"
cookie = "your_wechat_cookie"

# Target article
article_url = "https://mp.weixin.qq.com/s/example_article..."

# Initialize metrics extractor
test = ArticlesInfo(appmsg_token, cookie)

# Method 1: Get read and like counts
read_num, like_num, old_like_num = test.read_like_nums(article_url)
print(f"read_like_num: {read_num} {like_num} {old_like_num}")

# Method 2: Get all comments
comments = test.comments(article_url)
pprint(comments)
```

**Output:**
```
read_like_num: 1523 89 85
[
    {
        'user': 'Username',
        'text': 'Great article!',
        'timestamp': 1234567890
    },
    # ... more comments
]
```

---

### Example 3: Bulk Historical URL Collection

Rapidly collect large numbers of article URLs using historical access.

```python
import json
import os
import random
import time
from pprint import pprint
import pandas as pd
from wechatarticles import ArticlesInfo
from wechatarticles.utils import get_history_urls, verify_url

# Credentials
biz = "account_biz_id"
uin = "your_uin"
key = "your_key"  # Requires periodic renewal
appmsg_token = "your_appmsg_token"
cookie = "your_wechat_cookie"

# Initialize
ai = ArticlesInfo(appmsg_token, cookie)

# Helper function to save data
def save_xlsx(filename, data_list):
    """Export article data to Excel"""
    df = pd.DataFrame(data_list, columns=[
        'url', 'title', 'date', 'reads', 'likes', 'comments'
    ])
    df.to_excel(filename, index=False)
    print(f"Saved {len(data_list)} articles to {filename}")

# Helper function to process articles
def process_articles(article_list):
    """Extract metrics for a list of articles"""
    results = []

    for article in article_list:
        timestamp = article.get('timestamp')
        title = article.get('title')
        url = article.get('url')

        try:
            # Get engagement metrics
            read_num, like_num, old_like_num = ai.read_like_nums(url)

            # Get comments
            comments = ai.comments(url)
            comment_count = len(comments) if comments else 0

            results.append({
                'url': url,
                'title': title,
                'date': timestamp,
                'reads': read_num,
                'likes': like_num,
                'comments': comment_count
            })

            print(f"阅读：{read_num}; 在看: {like_num}; 点赞: {old_like_num}")

            # Rate limiting - important!
            time.sleep(random.uniform(5, 10))

        except Exception as e:
            print(f"Error processing {url}: {e}")
            continue

    return results

# Main workflow
def main():
    # Step 1: Get historical URLs (can retrieve 500+ articles)
    print("Fetching historical URLs...")
    article_urls = get_history_urls(biz, uin, key, offset=0)
    print(f"Found {len(article_urls)} articles")

    # Step 2: Process articles and get metrics
    print("Processing articles...")
    results = process_articles(article_urls)

    # Step 3: Save to Excel
    save_xlsx("article_data.xlsx", results)

    return results

if __name__ == "__main__":
    data = main()
    pprint(data[:5])  # Print first 5 results
```

**Excel Output:**
| url | title | date | reads | likes | comments |
|-----|-------|------|-------|-------|----------|
| https://... | Article 1 | 2025-01-15 | 1523 | 89 | 12 |
| https://... | Article 2 | 2025-01-14 | 2341 | 145 | 23 |

---

### Example 4: Download Articles as HTML

Convert articles to offline HTML format with image preservation.

```python
import os
from pprint import pprint
from wechatarticles import Url2Html

# Target article
url = "https://mp.weixin.qq.com/s/example_article..."

# IMPORTANT: Create directory structure first
account_name = "MyAccount"
os.makedirs(f"{account_name}/imgs", exist_ok=True)

# Initialize converter
uh = Url2Html()

# Download and convert to HTML (mode 4 preserves images)
result = uh.run(url, mode=4)

pprint(result)
print(f"Article saved to {account_name}/ directory")
```

**Directory Structure After:**
```
MyAccount/
├── imgs/
│   ├── image1.jpg
│   ├── image2.png
│   └── ...
└── article_title.html
```

---

### Example 5: Complete Analysis Pipeline

End-to-end workflow combining all features.

```python
import time
import random
import json
from datetime import datetime
from wechatarticles import PublicAccountsWeb, ArticlesInfo, Url2Html

class WeChatAnalyzer:
    def __init__(self, official_cookie, token, appmsg_token, wechat_cookie):
        self.paw = PublicAccountsWeb(cookie=official_cookie, token=token)
        self.ai = ArticlesInfo(appmsg_token, wechat_cookie)
        self.uh = Url2Html()

    def analyze_account(self, nickname, biz, max_articles=20):
        """Complete analysis of a public account"""
        results = []

        # Get article count
        total = self.paw.articles_nums(nickname)
        print(f"Total articles: {total}")

        # Get account info
        info = self.paw.official_info()
        print(f"Account: {info.get('name', 'Unknown')}")

        # Fetch articles
        articles = self.paw.get_urls(
            nickname,
            biz=biz,
            begin="0",
            count=str(max_articles)
        )

        # Process each article
        for i, article in enumerate(articles, 1):
            print(f"\nProcessing {i}/{len(articles)}: {article['title']}")

            url = article['url']

            try:
                # Get metrics
                reads, likes, old_likes = self.ai.read_like_nums(url)

                # Get comments
                comments = self.ai.comments(url)

                result = {
                    'title': article['title'],
                    'url': url,
                    'date': article.get('date'),
                    'reads': reads,
                    'likes': likes,
                    'like_change': likes - old_likes,
                    'comment_count': len(comments) if comments else 0,
                    'analyzed_at': datetime.now().isoformat()
                }

                results.append(result)
                print(f"  Reads: {reads}, Likes: {likes}, Comments: {result['comment_count']}")

                # Rate limiting
                time.sleep(random.uniform(5, 10))

            except Exception as e:
                print(f"  Error: {e}")
                continue

        return results

    def save_results(self, results, filename="analysis_results.json"):
        """Save analysis results to JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\nResults saved to {filename}")

    def download_top_articles(self, results, top_n=5):
        """Download HTML for top performing articles"""
        # Sort by reads
        top_articles = sorted(results, key=lambda x: x['reads'], reverse=True)[:top_n]

        print(f"\nDownloading top {top_n} articles...")
        for article in top_articles:
            try:
                print(f"  Downloading: {article['title']}")
                self.uh.run(article['url'], mode=4)
                time.sleep(random.uniform(3, 5))
            except Exception as e:
                print(f"  Error: {e}")

# Usage
if __name__ == "__main__":
    # Setup credentials
    analyzer = WeChatAnalyzer(
        official_cookie="your_official_cookie",
        token="your_token",
        appmsg_token="your_appmsg_token",
        wechat_cookie="your_wechat_cookie"
    )

    # Analyze account
    results = analyzer.analyze_account(
        nickname="TechBlog",
        biz="MzAxMjQ...",
        max_articles=20
    )

    # Save results
    analyzer.save_results(results)

    # Download top articles
    analyzer.download_top_articles(results, top_n=5)

    # Print summary
    total_reads = sum(r['reads'] for r in results)
    total_likes = sum(r['likes'] for r in results)
    print(f"\n=== Summary ===")
    print(f"Total articles analyzed: {len(results)}")
    print(f"Total reads: {total_reads}")
    print(f"Total likes: {total_likes}")
    print(f"Average reads per article: {total_reads // len(results)}")
```

---

## Common Patterns

### Pattern 1: Pagination

```python
# Fetch all articles with pagination
all_articles = []
begin = 0
count = 10

while True:
    articles = paw.get_urls(nickname, biz=biz, begin=str(begin), count=str(count))
    if not articles:
        break

    all_articles.extend(articles)
    begin += count
    time.sleep(2)  # Rate limiting
```

### Pattern 2: Error Recovery

```python
def safe_fetch_metrics(ai, url, max_retries=3):
    """Fetch metrics with retry logic"""
    for attempt in range(max_retries):
        try:
            return ai.read_like_nums(url)
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(5)
            else:
                return None, None, None
```

### Pattern 3: Batch Processing

```python
def process_in_batches(urls, batch_size=10):
    """Process URLs in batches with breaks"""
    for i in range(0, len(urls), batch_size):
        batch = urls[i:i + batch_size]

        for url in batch:
            process_article(url)
            time.sleep(random.uniform(5, 10))

        # Longer break between batches
        if i + batch_size < len(urls):
            print(f"Processed {i + batch_size}/{len(urls)}, taking a break...")
            time.sleep(random.uniform(30, 60))
```

## Next Steps

- Review [API Documentation](api.md) for detailed method signatures
- See [Authentication Guide](authentication.md) for credential setup
- Check [Getting Started](getting_started.md) for basic concepts
