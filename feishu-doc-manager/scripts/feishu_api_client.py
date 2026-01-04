#!/usr/bin/env python3
"""
飞书文档 API 客户端
负责与飞书 API 交互，包括文档创建、内容写入、图片上传等功能
"""

import os
import sys
import json
import requests
import re
from pathlib import Path
from typing import List, Dict, Optional, Any
import base64
import hashlib
import time


class FeishuAPIError(Exception):
    """飞书 API 错误"""
    def __init__(self, code: int, msg: str):
        self.code = code
        self.msg = msg
        super().__init__(f"API Error {code}: {msg}")


class FeishuAPIClient:
    """飞书 API 客户端"""

    def __init__(self):
        self.app_id = os.getenv("FEISHU_APP_ID")
        self.app_secret = os.getenv("FEISHU_APP_SECRET")
        self.folder_token = os.getenv("FEISHU_FOLDER_TOKEN")  # 新增：文件夹 Token

        # 强制检查环境变量
        self._check_env_vars()

        self.tenant_access_token = None
        self.token_expires_at = 0
        self.api_base = "https://open.feishu.cn/open-apis"

    def _check_env_vars(self):
        """检查并提醒配置环境变量"""
        missing = []
        if not self.app_id:
            missing.append("FEISHU_APP_ID")
        if not self.app_secret:
            missing.append("FEISHU_APP_SECRET")
        if not self.folder_token:
            missing.append("FEISHU_FOLDER_TOKEN")

        if missing:
            print(f"❌ 错误：缺少必要的环境变量: {', '.join(missing)}")
            print("\n请按以下步骤配置：")
            print("\n1. 获取授权文件夹的 Token")
            print("   - 在飞书中打开目标文件夹")
            print("   - 从 URL 中复制 folder_token（folder/ 后面的一串 ID）")
            print("   - URL 格式: https://feishu.cn/drive/folder/{folder_token}")
            print("\n2. 设置环境变量（Windows PowerShell 示例）：")
            for var in missing:
                print(f'   $env:{var}="your_value_here"')
            print("\n  Linux/Mac 示例：")
            for var in missing:
                print(f'   export {var}="your_value_here"')
            print("\n⚠️  只有配置了 FEISHU_FOLDER_TOKEN，同步后的文档才具有编辑权限。")
            sys.exit(1)

    def get_tenant_access_token(self) -> str:
        """获取 tenant_access_token"""
        # 如果 token 还有 5 分钟以上有效期，直接返回
        if self.tenant_access_token and time.time() < self.token_expires_at - 300:
            return self.tenant_access_token

        # 获取新 token
        url = f"{self.api_base}/auth/v3/tenant_access_token/internal"
        payload = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }

        response = requests.post(url, json=payload)
        result = response.json()

        if result.get("code") != 0:
            raise FeishuAPIError(result.get("code"), result.get("msg"))

        self.tenant_access_token = result.get("tenant_access_token")
        # token 有效期 2 小时，提前 5 分钟刷新
        self.token_expires_at = time.time() + 7200 - 300

        return self.tenant_access_token

    def _request(self, method: str, endpoint: str, **kwargs) -> Dict:
        """发送 API 请求"""
        token = self.get_tenant_access_token()
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {token}"

        url = f"{self.api_base}/{endpoint}"

        # 调试：打印请求详情
        import json
        if "json" in kwargs and endpoint.startswith("docx/v1/documents") and method == "POST":
            print(f"    [DEBUG] 创建文档请求")
            print(f"    [DEBUG] 请求 body keys: {list(kwargs['json'].keys())}")
            if "document" in kwargs["json"]:
                print(f"    [DEBUG] document keys: {list(kwargs['json']['document'].keys())}")
                if "blocks" in kwargs["json"]["document"]:
                    blocks = kwargs["json"]["document"]["blocks"]
                    print(f"    [DEBUG] blocks 数量: {len(blocks)}")
                    if blocks:
                        print(f"    [DEBUG] 第一个 block: {json.dumps(blocks[0], ensure_ascii=False)}")

        response = requests.request(method, url, headers=headers, **kwargs)

        # 调试：打印原始响应文本
        if endpoint.startswith("docx/v1/documents") and "blocks" in endpoint:
            print(f"    [DEBUG] API 响应状态码: {response.status_code}")
            print(f"    [DEBUG] API 响应文本: {response.text[:500]}")

        # 调试：打印响应
        try:
            result = response.json()
        except Exception as e:
            print(f"    [DEBUG] JSON 解析失败: {e}")
            print(f"    [DEBUG] 原始响应: {response.text}")
            raise

        # 打印创建文档的完整响应
        if endpoint == "docx/v1/documents" and method == "POST":
            print(f"    [DEBUG] 创建文档响应:")
            print(f"    [DEBUG] 完整响应: {json.dumps(result, ensure_ascii=False)[:500]}")

        if result.get("code") != 0:
            print(f"    [DEBUG] API 错误响应: {result}")

        if result.get("code") != 0:
            raise FeishuAPIError(result.get("code"), result.get("msg"))

        return result.get("data", {})

    def search_document(self, title: str) -> Optional[Dict]:
        """搜索文档

        Args:
            title: 文档标题

        Returns:
            文档信息字典，如果未找到返回 None
        """
        url = "docx/v1/documents/search"
        payload = {
            "query": title,
            "limit": 10
        }

        try:
            result = self._request("POST", url, json=payload)
            items = result.get("items", [])

            # 精确匹配标题
            for item in items:
                if item.get("title") == title:
                    return {
                        "document_id": item.get("document_id"),
                        "title": item.get("title"),
                        "revision_id": item.get("revision_id")
                    }

            return None
        except FeishuAPIError as e:
            if e.code == 99991400:  # 搜索功能未开通
                print(f"⚠️  警告：文档搜索功能未开通，将创建新文档")
                return None
            raise

    def create_document(self, title: str, blocks: List[Dict] = None) -> Dict:
        """在指定文件夹中创建新文档并写入初始内容

        Args:
            title: 文档标题
            blocks: 初始 block 列表

        Returns:
            创建的文档信息
        """
        url = "docx/v1/documents"

        # 关键修改：加入 folder_token，实现权限继承
        payload = {
            "title": title,
            "folder_token": self.folder_token
        }

        # 1. 创建空文档获取 ID
        result = self._request("POST", url, json=payload)
        document_id = result.get("document", {}).get("document_id")

        print(f"    [DEBUG] 成功在文件夹中创建文档 ID: {document_id}")
        print(f"    [DEBUG] 文件夹 Token: {self.folder_token}")

        # 2. 调用 append_blocks 写入内容
        if blocks and document_id:
            print(f"    [DEBUG] 正在写入初始内容...")
            self.append_blocks(document_id, blocks)

        return {
            "document_id": document_id
        }

    def append_blocks(self, document_id: str, blocks: List[Dict],
                     block_id: str = None) -> Dict:
        """追加内容块到文档（使用最稳定的 children 接口）

        飞书 Docx API 官方推荐接口：
        https://open.feishu.cn/document/server-docs/docs/docs/docx-v1/document-block/children/create

        Args:
            document_id: 文档 ID
            blocks: 要追加的 block 列表
            block_id: 追加位置的 block_id，None 表示追加到文档末尾

        Returns:
            追加结果
        """
        if not blocks:
            return {}

        # 如果 block_id 为空，说明是向文档根节点追加，此时 parent_id 就是 document_id
        parent_id = block_id or document_id
        url = f"docx/v1/documents/{document_id}/blocks/{parent_id}/children"

        # 飞书限制单次最多 50 个 block
        batch_size = 50
        for i in range(0, len(blocks), batch_size):
            batch = blocks[i:i + batch_size]

            # 严格遵守飞书 Docx v1 Schema：{"children": [...]}
            payload = {
                "children": batch
            }

            try:
                self._request("POST", url, json=payload)
                print(f"    [DEBUG] 已同步 {i + len(batch)}/{len(blocks)} 个区块")
            except FeishuAPIError as e:
                print(f"    [ERROR] 写入区块失败: {e.msg}")
                raise

        return {"status": "success"}

    def upload_image(self, image_path: str, parent_type: str = "docx",
                    parent_node: str = None) -> str:
        """上传图片到飞书

        Args:
            image_path: 图片本地路径
            parent_type: 父节点类型，默认 "docx"
            parent_node: 父节点 ID

        Returns:
            file_token
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"图片文件不存在: {image_path}")

        # 读取图片文件
        with open(image_path, 'rb') as f:
            image_data = f.read()

        # 计算文件大小和哈希
        file_size = len(image_data)
        file_hash = hashlib.sha256(image_data).hexdigest()

        # 分片上传
        url = "drive/v1/medias/upload_all"
        headers = {
            "Content-Type": "application/octet-stream"
        }
        params = {
            "parent_type": parent_type,
            "file_name": os.path.basename(image_path),
            "file_size": file_size,
            "file_hash": file_hash
        }

        if parent_node:
            params["parent_node"] = parent_node

        result = self._request("POST", url, data=image_data,
                             headers=headers, params=params)

        return result.get("file_token")

    def get_document_url(self, document_id: str) -> str:
        """获取文档访问链接

        Args:
            document_id: 文档 ID

        Returns:
            文档 URL
        """
        return f"https://feishu.cn/docx/{document_id}"


class MarkdownParser:
    """Markdown 解析器，将 Markdown 转换为飞书 Block 格式"""

    # 根据官方提供的最新映射表完全重写
    FEISHU_LANG_MAP = {
        "plaintext": 1, "text": 1, "plain": 1,
        "abap": 2,
        "ada": 3,
        "apache": 4,
        "apex": 5,
        "assembly": 6, "asm": 6,
        "bash": 7, "sh": 7, "shell": 60,  # 官方 7 是 Bash, 60 是 Shell
        "csharp": 8, "c#": 8, "cs": 8,
        "cpp": 9, "c++": 9,
        "c": 10,
        "cobol": 11,
        "css": 12, "scss": 55, "less": 12,  # CSS 相关
        "coffeescript": 13, "coffee": 13,
        "d": 14,
        "dart": 15,
        "delphi": 16,
        "django": 17,
        "dockerfile": 18, "docker": 18,
        "erlang": 19,
        "fortran": 20,
        "foxpro": 21,
        "go": 22, "golang": 22,
        "groovy": 23,
        "html": 24,
        "htmlbars": 25,
        "http": 26,
        "haskell": 27,
        "json": 28,  # ✅ 关键修复：从 34 改为 28
        "java": 29,
        "javascript": 30, "js": 30,
        "julia": 31,
        "kotlin": 32,
        "latex": 33,
        "lisp": 34,
        "logo": 35,
        "lua": 36,
        "matlab": 37,
        "makefile": 38, "make": 38,
        "markdown": 39, "md": 39,
        "nginx": 40,
        "objectivec": 41, "objc": 41, "objective-c": 41,
        "openedgeabl": 42,
        "php": 43,
        "perl": 44,
        "postscript": 45,
        "powershell": 46, "ps1": 46, "pwsh": 46,
        "prolog": 47,
        "protobuf": 48, "proto": 48,
        "python": 49, "py": 49,  # ✅ 关键修复：从 13 改为 49
        "r": 50,
        "rpg": 51,
        "ruby": 52,
        "rust": 53,  # ✅ 关键修复：从 16 改为 53
        "sas": 54,
        "scala": 57,
        "scheme": 58,
        "scratch": 59,
        "swift": 61,
        "thrift": 62,
        "typescript": 63, "ts": 63,  # ✅ 关键修复：从 23 改为 63
        "vbscript": 64,
        "visualbasic": 65, "vb": 65,
        "xml": 66,
        "yaml": 67, "yml": 67,  # ✅ 关键修复：从 35 改为 67
        "cmake": 68,
        "diff": 69,
        "gherkin": 70,
        "graphql": 71,
        "opengl": 72,
        "properties": 73, "ini": 73,
        "solidity": 74,
        "toml": 75,
        "mermaid": 32,  # Mermaid - 文本绘图（与 Kotlin 共享 ID 32）
        "sql": 56,  # ✅ 关键修复：从 28 改为 56
        "tsql": 76,  # T-SQL
        "plsql": 77,  # PL/SQL
        "mysql": 78,  # MySQL
    }

    def __init__(self):
        self.image_tokens = {}  # 存储图片路径到 file_token 的映射

    def parse(self, markdown_text: str) -> List[Dict]:
        """解析 Markdown 文本

        Args:
            markdown_text: Markdown 文本

        Returns:
            飞书 Block 列表
        """
        lines = markdown_text.split('\n')
        blocks = []

        i = 0
        while i < len(lines):
            line = lines[i].rstrip()

            # 跳过空行
            if not line:
                i += 1
                continue

            # 解析标题
            if line.startswith('#'):
                blocks.append(self._parse_heading(line))

            # 解析代码块
            elif line.startswith('```'):
                code_block, end_line = self._parse_code_block(lines, i)
                blocks.append(code_block)
                i = end_line
                continue

            # 解析列表
            elif line.startswith('- ') or line.startswith('* '):
                # 检查是否为任务列表 (todo)
                stripped = line.lstrip()
                if stripped.startswith('- [ ] ') or stripped.startswith('- [x] ') or \
                   stripped.startswith('* [ ] ') or stripped.startswith('* [x] '):
                    blocks.append(self._parse_todo_item(line))
                else:
                    blocks.append(self._parse_list_item(line))
            elif line[0].isdigit() and line[1:3] in ['. ', ') ']:
                blocks.append(self._parse_numbered_list_item(line))

            # 解析图片
            elif line.startswith('!['):
                blocks.append(self._parse_image(line))

            # 解析表格（优雅降级为 Markdown 代码块）
            elif line.startswith('|'):
                table_block, lines_consumed = self._parse_table(lines, i)
                blocks.append(table_block)
                i += lines_consumed - 1  # -1 因为循环末尾会 +1
                continue

            # 解析普通段落
            else:
                blocks.append(self._parse_paragraph(line))

            i += 1

        return blocks

    def _parse_heading(self, line: str) -> Dict:
        """解析标题 - 使用正确的 block_type 映射"""
        level = 0
        for char in line:
            if char == '#':
                level += 1
            else:
                break

        text = line[level:].strip()

        # 正确的 Docx v1 block_type 映射
        if level == 1:
            return {
                "block_type": 3,  # heading1
                "heading1": {
                    "elements": [{"text_run": {"content": text}}]
                }
            }
        elif level == 2:
            return {
                "block_type": 4,  # heading2
                "heading2": {
                    "elements": [{"text_run": {"content": text}}]
                }
            }
        else:  # level >= 3
            return {
                "block_type": 5,  # heading3
                "heading3": {
                    "elements": [{"text_run": {"content": text}}]
                }
            }

    def _parse_code_block(self, lines: List[str], start_line: int) -> tuple:
        """
        深度优化代码块解析：

        1. 使用正则精准提取语言标签
        2. 增加内容自动探测逻辑（JSON 对象/数组）
        3. 增强调试输出

        Returns:
            (block_dict, end_line_index)
        """
        first_line = lines[start_line].strip()

        # 使用正则提取 ``` 之后的第一个连续单词
        # 例如: ```json {1-5} -> json
        #      ```sql 数据查询 -> sql
        match = re.search(r'^```\s*([a-zA-Z0-9+#-]+)', first_line)
        lang_str = match.group(1).lower() if match else ""

        # 收集代码内容
        code_lines = []
        i = start_line + 1
        while i < len(lines) and not lines[i].strip().startswith('```'):
            code_lines.append(lines[i])
            i += 1

        code_text = '\n'.join(code_lines)

        # 获取初步的 language ID
        lang_id = self.FEISHU_LANG_MAP.get(lang_str, 1)

        # 自动探测逻辑：如果没标语言或识别为 PlainText，但内容看起来像 JSON
        if not lang_str or lang_id == 1:
            stripped_content = code_text.strip()
            # 探测 JSON 对象
            if stripped_content.startswith('{') and stripped_content.endswith('}'):
                lang_str = "json"
                lang_id = 28  # ✅ 官方 JSON ID 是 28
            # 探测 JSON 数组
            elif stripped_content.startswith('[') and stripped_content.endswith(']'):
                lang_str = "json"
                lang_id = 28  # ✅ 官方 JSON ID 是 28

        # 调试输出（始终显示，方便验证识别是否正确）
        print(f"    [DEBUG] 代码块识别: 标签='{lang_str}', 语言ID={lang_id}")

        return {
            "block_type": 14,  # code
            "code": {
                "style": {
                    "language": lang_id  # 关键：传入正确的整数 ID
                },
                "elements": [{
                    "text_run": {
                        "content": code_text
                    }
                }]
            }
        }, i

    def _parse_list_item(self, line: str) -> Dict:
        """解析无序列表项 - 使用正确的 block_type 12 和 bullet 字段"""
        text = line[2:].strip()
        return {
            "block_type": 12,  # bullet_list
            "bullet": {  # 注意：字段名是 bullet 不是 bullet_list
                "elements": [{
                    "text_run": {
                        "content": text
                    }
                }]
            }
        }

    def _parse_numbered_list_item(self, line: str) -> Dict:
        """解析有序列表项 - 使用正确的 block_type 13 和 ordered 字段"""
        # 找到数字后的位置
        i = 0
        while i < len(line) and line[i].isdigit():
            i += 1
        text = line[i+1:].strip()

        return {
            "block_type": 13,  # ordered_list
            "ordered": {  # 注意：字段名是 ordered 不是 ordered_list
                "elements": [{
                    "text_run": {
                        "content": text
                    }
                }]
            }
        }

    def _parse_todo_item(self, line: str) -> Dict:
        """解析任务列表项 - 使用 block_type 17 和 todo 字段

        支持格式：
        - [ ] 未完成任务
        - [x] 已完成任务
        * [ ] 未完成任务
        * [x] 已完成任务
        """
        stripped = line.lstrip()

        # 提取 checkbox 状态
        if '- [x] ' in stripped or '* [x] ' in stripped:
            checked = True
            # 移除 "- [x] " 或 "* [x] " 前缀
            if '- [x] ' in stripped:
                text = stripped.replace('- [x] ', '', 1).strip()
            else:
                text = stripped.replace('* [x] ', '', 1).strip()
        elif '- [ ] ' in stripped or '* [ ] ' in stripped:
            checked = False
            # 移除 "- [ ] " 或 "* [ ] " 前缀
            if '- [ ] ' in stripped:
                text = stripped.replace('- [ ] ', '', 1).strip()
            else:
                text = stripped.replace('* [ ] ', '', 1).strip()
        else:
            # 如果格式不匹配，降级为普通列表项
            return self._parse_list_item(line)

        return {
            "block_type": 17,  # todo
            "todo": {
                "elements": [{
                    "text_run": {
                        "content": text
                    }
                }],
                "style": {
                    "checked": checked
                }
            }
        }

    def _parse_table(self, lines: List[str], start_line: int) -> tuple:
        """解析表格 - 优雅降级为 Markdown 代码块

        Returns:
            (block_dict, lines_consumed)
        """
        # 收集连续的表格行
        table_lines = []
        i = start_line
        while i < len(lines) and lines[i].startswith('|'):
            table_lines.append(lines[i].rstrip())
            i += 1

        # 将表格转为 Markdown 代码块
        table_text = '\n'.join(table_lines)

        return {
            "block_type": 14,  # code
            "code": {
                "style": {
                    "language": 37  # Markdown - 保持表格格式
                },
                "elements": [{
                    "text_run": {
                        "content": table_text
                    }
                }]
            }
        }, i  # 返回处理到的行数

    def _parse_image(self, line: str) -> Dict:
        """解析图片"""
        # 提取 alt 和路径
        # 格式：![alt](path)
        import re
        match = re.match(r'!\[([^\]]*)\]\(([^\)]+)\)', line)
        if not match:
            return self._parse_paragraph(line)

        alt = match.group(1)
        path = match.group(2)

        # 检查是否已上传
        if path in self.image_tokens:
            file_token = self.image_tokens[path]
        else:
            # 标记需要上传
            file_token = f"UPLOAD_REQUIRED:{path}"

        return {
            "block_type": 15,  # image (Docx v1 正确的 ID)
            "image": {
                "file_token": file_token
            }
        }

    def _parse_paragraph(self, line: str) -> Dict:
        """解析段落"""
        # 解析内联样式：**bold**, *italic*, `code`
        elements = []
        i = 0

        while i < len(line):
            # **bold**
            if line[i:i+2] == '**':
                end = line.find('**', i + 2)
                if end != -1:
                    text = line[i+2:end]
                    elements.append({
                        "text_run": {
                            "content": text,
                            "text_element_style": {
                                "bold": True
                            }
                        }
                    })
                    i = end + 2
                    continue

            # *italic*
            if line[i] == '*':
                end = line.find('*', i + 1)
                if end != -1:
                    text = line[i+1:end]
                    elements.append({
                        "text_run": {
                            "content": text,
                            "text_element_style": {
                                "italic": True
                            }
                        }
                    })
                    i = end + 1
                    continue

            # `code`
            if line[i] == '`':
                end = line.find('`', i + 1)
                if end != -1:
                    text = line[i+1:end]
                    elements.append({
                        "text_run": {
                            "content": text,
                            "text_element_style": {
                                "code": True
                            }
                        }
                    })
                    i = end + 1
                    continue

            # 普通文本
            end = len(line)
            for marker in ['**', '*', '`']:
                pos = line.find(marker, i)
                if pos != -1 and pos < end:
                    end = pos

            if end > i:
                elements.append({
                    "text_run": {
                        "content": line[i:end]
                    }
                })
                i = end

        return {
            "block_type": 2,  # text (修复：2 而不是 1)
            "text": {  # ← 修复：使用 text 而不是 paragraph
                "elements": elements
            }
        }


class FeishuDocWriter:
    """飞书文档写入器"""

    def __init__(self):
        self.client = FeishuAPIClient()
        self.parser = MarkdownParser()

    def write(self, markdown_text: str, title: str,
             image_dir: str = None, preview: bool = False,
             render_mermaid: bool = False) -> str:
        """写入文档到飞书

        Args:
            markdown_text: Markdown 文本
            title: 文档标题
            image_dir: 图片目录
            preview: 是否预览模式
            render_mermaid: 是否渲染 Mermaid 图表

        Returns:
            document_id
        """
        # 1. 解析 Markdown
        print("📝 正在解析 Markdown...")
        blocks = self.parser.parse(markdown_text)

        # 2. 处理 Mermaid 图表
        if render_mermaid:
            print("🎨 正在渲染 Mermaid 图表...")
            blocks = self._process_mermaid(blocks)

        # 3. 上传图片
        if image_dir:
            print("📷 正在上传图片...")
            blocks = self._upload_images(blocks, image_dir)

        # 4. 预览模式
        if preview:
            self._preview_blocks(title, blocks)
            confirm = input("\n是否确认写入？[y/N]: ")
            if confirm.lower() != 'y':
                print("❌ 已取消")
                sys.exit(0)

        # 5. 搜索现有文档（如果搜索功能不可用，直接创建新文档）
        print("🔍 正在搜索现有文档...")
        try:
            existing_doc = self.client.search_document(title)

            if existing_doc:
                print(f"✓ 找到现有文档: {existing_doc['document_id']}")
                document_id = existing_doc['document_id']
                operation = "append"
            else:
                print("✓ 未找到文档，将创建新文档")
                document_id = None
                operation = "create"
        except Exception as e:
            print(f"⚠️  搜索功能不可用: {e}")
            print("✓ 将创建新文档")
            document_id = None
            operation = "create"

        # 6. 分批写入
        print(f"📝 正在写入内容 (共 {len(blocks)} 个 blocks)...")
        document_id = self._write_in_batches(document_id, title, blocks, operation)

        print(f"\n✅ 同步完成！")
        print(f"文档标题: {title}")
        print(f"文档ID: {document_id}")
        print(f"访问链接: {self.client.get_document_url(document_id)}")

        return document_id

    def _process_mermaid(self, blocks: List[Dict]) -> List[Dict]:
        """处理 Mermaid 代码块

        将 Mermaid 代码渲染为图片并替换
        """
        # 检查是否安装了 mermaid 渲染器
        try:
            from .mermaid_renderer import MermaidRenderer
            renderer = MermaidRenderer()
        except ImportError:
            print("⚠️  警告：未找到 mermaid_renderer.py，跳过 Mermaid 渲染")
            return blocks

        processed_blocks = []
        for block in blocks:
            if block.get("block_type") == 14:  # code block (Docx v1 正确的 ID)
                code_data = block.get("code", {})
                # 检查 language 是否为 mermaid (language ID 32)
                language_id = code_data.get("style", {}).get("language", 1)

                if language_id == 32:  # 32 = Mermaid
                    code = code_data.get("elements", [{}])[0].get("text_run", {}).get("content", "")

                    # 渲染为图片
                    temp_image = f"temp_mermaid_{hash(code)}.png"
                    try:
                        renderer.render(code, temp_image)

                        # 替换为图片 block (Docx v1 正确的 ID)
                        processed_blocks.append({
                            "block_type": 15,  # image (从 25 改为 15)
                            "image": {
                                "file_token": f"UPLOAD_REQUIRED:{temp_image}"
                            }
                        })
                        print(f"✓ 已渲染 Mermaid 图表")
                    except Exception as e:
                        print(f"⚠️  渲染失败: {e}")
                        # 保留原代码块
                        processed_blocks.append(block)

                    continue

            processed_blocks.append(block)

        return processed_blocks

    def _upload_images(self, blocks: List[Dict], image_dir: str) -> List[Dict]:
        """上传所有需要上传的图片

        Args:
            blocks: block 列表
            image_dir: 图片基础目录

        Returns:
            更新后的 block 列表
        """
        image_dir = Path(image_dir)

        for block in blocks:
            if block.get("block_type") == 25:  # image
                file_token = block.get("image", {}).get("file_token", "")

                if file_token.startswith("UPLOAD_REQUIRED:"):
                    # 提取图片路径
                    image_path = file_token.replace("UPLOAD_REQUIRED:", "")

                    # 处理相对路径
                    if not os.path.isabs(image_path):
                        image_path = image_dir / image_path

                    # 上传图片
                    try:
                        print(f"  上传: {os.path.basename(image_path)}")
                        token = self.client.upload_image(str(image_path))
                        block["image"]["file_token"] = token
                        print(f"    ✓ 完成")
                    except Exception as e:
                        print(f"    ✗ 失败: {e}")
                        # 替换为错误提示文本
                        block["block_type"] = 1  # paragraph
                        block["paragraph"] = {
                            "elements": [{
                                "text_run": {
                                    "content": f"[图片上传失败: {image_path}]"
                                }
                            }]
                        }

        return blocks

    def _preview_blocks(self, title: str, blocks: List[Dict]):
        """预览块结构"""
        block_type_names = {
            1: "paragraph",
            2: "heading1",
            3: "bulleted_list",
            4: "heading2",
            6: "heading3",
            8: "code",
            11: "ordered_list",
            25: "image"
        }

        # 统计块类型
        type_counts = {}
        for block in blocks:
            block_type = block.get("block_type", 0)
            type_name = block_type_names.get(block_type, f"unknown({block_type})")
            type_counts[type_name] = type_counts.get(type_name, 0) + 1

        # 计算批次数
        batch_count = (len(blocks) + 49) // 50

        print("\n" + "="*50)
        print("即将写入的内容结构")
        print("="*50)
        print(f"标题: {title}")
        print(f"总块数: {len(blocks)}")
        print(f"批次数: {batch_count}")
        print(f"\n块类型分布:")
        for type_name, count in sorted(type_counts.items()):
            print(f"  - {type_name}: {count}")

    def _write_in_batches(self, document_id: str, title: str,
                         blocks: List[Dict], operation: str):
        """分批写入文档

        Args:
            document_id: 文档 ID（创建时为 None）
            title: 文档标题
            blocks: block 列表
            operation: 操作类型 "create" 或 "append"
        """
        batch_size = 50
        total_batches = (len(blocks) + batch_size - 1) // batch_size

        for i in range(0, len(blocks), batch_size):
            batch_num = i // batch_size + 1
            batch = blocks[i:i + batch_size]

            print(f"  正在写入第 {batch_num}/{total_batches} 批...")

            try:
                if operation == "create" and batch_num == 1:
                    # 第一批：创建文档
                    result = self.client.create_document(title, batch)
                    document_id = result["document_id"]
                    # 获取完整的 revision_id
                    revision_id = result.get("revision_id")
                else:
                    # 后续批次或追加模式
                    self.client.append_blocks(document_id, batch)

                print(f"    ✓ 第 {batch_num} 批完成")

            except FeishuAPIError as e:
                print(f"    ✗ 第 {batch_num} 批失败: {e}")
                if document_id:
                    print(f"\n已保存 document_id: {document_id}")
                    print(f"可以稍后重新运行以继续写入")
                sys.exit(1)

        return document_id


def main():
    """命令行入口"""
    import argparse

    parser = argparse.ArgumentParser(description="飞书文档同步工具")
    parser.add_argument("--text", help="纯文本内容")
    parser.add_argument("--markdown", help="Markdown 文件路径")
    parser.add_argument("--title", required=True, help="文档标题")
    parser.add_argument("--image-dir", help="图片目录")
    parser.add_argument("--preview", action="store_true", help="预览模式")
    parser.add_argument("--render-mermaid", action="store_true",
                       help="渲染 Mermaid 图表")
    parser.add_argument("--document-id", help="指定文档ID（追加模式）")

    args = parser.parse_args()

    # 读取内容
    if args.markdown:
        with open(args.markdown, 'r', encoding='utf-8') as f:
            markdown_text = f.read()
    elif args.text:
        markdown_text = args.text
    else:
        print("❌ 错误：请指定 --text 或 --markdown")
        sys.exit(1)

    # 写入文档
    writer = FeishuDocWriter()
    writer.write(
        markdown_text=markdown_text,
        title=args.title,
        image_dir=args.image_dir,
        preview=args.preview,
        render_mermaid=args.render_mermaid
    )


if __name__ == "__main__":
    main()
