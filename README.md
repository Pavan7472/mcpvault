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
  <a href="README_KR.md">🇰🇷 한국어</a> | <a href="README_CN.md">🇨🇳 中文</a>
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
- **Permission Bypass**: Bypasses annoying admin permission requests (Error 740) using `RunAsInvoker`.
- **Zombie Process Killer**: Automatically cleans up ghost processes occupying ports.

### 2️⃣ Smart Valve (Cost Defense)
**"Smart wallet protector that saves for you"**
- Detects the massive context data (`repomix`) that agents habitually request.
- **Sends only the first time**, and replies with a 10-token **"Already cached"** message from the second time onwards.
- Physically blocks accidental token bombs.

### 3️⃣ Gateway Hijacking (Secure Vault)
**"Stop struggling with complex configs"**
- Automatically migrates existing complex MCP settings to a secure Vault.
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
```

<br>

---

## 📦 Installation

Choose the method that fits your needs.

### Option A: The "It Just Works" Method (Recommended for most users)
If you have Python installed and added to PATH.

```powershell
# 1. Install from PyPI
pip install mcpv

# 2. Setup Gateway & Booster
mcpv install

# 3. Done! 
# Look for the "Antigravity Boost (mcpv)" shortcut on your Desktop.

```

---

### Option B: The "Rock-Solid" Method (Using `uv`)

Use this method if your Python environment is messy or you want complete isolation.

#### 1. Clean up existing processes

```powershell
Stop-Process -Name "mcpv" -Force -ErrorAction SilentlyContinue
Stop-Process -Name "python" -Force -ErrorAction SilentlyContinue

```

#### 2. Create Virtual Environment & Install

```powershell
# Install uv (if needed)
powershell -ExecutionPolicy ByPass -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"

# Create .venv and install mcpv
uv venv
uv pip install mcpv

```

#### 3. Register & Lock

This registers the **isolated virtual environment** into Antigravity's config.

```powershell
.venv\Scripts\python -m mcpv install --force

```

#### 4. Run

Launch **`Antigravity Boost (mcpv)`** from your Desktop.

---

## 🛠️ Commands

| Command | Description |
| --- | --- |
| `mcpv install` | Installs the gateway and creates the Desktop shortcut. |
| `mcpv install --force` | Forces installation even if only 1 MCP server exists. |
| `mcpv start` | Starts the server (Used internally by Antigravity). |
| `mcpv link` | Updates the Vault to target the current directory as the project root. |
| `mcpv --help` | Show help message. |

---

## ❓ Troubleshooting

#### Q. "File access denied" or "Failed to remove file" during update?

This means `mcpv.exe` or `Antigravity` is still running.

1. Close Antigravity.
2. Run: `Stop-Process -Name "mcpv" -Force` in PowerShell.
3. Try installing again.

#### Q. I installed it, but I don't see the Shortcut.

The shortcut is created on your **Desktop**. If not, check the installation logs. You can create it manually by running `mcpv install` again.

---

## 📜 License

MIT License. Feel free to fork and modify!

---

☕ **Support**  
If this project helped you save tokens and time, consider buying me a coffee!  

[<img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" width="180" />](https://www.buymeacoffee.com/mcpv)

<br>

---

<div align="center">
  <b>⚡ Charged by MCP Vault</b><br>
  <i>Developed for High-Performance AI Agent Operations</i>
</div>
