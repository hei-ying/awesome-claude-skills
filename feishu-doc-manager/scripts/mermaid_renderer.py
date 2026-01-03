#!/usr/bin/env python3
"""
Mermaid 图表渲染器
将 Mermaid 语法渲染为 PNG 图片
"""

import os
import sys
import subprocess
import tempfile
from pathlib import Path


class MermaidRenderer:
    """Mermaid 图表渲染器"""

    def __init__(self, method="auto"):
        """
        初始化渲染器

        Args:
            method: 渲染方法 "auto", "cli", 或 "puppeteer"
                   - auto: 自动选择可用方法
                   - cli: 使用 mermaid-cli
                   - puppeteer: 使用 pyppeteer
        """
        self.method = method
        self.available_methods = []

        # 检测可用的渲染方法
        self._detect_methods()

    def _detect_methods(self):
        """检测系统中可用的渲染方法"""
        # 检查 mermaid-cli
        try:
            result = subprocess.run(
                ["mmdc", "--version"],
                capture_output=True,
                timeout=5
            )
            if result.returncode == 0:
                self.available_methods.append("cli")
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

        # 检查 pyppeteer
        try:
            import pyppeteer
            self.available_methods.append("puppeteer")
        except ImportError:
            pass

        if not self.available_methods:
            print("❌ 错误：未找到 Mermaid 渲染工具")
            print("\n请安装以下任一工具：")
            print("1. mermaid-cli（推荐）:")
            print("   npm install -g @mermaid-js/mermaid-cli")
            print("\n2. pyppeteer:")
            print("   pip install pyppeteer")
            sys.exit(1)

    def render(self, mermaid_code: str, output_path: str) -> str:
        """
        渲染 Mermaid 代码为 PNG

        Args:
            mermaid_code: Mermaid 图表代码
            output_path: 输出 PNG 文件路径

        Returns:
            输出文件的绝对路径
        """
        # 选择渲染方法
        method = self._select_method()

        # 根据方法渲染
        if method == "cli":
            return self._render_with_cli(mermaid_code, output_path)
        elif method == "puppeteer":
            return self._render_with_puppeteer(mermaid_code, output_path)
        else:
            raise ValueError(f"不支持的渲染方法: {method}")

    def _select_method(self) -> str:
        """选择渲染方法"""
        if self.method == "auto":
            # 优先使用 cli（更快更稳定）
            if "cli" in self.available_methods:
                return "cli"
            elif "puppeteer" in self.available_methods:
                return "puppeteer"
            else:
                raise RuntimeError("没有可用的渲染方法")
        else:
            if self.method in self.available_methods:
                return self.method
            else:
                print(f"❌ 错误：指定的方法 '{self.method}' 不可用")
                print(f"可用方法: {', '.join(self.available_methods)}")
                sys.exit(1)

    def _render_with_cli(self, mermaid_code: str, output_path: str) -> str:
        """
        使用 mermaid-cli 渲染

        Args:
            mermaid_code: Mermaid 代码
            output_path: 输出路径

        Returns:
            输出文件路径
        """
        # 创建临时文件
        with tempfile.NamedTemporaryFile(
            mode='w',
            suffix='.mmd',
            delete=False,
            encoding='utf-8'
        ) as f:
            f.write(mermaid_code)
            input_file = f.name

        try:
            # 调用 mmdc 命令
            output_abs_path = os.path.abspath(output_path)
            input_dir = os.path.dirname(input_file)

            cmd = [
                "mmdc",
                "-i", input_file,
                "-o", output_abs_path,
                "-b", "transparent",  # 透明背景
                "-s", "2"  # scale 2x 提高清晰度
            ]

            result = subprocess.run(
                cmd,
                capture_output=True,
                timeout=30,
                cwd=input_dir
            )

            if result.returncode != 0:
                error_msg = result.stderr.decode('utf-8', errors='ignore')
                raise RuntimeError(f"mermaid-cli 渲染失败: {error_msg}")

            return output_abs_path

        finally:
            # 清理临时文件
            if os.path.exists(input_file):
                os.unlink(input_file)

    def _render_with_puppeteer(self, mermaid_code: str, output_path: str) -> str:
        """
        使用 pyppeteer 渲染

        Args:
            mermaid_code: Mermaid 代码
            output_path: 输出路径

        Returns:
            输出文件路径
        """
        try:
            import pyppeteer
        except ImportError:
            print("❌ 错误：未安装 pyppeteer")
            print("\n请运行: pip install pyppeteer")
            sys.exit(1)

        # 创建临时 HTML 文件
        html_content = self._generate_html(mermaid_code)

        with tempfile.NamedTemporaryFile(
            mode='w',
            suffix='.html',
            delete=False,
            encoding='utf-8'
        ) as f:
            f.write(html_content)
            html_file = f.name

        try:
            # 使用 pyppeteer 渲染
            output_abs_path = os.path.abspath(output_path)

            # 异步渲染函数
            async def render_page():
                browser = await pyppeteer.launch(headless=True)
                page = await browser.newPage()

                # 设置视口大小
                await page.setViewport(viewport={'width': 1200, 'height': 800})

                # 加载 HTML
                html_url = f'file://{html_file}'
                await page.goto(html_url)

                # 等待图表渲染
                await page.waitForSelector('.mermaid', timeout=10000)

                # 截图
                mermaid_element = await page.querySelector('.mermaid')
                await mermaid_element.screenshot({'path': output_abs_path})

                await browser.close()

            # 运行异步函数
            import asyncio
            asyncio.get_event_loop().run_until_complete(render_page())

            return output_abs_path

        finally:
            # 清理临时文件
            if os.path.exists(html_file):
                os.unlink(html_file)

    def _generate_html(self, mermaid_code: str) -> str:
        """
        生成包含 Mermaid 图表的 HTML

        Args:
            mermaid_code: Mermaid 代码

        Returns:
            HTML 内容
        """
        return f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {{
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }}
        .mermaid {{
            width: 100%;
        }}
    </style>
</head>
<body>
    <div class="mermaid">
{mermaid_code}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <script>
        mermaid.initialize({{
            startOnLoad: true,
            theme: 'default',
            securityLevel: 'loose'
        }});
    </script>
</body>
</html>
"""

    def render_from_file(self, input_file: str, output_path: str) -> str:
        """
        从文件读取 Mermaid 代码并渲染

        Args:
            input_file: 输入文件路径
            output_path: 输出 PNG 路径

        Returns:
            输出文件路径
        """
        with open(input_file, 'r', encoding='utf-8') as f:
            mermaid_code = f.read()

        return self.render(mermaid_code, output_path)


def main():
    """命令行入口"""
    import argparse

    parser = argparse.ArgumentParser(description="Mermaid 图表渲染工具")
    parser.add_argument("input", help="Mermaid 代码或文件路径")
    parser.add_argument("output", help="输出 PNG 文件路径")
    parser.add_argument("-f", "--file", action="store_true",
                       help="输入为文件路径")
    parser.add_argument("-m", "--method", choices=["auto", "cli", "puppeteer"],
                       default="auto", help="渲染方法（默认: auto）")

    args = parser.parse_args()

    # 创建渲染器
    renderer = MermaidRenderer(method=args.method)

    try:
        # 渲染
        if args.file:
            output_path = renderer.render_from_file(args.input, args.output)
        else:
            output_path = renderer.render(args.input, args.output)

        print(f"✓ 渲染成功: {output_path}")

    except Exception as e:
        print(f"✗ 渲染失败: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
