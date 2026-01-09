Hi everyone,
I've been using AI Agents (specifically Antigravity) heavily for coding, but I ran into three major frustrations that I think many of you might recognize:
Infinite Loading: Without GPU, Antigravity went too slow. In my case it went 58s unresponsive per 1 min. 
Context Bloat: The agent keeps requesting the full codebase context repeatedly whenever it loads MCP's, making my MCP servers unresponsive.
Agent/UI Lag: On Windows, the agent responses kept saying "Continue" repeatedly because of 1, 2.
I couldn't find a tool that solved all of this, so I built MCP Vault (mcpv).
🔗 Repo:https://github.com/thekeunpie-hash/mcpvault (MIT Licensed)
🚀 What does it do?
It acts as a "Smart Middleware" between your Agent and your actual tools. It hijacks the mcp_config.json safely and optimizes the traffic.(All of MCPs will be kept exactly identically on C:\Users\[Username]\.gemini\antigravity\mcp_config.original.json)
1. Zero-Latency Startup (Lazy Loading) Instead of scanning files at boot, mcpv starts instantly (<0.1s). It only scans directories when the agent actually requests them. No timeouts on large repos.
2. Smart Context Valve It detects if the agent asks for a massive context dump (like a full repo summary) more than once in a session.
First request: Allowed (Full context provided).
Subsequent requests: Blocked with a "Context already cached" message (only ~20 tokens used). This physically prevents the agent from wasting tokens on duplicate data.
[System Instruction]


Session Start: At the very beginning of the conversation, you MUST call get_initial_context tool immediately. This is your only way to understand the project structure.


Context Management: Do NOT call get_initial_context again in the same session unless the user explicitly asks for a "refresh" with force=True. The proxy will block redundant requests.


File Access: After reading the initial context map, use read_file to inspect specific files needed for the task.
This Antigravity rule needs to be added though.

3. Booster Injection (Windows/Antigravity) It auto-generates an optimized launcher script that:
Forces GPU rasterization & zero-copy flags.
Drops Admin rights (fixes drag-and-drop & UI bugs).
Kills zombie processes on port 26646 automatically.
The shortcut with injected script can be found on the desktop after installation.
🛠️ Tech Stack
Python & uv: Uses uv for clean, isolated virtual environments to prevent dependency hell.
FastMCP: Built on top of the FastMCP framework for speed.
Gateway Pattern: It backs up your original config and routes traffic through the proxy securely.
📦 Installation
It's available on PyPI too.
Bash
pip install mcpv
mcpv install
Currently, it's optimized for Windows and Antigravity, but the core logic (Lazy Loading/Smart Valve) is applicable to any MCP-compliant agent.
I'd love to hear your feedback or feature requests!
