import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
	name="execute-shell-mcp",
	description="MCP Server for executing shell commands.",
)

@mcp.tool(name="execute_shell_command", description="Execute a shell command provided in natural language")
async def execute_shell_command(command: str) -> str:
	"""
	Execute a shell command.
	Args:
		command (str): The shell command to execute (parsed from natural language).
	Returns:
		str: The output or error from the shell command.
	Example:
		execute_shell_command("ls -l /home/user")
	Example response:
		"total 0\n-rw-r--r-- 1 user user 0 Aug 30 12:00 file.txt"
	"""
	try:
		result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
		if result.returncode == 0:
			return result.stdout.strip() or "(No output)"
		else:
			return f"Error (code {result.returncode}): {result.stderr.strip()}"
	except Exception as e:
		return f"Exception occurred: {e}"

if __name__ == "__main__":
	mcp.run(transport="stdio")
	"""
	Run the MCP server for shell command execution
	"""
