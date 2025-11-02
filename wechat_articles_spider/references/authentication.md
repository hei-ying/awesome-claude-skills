# Authentication Guide

## Overview

WeChat Articles Spider requires manual extraction of authentication credentials. There are two sets of credentials needed depending on which features you use:

1. **Official Account Credentials** (`official_cookie`, `token`) - For web-based scraping
2. **WeChat Client Credentials** (`wechat_cookie`, `appmsg_token`) - For engagement metrics

## Method 1: Official Account Credentials

### Required For
- `PublicAccountsWeb` class
- Web-based article URL collection

### Prerequisites
- WeChat personal subscription account
- Access to mp.weixin.qq.com

### Steps

1. **Login to Official Account Platform**
   - Navigate to https://mp.weixin.qq.com
   - Login with your credentials

2. **Open Developer Tools**
   - Press `F12` in your browser
   - Chrome or Firefox recommended

3. **Capture Network Traffic**
   - Switch to the "Network" tab in Developer Tools
   - Refresh the webpage (F5)

4. **Extract Credentials**
   - Look for network requests in the list
   - Find a request to the WeChat API
   - Copy the following values:
     - **Cookie**: Full cookie string from request headers
     - **Token**: Token parameter from the request URL or headers

5. **Use in Code**
```python
from wechatarticles import PublicAccountsWeb

official_cookie = "your_cookie_value_here"
token = "your_token_value_here"

paw = PublicAccountsWeb(cookie=official_cookie, token=token)
```

### Finding the Right Request

Look for requests containing:
- URLs with `/mp/` in the path
- GET or POST requests to WeChat API endpoints
- Headers containing Cookie information

## Method 2: WeChat PC Client Credentials

### Required For
- `ArticlesInfo` class
- Engagement metrics (reads, likes, comments)
- Historical article collection

### Prerequisites
- WeChat PC client installed
- Packet capture tool (e.g., Fiddler, Charles Proxy)
- Active WeChat login session

### Steps

1. **Setup Packet Capture Tool**
   - Install Fiddler or similar tool
   - Configure to capture HTTPS traffic
   - Enable system proxy

2. **Login to WeChat PC Client**
   - Open WeChat on your computer
   - Ensure you're logged in successfully

3. **Trigger API Requests**
   - Navigate to a public account
   - Open an article
   - Let the page fully load

4. **Capture API Request**
   - In Fiddler, look for requests to:
     - `/mp/getappmsgext?...`
     - Other WeChat API endpoints
   - These contain the metrics (read_num, like_num)

5. **Extract Credentials**
   - **Cookie**: Full cookie string from the request
   - **appmsg_token**: Token from the request parameters or body
   - **uin**: User ID (for some features)
   - **key**: Authentication key (requires periodic renewal)

6. **Use in Code**
```python
from wechatarticles import ArticlesInfo

appmsg_token = "your_appmsg_token"
wechat_cookie = "your_wechat_cookie"

ai = ArticlesInfo(appmsg_token, wechat_cookie)
```

## Additional Parameters

### For Historical URL Collection

Some features require additional parameters:

```python
from wechatarticles.utils import get_history_urls

biz = "account_biz_identifier"  # From account info
uin = "your_uin"                # Your WeChat ID
key = "session_key"             # Requires periodic renewal
```

### Parameter Locations

- **biz**: Found in article URLs (e.g., `?__biz=XXXXX`)
- **uin**: Extracted from WeChat login session
- **key**: Obtained from authenticated API requests
- **nickname**: The public account's display name

## Security Notes

⚠️ **Important Security Considerations**:

1. **Never share credentials**: These tokens provide full access to your WeChat session
2. **Token expiration**: Most tokens expire after a few hours
3. **Renewal required**: Update credentials when they expire
4. **Account-specific**: Each public account may require different credentials
5. **Rate limiting**: Excessive requests may trigger security blocks

## Credential Refresh

Credentials typically expire after:
- **Cookies**: 24-48 hours
- **Tokens**: 1-24 hours
- **Keys**: Varies, may need renewal per session

When you see authentication errors, repeat the extraction process to get fresh credentials.

## Common Issues

### Invalid Cookie/Token
- **Symptom**: Authentication errors, empty responses
- **Solution**: Extract fresh credentials following the steps above

### Access Denied
- **Symptom**: HTTP 403 or similar errors
- **Solution**: Check rate limiting, ensure credentials are current

### Missing Parameters
- **Symptom**: `KeyError` or parameter not found
- **Solution**: Verify all required parameters are extracted correctly

## Example: Complete Setup

```python
# Official account credentials
official_cookie = "paste_your_cookie_here"
token = "paste_your_token_here"

# WeChat client credentials
appmsg_token = "paste_appmsg_token_here"
wechat_cookie = "paste_wechat_cookie_here"

# Account identifiers
nickname = "target_account_name"
biz = "account_biz_id"

# Initialize classes
from wechatarticles import PublicAccountsWeb, ArticlesInfo

paw = PublicAccountsWeb(cookie=official_cookie, token=token)
ai = ArticlesInfo(appmsg_token, wechat_cookie)

# Now you're ready to use the API!
```

## Next Steps

Once you have credentials configured:
1. See [API Documentation](api.md) for available methods
2. Check [Usage Examples](examples.md) for complete workflows
3. Review [Getting Started](getting_started.md) for basic usage patterns
