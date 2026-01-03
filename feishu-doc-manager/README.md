# Feishu Doc Manager 配置指南

本文档详细说明如何配置和使用 feishu-doc-manager 技能。

## 目录

- [快速开始](#快速开始)
- [飞书应用配置](#飞书应用配置)
- [环境变量配置](#环境变量配置)
- [依赖安装](#依赖安装)
- [权限配置](#权限配置)
- [验证配置](#验证配置)
- [常见问题](#常见问题)

## 快速开始

### 前置条件

1. 飞书企业账号或飞书个人账号
2. Python 3.7+
3. 能够访问飞书 API（网络环境）

### 安装步骤概览

```
1. 创建飞书应用 → 2. 配置权限 → 3. 获取凭证 → 4. 设置环境变量 → 5. 安装依赖 → 6. 测试
```

## 飞书应用配置

### 步骤 1：创建飞书应用

1. 访问 [飞书开放平台](https://open.feishu.cn/)
2. 登录飞书账号
3. 进入"管理后台"
4. 点击"创建企业自建应用"
   - 或"创建个人自建应用"（个人用户）

5. 填写应用信息：
   - **应用名称**：Feishu Doc Manager（或自定义名称）
   - **应用描述**：自动同步文档到飞书
   - **应用图标**：可选

6. 点击"创建"

### 步骤 2：配置应用权限

在应用详情页面，找到"权限管理"：

#### 必需权限

**文档权限**：
- ✅ `docx:document:readonly` - 读取文档
- ✅ `docx:document:create` - 创建文档
- ✅ `docx:document:write` - 编辑文档
- ✅ `docx:document:content:readonly` - 读取文档内容

**文件权限**：
- ✅ `drive:drive:readonly` - 访问云文档
- ✅ `drive:file:readonly` - 读取文件
- ✅ `drive:file:create` - 上传文件

**搜索权限**（可选）：
- ⚡ `search:document:readonly` - 搜索文档

#### 配置方法

1. 在"权限管理"页面搜索上述权限
2. 勾选所需权限
3. 点击"批量开通权限"或"申请权限"

### 步骤 3：发布应用

1. 在应用管理后台，找到"权限与发布"
2. 点击"发布"按钮
3. 选择发布范围：
   - **企业应用**：选择"全员可用"或指定部门
   - **个人应用**：直接发布

4. 等待审核（通常即时生效）

### 步骤 4：获取凭证

在应用详情页面，找到"凭证与基础信息"：

1. 复制以下信息：
   - **App ID**：格式如 `cli_xxxxxxxxxxxxx`
   - **App Secret**：格式如 `xxxxxxxxxxxxxxxxxxxx`

2. **重要**：妥善保管 App Secret，不要泄露或提交到 git

## 环境变量配置

### Windows

#### PowerShell（临时，当前会话有效）

```powershell
$env:FEISHU_APP_ID="cli_xxxxxxxxxxxxx"
$env:FEISHU_APP_SECRET="xxxxxxxxxxxxxxxxxxxx"
```

#### PowerShell（永久，添加到用户环境变量）

```powershell
# 设置用户环境变量
[System.Environment]::SetEnvironmentVariable('FEISHU_APP_ID', 'cli_xxxxxxxxxxxxx', 'User')
[System.Environment]::SetEnvironmentVariable('FEISHU_APP_SECRET', 'xxxxxxxxxxxxxxxxxxxx', 'User')

# 重启终端生效
```

#### CMD（临时）

```cmd
set FEISHU_APP_ID=cli_xxxxxxxxxxxxx
set FEISHU_APP_SECRET=xxxxxxxxxxxxxxxxxxxx
```

#### CMD（永久，通过系统设置）

1. 右键"此电脑" → "属性"
2. 点击"高级系统设置"
3. 点击"环境变量"
4. 在"用户变量"中新建：
   - 变量名：`FEISHU_APP_ID`
   - 变量值：你的 App ID
5. 再新建：
   - 变量名：`FEISHU_APP_SECRET`
   - 变量值：你的 App Secret

### Linux / macOS

#### 临时（当前终端会话）

```bash
export FEISHU_APP_ID="cli_xxxxxxxxxxxxx"
export FEISHU_APP_SECRET="xxxxxxxxxxxxxxxxxxxx"
```

#### 永久（添加到 Shell 配置文件）

**Bash** (`~/.bashrc` 或 `~/.bash_profile`)：
```bash
echo 'export FEISHU_APP_ID="cli_xxxxxxxxxxxxx"' >> ~/.bashrc
echo 'export FEISHU_APP_SECRET="xxxxxxxxxxxxxxxxxxxx"' >> ~/.bashrc
source ~/.bashrc
```

**Zsh** (`~/.zshrc`)：
```bash
echo 'export FEISHU_APP_ID="cli_xxxxxxxxxxxxx"' >> ~/.zshrc
echo 'export FEISHU_APP_SECRET="xxxxxxxxxxxxxxxxxxxx"' >> ~/.zshrc
source ~/.zshrc
```

### 使用 .env 文件（开发环境推荐）

在项目根目录创建 `.env` 文件：

```bash
# .env
FEISHU_APP_ID=cli_xxxxxxxxxxxxx
FEISHU_APP_SECRET=xxxxxxxxxxxxxxxxxxxx
```

**重要**：将 `.env` 添加到 `.gitignore`：

```bash
echo ".env" >> .gitignore
```

**使用方法**（需要 python-dotenv）：
```python
from dotenv import load_dotenv
load_dotenv()  # 自动加载 .env 文件
```

### 验证环境变量

**Windows PowerShell**：
```powershell
echo $env:FEISHU_APP_ID
echo $env:FEISHU_APP_SECRET
```

**Linux / macOS**：
```bash
echo $FEISHU_APP_ID
echo $FEISHU_APP_SECRET
```

**Python 验证**：
```python
import os
print(os.getenv("FEISHU_APP_ID"))
print(os.getenv("FEISHU_APP_SECRET"))
```

## 依赖安装

### 基础依赖（必需）

```bash
pip install requests
```

### Mermaid 渲染依赖（可选）

#### 方式 1：使用 mermaid-cli（推荐）

**安装 Node.js**：
- 访问 [https://nodejs.org/](https://nodejs.org/)
- 下载并安装 LTS 版本

**安装 mermaid-cli**：
```bash
npm install -g @mermaid-js/mermaid-cli
```

**验证安装**：
```bash
mmdc --version
```

#### 方式 2：使用 pyppeteer

```bash
pip install pyppeteer
```

**首次使用会自动下载 Chromium**：
```python
# Python 脚本
import pyppeteer
# 自动下载浏览器
```

### 完整安装

```bash
# 基础依赖
pip install requests

# Mermaid 渲染（二选一）
npm install -g @mermaid-js/mermaid-cli
# 或
pip install pyppeteer

# 开发环境
pip install python-dotenv
```

### requirements.txt

创建 `requirements.txt`：

```txt
requests>=2.28.0
pyppeteer>=1.0.0
python-dotenv>=1.0.0
```

安装：
```bash
pip install -r requirements.txt
```

## 权限配置

### 飞书应用权限

确保以下权限已开通：

| 权限名称 | 权限标识 | 是否必需 | 用途 |
|---------|---------|---------|------|
| 读取文档 | `docx:document:readonly` | ✅ 必需 | 读取文档信息 |
| 创建文档 | `docx:document:create` | ✅ 必需 | 创建新文档 |
| 编辑文档 | `docx:document:write` | ✅ 必需 | 追加内容 |
| 读取文档内容 | `docx:document:content:readonly` | ✅ 必需 | 读取文档 block |
| 访问云文档 | `drive:drive:readonly` | ✅ 必需 | 访问文档空间 |
| 上传文件 | `drive:file:create` | ✅ 必需 | 上传图片 |
| 搜索文档 | `search:document:readonly` | ⚡ 可选 | 搜索现有文档 |

### 权限开通检查

1. 登录飞书开放平台
2. 进入应用管理
3. 点击"权限管理"
4. 搜索上述权限标识
5. 确认状态为"已开通"

### 权限不足的处理

如果提示"无权限"：

1. 检查应用权限是否已开通
2. 检查应用是否已发布
3. 重新获取 tenant_access_token
4. 联系飞书管理员（企业应用）

## 验证配置

### 测试脚本

创建 `test_config.py`：

```python
#!/usr/bin/env python3
"""
配置验证脚本
"""
import os
import sys

def check_env_vars():
    """检查环境变量"""
    print("检查环境变量...")

    app_id = os.getenv("FEISHU_APP_ID")
    app_secret = os.getenv("FEISHU_APP_SECRET")

    if not app_id:
        print("❌ FEISHU_APP_ID 未设置")
        return False
    else:
        print(f"✓ FEISHU_APP_ID: {app_id[:10]}...")

    if not app_secret:
        print("❌ FEISHU_APP_SECRET 未设置")
        return False
    else:
        print(f"✓ FEISHU_APP_SECRET: {app_secret[:10]}...")

    return True

def check_dependencies():
    """检查依赖"""
    print("\n检查依赖...")

    # 检查 requests
    try:
        import requests
        print(f"✓ requests {requests.__version__}")
    except ImportError:
        print("❌ requests 未安装")
        print("  运行: pip install requests")
        return False

    # 检查 mermaid-cli
    import subprocess
    try:
        result = subprocess.run(
            ["mmdc", "--version"],
            capture_output=True,
            timeout=5
        )
        if result.returncode == 0:
            print("✓ mermaid-cli 已安装")
    except (FileNotFoundError, subprocess.TimeoutExpired):
        print("⚠️  mermaid-cli 未安装（可选）")
        print("  安装: npm install -g @mermaid-js/mermaid-cli")

    # 检查 pyppeteer
    try:
        import pyppeteer
        print("✓ pyppeteer 已安装")
    except ImportError:
        print("⚠️  pyppeteer 未安装（可选）")
        print("  安装: pip install pyppeteer")

    return True

def test_api_connection():
    """测试 API 连接"""
    print("\n测试 API 连接...")

    try:
        from scripts.feishu_api_client import FeishuAPIClient

        client = FeishuAPIClient()
        token = client.get_tenant_access_token()
        print(f"✓ API 连接成功")
        print(f"  Token: {token[:20]}...")

        return True
    except Exception as e:
        print(f"❌ API 连接失败: {e}")
        return False

def main():
    """主函数"""
    print("=" * 50)
    print("Feishu Doc Manager 配置验证")
    print("=" * 50)

    checks = [
        check_env_vars(),
        check_dependencies(),
        test_api_connection()
    ]

    print("\n" + "=" * 50)
    if all(checks):
        print("✓ 配置验证通过！")
        print("\n可以开始使用 feishu-doc-manager")
        return 0
    else:
        print("❌ 配置验证失败，请修复上述问题")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

运行验证：
```bash
python test_config.py
```

### 功能测试

创建测试文档 `test.md`：
```markdown
# 测试文档

这是一个测试文档。

## 功能测试

- 文本支持 ✓
- 列表支持 ✓
```

同步测试：
```bash
python scripts/feishu_api_client.py \
  --markdown test.md \
  --title "测试文档" \
  --preview
```

预期输出：
```
📝 正在解析 Markdown...
🔍 正在搜索现有文档...
✓ 未找到文档，将创建新文档

==================================================
即将写入的内容结构
==================================================
标题: 测试文档
总块数: 4
批次数: 1

块类型分布:
  - heading1: 1
  - paragraph: 1
  - heading2: 1
  - bulleted_list: 1

是否确认写入？[y/N]: y
📝 正在写入内容 (共 4 个 blocks)...
  正在写入第 1/1 批...
    ✓ 第 1 批完成

✅ 同步完成！
文档标题: 测试文档
文档ID: doxcnxxxxxxxxxxxxxx
访问链接: https://feishu.cn/docx/doxcnxxxxxxxxxxxxxx
```

## 常见问题

### Q1: 环境变量设置后仍然提示未设置？

**原因**：终端会话未刷新

**解决**：
- Windows：关闭并重新打开终端
- Linux/Mac：执行 `source ~/.bashrc` 或重启终端

### Q2: 提示"应用无权限"？

**检查清单**：
1. ✅ 应用权限已开通
2. ✅ 应用已发布
3. ✅ App ID 和 Secret 正确
4. ✅ 使用正确的账号登录飞书

**企业应用**：联系管理员确认权限

### Q3: 图片上传失败？

**可能原因**：
1. 图片路径错误
2. 图片格式不支持
3. 图片文件过大（> 10MB）
4. 网络问题

**解决**：
```bash
# 检查图片路径
ls ./images/

# 压缩图片
mogrify -resize 80% -quality 85 *.png

# 使用绝对路径
python scripts/feishu_api_client.py \
  --markdown doc.md \
  --image-dir /absolute/path/to/images \
  --title "文档"
```

### Q4: Mermaid 图表不显示？

**检查清单**：
1. ✅ 安装了 mermaid-cli 或 pyppeteer
2. ✅ 使用 `--render-mermaid` 参数
3. ✅ Mermaid 语法正确

**测试渲染**：
```bash
python scripts/mermaid_renderer.py \
  "graph TD; A-->B;" \
  test.png
```

### Q5: 如何在多台电脑上使用？

**方案 1：复制配置**
- 复制 App ID 和 Secret
- 在新电脑上设置环境变量

**方案 2：使用配置文件**
创建 `config.json`（不要提交到 git）：
```json
{
  "app_id": "cli_xxxxxxxxxxxxx",
  "app_secret": "xxxxxxxxxxxxxxxxxxxx"
}
```

修改脚本读取配置：
```python
import json

with open("config.json") as f:
    config = json.load(f)

os.environ["FEISHU_APP_ID"] = config["app_id"]
os.environ["FEISHU_APP_SECRET"] = config["app_secret"]
```

### Q6: Token 过期怎么办？

脚本会自动处理 token 刷新，无需手动干预。

如果手动调用 API，需要重新获取 token：
```python
client = FeishuAPIClient()
# token 会自动缓存和刷新
```

### Q7: 如何提高上传速度？

**优化建议**：
1. 批量上传图片后统一插入
2. 压缩图片大小
3. 使用更快的网络
4. 减小单次上传的图片数量

### Q8: 支持代理吗？

**设置代理**：
```python
import os

# HTTP 代理
os.environ["HTTP_PROXY"] = "http://proxy.example.com:8080"
os.environ["HTTPS_PROXY"] = "http://proxy.example.com:8080"

# 或在 requests 中配置
import requests
proxies = {
    "http": "http://proxy.example.com:8080",
    "https": "http://proxy.example.com:8080"
}
requests.post(url, proxies=proxies)
```

## 安全建议

### 保护凭证安全

1. **不要提交到 git**：
   ```bash
   echo ".env" >> .gitignore
   echo "config.json" >> .gitignore
   ```

2. **使用环境变量**：
   - ✅ 推荐：环境变量
   - ⚠️ 谨慎：配置文件（添加到 .gitignore）
   - ❌ 禁止：硬编码在代码中

3. **定期更换 Secret**：
   - 在飞书开放平台重新生成
   - 更新环境变量

4. **限制权限范围**：
   - 只申请必需的权限
   - 企业应用可以限制到特定部门

### 访问控制

**企业应用**：
- 限制应用可用范围
- 设置 IP 白名单（如支持）
- 定期审计应用使用情况

**个人应用**：
- 不要分享 App Secret
- 定期检查文档访问权限

## 下一步

配置完成后，可以：

1. 查看 [examples.md](examples.md) 了解详细使用示例
2. 阅读 [reference.md](reference.md) 深入了解 API
3. 开始同步你的第一个文档！

## 获取帮助

遇到问题？

1. 查看本文档的"常见问题"部分
2. 检查飞书开放平台文档
3. 运行 `test_config.py` 诊断问题

---

**祝使用愉快！** 🎉
