from crewai_tools import BaseTool
#from langchain_community.tools import tool
import subprocess

class GitTool(BaseTool):
    name: str = "Git Tool"
    description: str = "A tool for performing Git operations like commit and push."

    def _run(self, command: str) -> str:
        try:
            result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"

    def commit(self, message: str) -> str:
        return self._run(f"git commit -am '{message}'")

    def push(self) -> str:
        return self._run("git push")