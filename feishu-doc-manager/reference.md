# 飞书 API 参考文档

本文档提供飞书文档 API 的详细参考信息，包括 Block 结构定义、API 端点、错误码等。

## 目录

- [API 基础](#api-基础)
- [Block 类型定义](#block-类型定义)
- [API 端点](#api-端点)
- [错误码参考](#错误码参考)
- [权限说明](#权限说明)

## API 基础

### 认证方式

飞书 API 使用 OAuth 2.0 进行认证。需要先获取 `tenant_access_token`。

#### 获取 tenant_access_token

**端点**：`POST https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal`

**请求体**：
```json
{
  "app_id": "your_app_id",
  "app_secret": "your_app_secret"
}
```

**响应**：
```json
{
  "code": 0,
  "tenant_access_token": "t-xxx",
  "expire": 7200
}
```

**Token 有效期**：7200 秒（2 小时）

**最佳实践**：
- 缓存 token，避免频繁请求
- 提前 5 分钟刷新 token
- 使用 `Authorization: Bearer {token}` 头部携带 token

### API 请求格式

所有 API 请求应包含：
- **Authorization** 头部：`Bearer {tenant_access_token}`
- **Content-Type**：`application/json`

示例：
```python
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
```

## Block 类型定义

飞书文档由一系列 Block 组成，每个 Block 代表文档中的一个元素。

### Block 基础结构

```json
{
  "block_type": integer,  // Block 类型编号
  "[type_name]": {        // 类型特定的数据
    "elements": [...]
  }
}
```

### 常用 Block 类型

#### 1. 段落 (Paragraph)

**block_type**: `1`

**结构**：
```json
{
  "block_type": 1,
  "paragraph": {
    "elements": [
      {
        "text_run": {
          "content": "文本内容",
          "text_element_style": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "link": {
              "url": "https://example.com"
            }
          }
        }
      }
    ]
  }
}
```

**文本样式属性**：
- `bold`: 粗体
- `italic`: 斜体
- `strikethrough`: 删除线
- `underline`: 下划线
- `code`: 行内代码
- `link`: 超链接

#### 2. 一级标题 (Heading 1)

**block_type**: `2`

**结构**：
```json
{
  "block_type": 2,
  "heading1": {
    "elements": [
      {
        "text_run": {
          "content": "标题内容"
        }
      }
    ]
  }
}
```

#### 3. 无序列表 (Bulleted List)

**block_type**: `3`

**结构**：
```json
{
  "block_type": 3,
  "bulleted_list": {
    "elements": [
      {
        "text_run": {
          "content": "列表项内容"
        }
      }
    ]
  }
}
```

#### 4. 二级标题 (Heading 2)

**block_type**: `4`

**结构**：
```json
{
  "block_type": 4,
  "heading2": {
    "elements": [
      {
        "text_run": {
          "content": "二级标题"
        }
      }
    ]
  }
}
```

#### 6. 三级标题 (Heading 3)

**block_type**: `6`

**结构**：
```json
{
  "block_type": 6,
  "heading3": {
    "elements": [
      {
        "text_run": {
          "content": "三级标题"
        }
      }
    ]
  }
}
```

#### 8. 代码块 (Code)

**block_type**: `8`

**结构**：
```json
{
  "block_type": 8,
  "code": {
    "style": {},
    "elements": [
      {
        "text_run": {
          "content": "代码内容"
        }
      }
    ],
    "language": "python",
    "caption": {}
  }
}
```

**支持的语言**：
- `python`, `javascript`, `java`, `go`, `rust`, `c++`, `c`, `c#`
- `typescript`, `php`, `ruby`, `swift`, `kotlin`
- `sql`, `html`, `css`, `json`, `yaml`, `xml`, `markdown`
- `bash`, `shell`, `powershell`, `dockerfile`
- 其他 50+ 种语言

#### 11. 有序列表 (Ordered List)

**block_type**: `11`

**结构**：
```json
{
  "block_type": 11,
  "ordered_list": {
    "elements": [
      {
        "text_run": {
          "content": "有序列表项"
        }
      }
    ]
  }
}
```

#### 25. 图片 (Image)

**block_type**: `25`

**结构**：
```json
{
  "block_type": 25,
  "image": {
    "file_token": "file_xxxxx"
  }
}
```

**获取 file_token**：
1. 先调用图片上传 API
2. 返回的 `file_token` 用于在文档中引用图片

#### 完整 Block 类型映射表

| Block Type | 名称 | 英文 | 说明 |
|-----------|------|------|------|
| 1 | 段落 | paragraph | 普通文本段落 |
| 2 | 一级标题 | heading1 | H1 标题 |
| 3 | 无序列表 | bulleted_list | 圆点列表 |
| 4 | 二级标题 | heading2 | H2 标题 |
| 5 | 引用块 | quote | 引用内容 |
| 6 | 三级标题 | heading3 | H3 标题 |
| 7 | 分隔线 | divider | 水平线 |
| 8 | 代码块 | code | 代码片段 |
| 9 | 待办事项 | todo | Todo 项 |
| 10 | 表格 | table | 表格 |
| 11 | 有序列表 | ordered_list | 数字列表 |
| 12 | 高亮块 | callout | 强调内容 |
| 13 | 公式 | equation | 数学公式 |
| 14 | 视图 | view | 数据库视图 |
| 15 | 文件 | file | 文件附件 |
| 16 | 视频 | video | 视频嵌入 |
| 17 | 音频 | audio | 音频嵌入 |
| 18 | 链接 | link | 外部链接卡片 |
| 19 | 用户 | user | @用户 |
| 20 | 群组 | group | @群组 |
| 21 | 文档 | doc | 文档引用 |
| 22 | 维度 | bitable | 多维表格 |
| 23 | 投票 | poll | 投票组件 |
| 24 | 目录 | table_of_contents | 文档目录 |
| 25 | 图片 | image | 图片 |
| 26 | 代码模拟器 | code_simulator | 交互式代码 |
| 27 | 文件卡片 | filecard | 文件卡片 |

### Text Element 结构

文本元素是构成大多数 Block 的基本单元。

**完整结构**：
```json
{
  "text_run": {
    "content": "文本内容",
    "text_element_style": {
      "bold": true,
      "italic": false,
      "strikethrough": false,
      "underline": false,
      "code": false,
      "link": {
        "url": "https://example.com"
      },
      "inline_code": true
    }
  }
}
```

**样式优先级**：
- 内联样式优先于整体样式
- `link` 和 `inline_code` 不能同时使用
- `code` 和 `inline_code` 效果相同

## API 端点

### 1. 文档搜索

**端点**：`POST https://open.feishu.cn/open-apis/docx/v1/documents/search`

**请求体**：
```json
{
  "query": "文档标题",
  "limit": 10
}
```

**响应**：
```json
{
  "code": 0,
  "data": {
    "items": [
      {
        "document_id": "doxcnxxxxxxxxxxxxxx",
        "title": "文档标题",
        "revision_id": 123,
        "create_time": 1234567890
      }
    ]
  }
}
```

**权限要求**：
- `docx:document:readonly`

**注意事项**：
- 搜索功能可能需要额外开通
- 默认返回最相关的 10 条结果
- 支持模糊匹配

### 2. 创建文档

**端点**：`POST https://open.feishu.cn/open-apis/docx/v1/documents`

**请求体**：
```json
{
  "title": "文档标题",
  "document": {
    "blocks": [
      {
        "block_type": 2,
        "heading1": {
          "elements": [
            {
              "text_run": {
                "content": "这是标题"
              }
            }
          ]
        }
      },
      {
        "block_type": 1,
        "paragraph": {
          "elements": [
            {
              "text_run": {
                "content": "这是正文"
              }
            }
          ]
        }
      }
    ]
  }
}
```

**响应**：
```json
{
  "code": 0,
  "data": {
    "document": {
      "document_id": "doxcnxxxxxxxxxxxxxx",
      "revision_id": 123
    }
  }
}
```

**限制**：
- 单次最多创建 50 个 block
- 超过 50 个需要分批创建

### 3. 追加内容块

**端点**：`POST https://open.feishu.cn/open-apis/docx/v1/documents/{document_id}/blocks/batch_create`

**路径参数**：
- `document_id`: 文档 ID

**请求体**：
```json
{
  "blocks": [
    {
      "block_type": 1,
      "paragraph": {
        "elements": [
          {
            "text_run": {
              "content": "追加的内容"
            }
          }
        ]
      }
    }
  ],
  "index": -1
}
```

**参数说明**：
- `index`: 插入位置
  - `-1`: 追加到文档末尾（默认）
  - `0`: 插入到文档开头
  - `block_id`: 插入到指定 block 之后

**响应**：
```json
{
  "code": 0,
  "data": {
    "blocks": [
      {
        "block_id": "doxcnxxxxxxxxxxxxxx",
        "block_type": 1
      }
    ]
  }
}
```

**限制**：
- 单次最多追加 50 个 block
- `index` 参数可选

### 4. 上传图片

**端点**：`POST https://open.feishu.cn/open-apis/drive/v1/medias/upload_all`

**请求头**：
```
Content-Type: application/octet-stream
Authorization: Bearer {tenant_access_token}
```

**查询参数**：
- `parent_type`: 父节点类型，通常为 `docx`
- `parent_node`: 父节点 ID（可选）
- `file_name`: 文件名
- `file_size`: 文件大小（字节）
- `file_hash`: 文件 SHA256 哈希值

**请求体**：
- 文件的二进制数据

**响应**：
```json
{
  "code": 0,
  "data": {
    "file_token": "file_xxxxx",
    "upload_key": "upload_key_xxxxx"
  }
}
```

**计算文件哈希**：
```python
import hashlib

with open('image.png', 'rb') as f:
    data = f.read()
    file_hash = hashlib.sha256(data).hexdigest()
    file_size = len(data)
```

**支持的图片格式**：
- PNG
- JPEG / JPG
- GIF
- BMP
- WEBP

**限制**：
- 单个文件最大 10 MB
- 建议图片分辨率不超过 4K
- 支持分片上传大文件

### 5. 获取文档信息

**端点**：`GET https://open.feishu.cn/open-apis/docx/v1/documents/{document_id}`

**路径参数**：
- `document_id`: 文档 ID

**响应**：
```json
{
  "code": 0,
  "data": {
    "document": {
      "document_id": "doxcnxxxxxxxxxxxxxx",
      "title": "文档标题",
      "revision_id": 123,
      "create_time": 1234567890,
      "update_time": 1234599999
    }
  }
}
```

### 6. 获取文档块列表

**端点**：`GET https://open.feishu.cn/open-apis/docx/v1/documents/{document_id}/blocks/{block_id}/children`

**路径参数**：
- `document_id`: 文档 ID
- `block_id`: 块 ID（文档根节点为 `0`）

**查询参数**：
- `page_size`: 每页数量（最大 100）
- `page_token`: 分页 token

**响应**：
```json
{
  "code": 0,
  "data": {
    "items": [
      {
        "block_id": "doxcnxxxxxxxxxxxxxx",
        "block_type": 1,
        "paragraph": {
          "elements": [...]
        }
      }
    ],
    "page_token": "next_page_token"
  }
}
```

### 7. 更新块内容

**端点**：`PATCH https://open.feishu.cn/open-apis/docx/v1/documents/{document_id}/blocks/{block_id}`

**路径参数**：
- `document_id`: 文档 ID
- `block_id`: 块 ID

**请求体**：
```json
{
  "block": {
    "block_type": 1,
    "paragraph": {
      "elements": [
        {
          "text_run": {
            "content": "更新后的内容"
          }
        }
      ]
    }
  },
  "revision_id": 123
}
```

**注意事项**：
- 必须提供最新的 `revision_id` 避免冲突
- 不可修改 block_type

## 错误码参考

### 通用错误码

| 错误码 | 说明 | 解决方案 |
|-------|------|---------|
| 0 | 成功 | - |
| 99991663 | 无权限 | 检查应用权限配置 |
| 99991400 | 功能未开通 | 开通相应功能 |
| 99991401 | 文档不存在 | 检查 document_id |
| 99991668 | 参数错误 | 检查请求参数 |
| 99991669 | 请求过于频繁 | 降低请求频率 |
| 99991636 | Token 无效 | 重新获取 token |

### 认证相关错误

| 错误码 | 说明 | 解决方案 |
|-------|------|---------|
| 99991668 | app_id 或 app_secret 错误 | 检查凭证 |
| 99991636 | tenant_access_token 过期 | 刷新 token |
| 99991663 | 应用无权限访问资源 | 配置应用权限 |

### 文档操作错误

| 错误码 | 说明 | 解决方案 |
|-------|------|---------|
| 99991401 | 文档不存在 | 检查 document_id |
| 99991665 | 文档已删除 | 文档已被删除 |
| 99991666 | 文档被锁定 | 等待解锁或联系管理员 |
| 99991667 | revision_id 不匹配 | 获取最新的 revision_id |

### 文件上传错误

| 错误码 | 说明 | 解决方案 |
|-------|------|---------|
| 99991668 | 文件大小超限 | 文件不能超过 10 MB |
| 99991669 | 文件格式不支持 | 使用支持的格式 |
| 99991670 | 文件哈希不匹配 | 重新计算 SHA256 |
| 99991671 | 父节点不存在 | 检查 parent_node |

### 错误处理示例

```python
try:
    result = client.create_document(title, blocks)
except FeishuAPIError as e:
    if e.code == 99991663:
        print("❌ 应用无权限，请在飞书开放平台配置权限")
    elif e.code == 99991401:
        print("❌ 文档不存在，请检查 document_id")
    elif e.code == 99991636:
        print("❌ Token 过期，正在重新获取...")
        client.refresh_token()
    else:
        print(f"❌ API 错误: {e.code} - {e.msg}")
```

## 权限说明

### 应用权限配置

在飞书开放平台需要配置以下权限：

#### 文档权限

- **docx:document:readonly**: 读取文档
- **docx:document:create**: 创建文档
- **docx:document:write**: 编辑文档
- **docx:document:content:readonly**: 读取文档内容

#### 文件权限

- **drive:drive:readonly**: 访问云文档
- **drive:file:readonly**: 读取文件
- **drive:file:create**: 上传文件

#### 搜索权限

- **search:document:readonly**: 搜索文档

### 权限申请流程

1. 打开飞书开放平台：https://open.feishu.cn/
2. 创建自建应用
3. 在"权限管理"中申请所需权限
4. 在"权限与发布"中发布权限
5. 在飞书管理后台审核并开通权限

### 权限范围

- **获取文档所有信息**: 需要 `docx:document:readonly` + `docx:document:content:readonly`
- **创建文档**: 需要 `docx:document:create`
- **编辑文档**: 需要 `docx:document:write`
- **上传图片**: 需要 `drive:file:create`

## 高级用法

### 分批写入策略

当文档内容超过 50 个 block 时，需要分批写入：

```python
def write_in_batches(client, document_id, blocks):
    batch_size = 50

    # 第一批：创建文档
    first_batch = blocks[:batch_size]
    result = client.create_document(title, first_batch)
    document_id = result["document_id"]

    # 后续批次：追加内容
    for i in range(batch_size, len(blocks), batch_size):
        batch = blocks[i:i + batch_size]
        client.append_blocks(document_id, batch)

    return document_id
```

### 幂等性保证

```python
def write_with_idempotency(client, title, blocks):
    # 先搜索文档
    existing = client.search_document(title)

    if existing:
        # 追加到现有文档
        document_id = existing["document_id"]
        client.append_blocks(document_id, blocks)
    else:
        # 创建新文档
        result = client.create_document(title, blocks)
        document_id = result["document_id"]

    return document_id
```

### 图片缓存优化

```python
class ImageCache:
    def __init__(self, cache_file="image_cache.json"):
        self.cache_file = cache_file
        self.cache = self._load_cache()

    def get_token(self, image_path):
        if image_path in self.cache:
            return self.cache[image_path]
        return None

    def set_token(self, image_path, token):
        self.cache[image_path] = token
        self._save_cache()

    def _load_cache(self):
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r') as f:
                return json.load(f)
        return {}

    def _save_cache(self):
        with open(self.cache_file, 'w') as f:
            json.dump(self.cache, f, indent=2)
```

### Markdown 到 Block 转换完整示例

```python
def markdown_to_blocks(markdown_text):
    """
    将 Markdown 转换为飞书 Block 数组

    支持的语法：
    - # ## ### 标题
    - **bold**, *italic*, `code`
    - - 列表, 1. 有序列表
    - ```代码块```
    - ![图片](path)
    """
    parser = MarkdownParser()
    blocks = parser.parse(markdown_text)
    return blocks
```

## 参考资料

- [飞书开放平台文档](https://open.feishu.cn/document/server-docs/docs/docs/docx-v1/document)
- [飞书文档 API 规范](https://open.feishu.cn/document/server-docs/docs/docs/docx-v1/document/introduction)
- [飞书权限管理](https://open.feishu.cn/document/ukTMukTMukTM/uUTNz4SN1MjL1UzM)
- [飞书 API 速率限制](https://open.feishu.cn/document/ukTMukTMukTM/uUTNz4SN1MjL1UzM)

## 更新日志

- **2025-01-03**: 初始版本，包含常用 Block 类型和 API 端点
