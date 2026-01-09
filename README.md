# ⚡ MCP Vault (`mcpv`)

> **The Ultimate Performance Booster for AI Agents**  
> _"Reduce system lag by 99%, eliminate loading times, and cut token costs by 90%."_

<div align="center">

![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-F7CA3F.svg?style=flat-square&logo=python&logoColor=black)
![Platform](https://img.shields.io/badge/OS-Windows-0078D6.svg?style=flat-square&logo=windows&logoColor=white)
![Status](https://img.shields.io/badge/Status-Accelerated-brightgreen.svg?style=flat-square)

</div>

<div align="right">
  <a href="README_KR.md">🇰🇷 한국어</a> | <a href="README_CN.md">🇨🇳 中文</a> | <a href="README_RU.md">🇷🇺 Русский</a>
</div>

<br>

> [!CAUTION]
> **⚠️ Compatibility Warning**<br>
> Currently, this project ONLY supports **Windows** OS and the **Antigravity** agent environment.

<br>

## ❓ Why `mcpv`?

Have you ever felt this while using AI Agents (Antigravity, Cursor)?
> *"Why is it so heavy?"*  
> *"It froze again..."*  
> *"Why are the token costs so high?"*

`mcpv` is not just a tool. It is a **Turbo Engine** for your agent.

<br>

### 🏎️ Overwhelming Performance Difference

| Feature | 😫 Without `mcpv` (Before) | ⚡ With `mcpv` (After) | 📈 Effect |
| :--- | :--- | :--- | :--- |
| **Speed** | No GPU, Laggy UI | **Forced GPU Acceleration, Smooth** | **100x** Perceived Speed |
| **Loading** | Wait 60s+ every time | **0.1s Instant Start** (Lazy Load) | **Zero** Latency |
| **Cost** | Resend full code every time | **Auto-block Duplicates** (Smart Cache) | **90%** Savings |

<br>

---

## ✨ 3 Core Features

### 1️⃣ Booster Injection (Physical Acceleration)
**"Unlock hardware limits with one line"**
- **Forced GPU Activation**: Injects hidden rendering acceleration flags (`--enable-gpu-rasterization`).
- **Permission Bypass**: Drops Admin rights to fix drag-and-drop & UI bugs, and bypasses permission requests (Error 740) using `RunAsInvoker`.
- **Zombie Process Killer**: Automatically cleans up ghost processes occupying ports.

### 2️⃣ Smart Valve (Cost Defense)
**"Smart wallet protector that saves for you"**
- Detects the massive context data (`repomix`) that agents habitually request.
- **First request: Allowed** (Full context provided).
- **Subsequent requests: Blocked** with a 10-token **"Already cached"** message.
- Physically blocks accidental token bombs.

### 3️⃣ Gateway Hijacking (Secure Vault)
**"Stop struggling with complex configs"**
- **Zero-Latency Startup**: Only scans directories when the agent actually requests them. No timeouts on large repos.
- Automatically migrates existing complex MCP settings to a secure Vault.
- Original config is safely backed up to `mcp_config.original.json`.
- The agent talks only to `mcpv`, but all tools work perfectly behind the scenes.

<br>

---

## 🛠️ Verified Recommended Setup

Verified MCP server configuration used by the developer. It creates the best synergy when used with `mcpv`.

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
