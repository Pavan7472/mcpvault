# ⚡ MCP Vault (`mcpv`)

> **AI 代理 (AI Agents) 的终极性能加速器**  
> _"系统延迟减少 99%，加载时间归零，Token 成本降低 90%。"_

<div align="center">

![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-F7CA3F.svg?style=flat-square&logo=python&logoColor=black)
![Platform](https://img.shields.io/badge/OS-Windows-0078D6.svg?style=flat-square&logo=windows&logoColor=white)
![Status](https://img.shields.io/badge/Status-Accelerated-brightgreen.svg?style=flat-square)

</div>

<div align="right">
  <a href="README.md">🇺🇸 English</a> | <a href="README_KR.md">🇰🇷 한국어</a> | <a href="README_RU.md">🇷🇺 Русский</a>
</div>

<br>

> [!CAUTION]
> **⚠️ 兼容性警告 (Compatibility Warning)**<br>
> 目前本项目仅支持 **Windows** 操作系统和 **Antigravity** 代理环境。

<br>

## ❓ 为什么选择 `mcpv`？

在使用 AI 代理（Antigravity, Cursor）时，你是否有过这样的体验？
> *"为什么这么卡？"*  
> *"又卡死了..."*  
> *"为什么 Token 费用这么高？"*

`mcpv` 不仅仅是一个工具。它是你代理的 **涡轮引擎 (Turbo Engine)**。

<br>

### 🏎️ 压倒性的性能差异

| 功能 | 😫 没有 `mcpv` (Before) | ⚡ 安装 `mcpv` (After) | 📈 效果 |
| :--- | :--- | :--- | :--- |
| **速度** | 无 GPU 加速，UI 卡顿 | **强制 GPU 加速，流畅** | **100倍** 体感提升 |
| **加载** | 每次等待 10秒+ | **0.1秒 瞬间启动** (Lazy Load) | **零** 等待 |
| **成本** | 每次发送全部代码 | **自动拦截重复项** (Smart Cache) | **90%** 节省 |

<br>

---

## ✨ 3大核心功能

### 1️⃣ Booster Injection (物理加速)
**"一行命令解锁硬件限制"**
- **强制激活 GPU**: 注入隐藏的渲染加速标志 (`--enable-gpu-rasterization`)。
- **绕过权限问题**: 放弃管理员权限以修复拖放和 UI 错误，并使用 `RunAsInvoker` 绕过烦人的管理员权限请求 (Error 740)。
- **僵尸进程杀手**: 自动清理占用端口的幽灵进程。

### 2️⃣ Smart Valve (成本防御)
**"为你省钱的智能钱包卫士"**
- 检测代理习惯性请求的巨大上下文数据 (`repomix`)。
- **首次请求：允许**（提供完整上下文）。
- **后续请求：拦截**（仅回复 10 Token 的 **“已缓存”** 消息）。
- 物理阻断意外的 Token 炸弹。

### 3️⃣ Gateway Hijacking (安全金库)
**"不再为复杂的配置烦恼"**
- **零延迟启动**：仅在代理实际请求时扫描目录。大代码库也不会超时。
- 自动将现有的复杂 MCP 设置迁移到安全的金库 (Vault)。
- 原始配置安全备份至 `mcp_config.original.json`。
- 代理只与 `mcpv` 对话，但所有工具在后台都能完美运行。

<br>

---

## 🛠️ 经过验证的推荐设置 (Verified Setup)

开发者亲测的 MCP 服务器配置。与其一起使用时，`mcpv` 能发挥最佳协同效应。

```json
{
  "mcpServers": {
    "rube": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://rube.app/mcp"]
    },
    "open-aware": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://open-aware.qodo.ai/mcp"]
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp", "--api-key", "PUT_IN_YOUR_API_KEY_HERE"]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "mcp-server-neon": {
      "disabled": false,
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.neon.tech/sse"],
      "env": {
        "NEON_API_KEY": "NEVERCHANGE_DONT_PUT_IN_ANYTHING_ELSE_THAN_ME_HERE"
      }
    }
  }
}
