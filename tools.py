# Import BaseTool so CrewAI can recognize this class as a custom tool
from crewai.tools import BaseTool

# Import Path for handling folders/files in a clean, cross-platform way
from pathlib import Path


# Create a custom CrewAI tool by inheriting from BaseTool
class FileWriterTool(BaseTool):

    # Name of the tool shown to the agent
    name: str = "File Writer"

    # Description helps the LLM understand when to use this tool
    description: str = """
    Writes generated code into the output folder.

    Examples:
    - index.html
    - styles.css
    - app/page.tsx

    Never include 'output/' in the filename.
    """

    # This method contains the actual tool logic
    def _run(self, filename: str, content: str):

        # Create output folder if it doesn't exist
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)

        if filename.startswith("output/"):
            filename = filename.replace("output/", "", 1)

        # Create full file path
        filepath = output_dir / filename

        # Create parent folders automatically
        # Example:
        # output/app/page.tsx
        filepath.parent.mkdir(parents=True, exist_ok=True)

        # Write file content
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        # Return success message
        return f"Saved {filepath}"