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
- **Root Path Locking**: Captures the directory where you run `mcpv install` and forces the agent to ALWAYS see that directory as the project root. No more "File not found" errors when the agent drifts to other folders.
- Automatically migrates existing complex MCP settings to a secure Vault.
- Original config is safely backed up to `mcp_config.original.json`.

### 4️⃣ Smart Router (Flattened Execution)
**"One Tool to Rule Them All"**
- **Unified Interface**: The agent doesn't need to know which server has which tool. It just calls `run_tool(name="...")`.
- **Auto-Correction**: Did the agent make a typo? Did it try to call a server name? `mcpv` automatically finds the correct tool or suggests the right name.
- **Zero-Latency Startup**: Only connects to upstream servers when their tools are actually needed.

<br>

---

## 📦 Installation

This project is optimized for **Windows**. We recommend using `uv` for a fast and clean installation.

```powershell
# Install using uv (Recommended)
uv pip install . --system

# OR using standard pip
pip install .
```

After installing the package, **you must run the install command** to configure the vault:

```powershell
mcpv install
```

<br>

---

## 💻 Commands

| Command | Description |
| :--- | :--- |
| `mcpv install` | **(Essential)** Installs `mcpv` as the primary gateway, migrates existing config, and **locks the current directory** as the project root. |
| `mcpv install --force` | Overwrites existing `mcpv` installation if found. |
| `mcpv start` | **(Internal)** Starts the MCP server. Used by the Antigravity agent, not for humans. |

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

<br>

---


<br>

---

## ❓ Troubleshooting & FAQ

If you encounter issues, please check the specific solutions below.

### 1. ❌ "Permission Denied" during Installation
**Error Example:**
> `❌ PERMISSION DENIED: Cannot create config directory`  
> `❌ PERMISSION DENIED: Cannot save root path`

**Solution:**
Windows prevents regular users from writing to protected paths.
1. Right-click your terminal (Command Prompt or PowerShell).
2. Select **"Run as Administrator"**.
3. Run `mcpv install` again.

**Verification Command:**
```powershell
# Check if you have write access (should return 'True' if Admin)
[bool](([System.Security.Principal.WindowsIdentity]::GetCurrent()).Groups -match "S-1-5-32-544")
```

<br>

### 2. ⚠️ "Running as Administrator detected" (Booster Warning)
**Warning Message:**
> `[WARNING] Running as Administrator detected!`  
> `Antigravity running as Admin may cause UI glitches...`

**Solution:**
- **Do NOT** run the booster script manually from an Admin terminal.
- Use the **Desktop Shortcut** created by `mcpv` (`Antigravity Boost (mcpv)`).
- If the shortcut still triggers the warning, right-click the shortcut → Properties → Compatibility → Uncheck "Run this program as an administrator".

**Verification Command:**
```powershell
# If this returns a value, you are Admin (Try to run as Standard User instead)
net session
```

<br>

### 3. ⚠️ "Corrupted Config File"
**Error Example:**
> `⚠️ WARNING: Corrupted config file found`

**Solution:**
Your `mcp_config.json` file contains invalid JSON syntax.
- **Option A (Reset)**: Run `mcpv install --force` to completely wipe and reset the configuration.
- **Option B (Manual Fix)**: Open `%HOMEPATH%\.gemini\antigravity\mcp_config.json` and fix the syntax errors.

<br>

### 4. ⚠️ "Existing MCP Servers Found"
**Message:**
> `⚠️ EXISTING MCP SERVERS FOUND: ...`

**Solution:**
`mcpv` tries to protect your existing work.
- Run `mcpv install --force` to proceed.
- `mcpv` will automatically **backup** your old configuration to `mcp_config.original.json` before overwriting it.

<br>

### 5. ❌ "exec: npx: executable file not found"
**Cause:**
The Agent cannot find Node.js (`npx`) in your system PATH.

**Solution:**
1. Ensure **Node.js** is installed.
2. **ALWAYS** start Antigravity using the **Booster Shortcut** (`Antigravity Boost (mcpv)`).
   - The booster script automatically injects the correct PATH for `npx` before launching the application.

**Verification Commands:**
Run these in PowerShell to check your environment:
```powershell
# 1. Check Node.js version (Must be v18+)
node -v

# 2. Check NPM version
npm -v

# 3. Check if npx is in PATH
Get-Command npx
```
If any of these fail, you must install **Node.js LTS** from [nodejs.org](https://nodejs.org).
