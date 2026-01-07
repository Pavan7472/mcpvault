import typer
import asyncio
from .vault import manager
from .server import mcp

app = typer.Typer()

@app.command()
def install(
    force: bool = typer.Option(False, "--force", "-f", help="Force install even if only 1 MCP exists.")
):
    """Installs mcpv and sets the CURRENT directory as the target."""
    print("🛡️  Installing MCP Vault...")
    manager.install(force=force)

@app.command()
def link():
    """[Safe Switch] Updates the Vault to target the CURRENT directory."""
    print("🔗 Linking Vault to current directory...")
    manager.link()

@app.command()
def start():
    """Starts the mcpv server (Used by Antigravity)."""
    try:
        mcp.run()
    except KeyboardInterrupt:
        pass
    finally:
        asyncio.run(manager.cleanup())

if __name__ == "__main__":
    app()