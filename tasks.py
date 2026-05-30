from crewai import Task


def create_task(agent, requirement):
    return Task(
        description=f"""
        Build the following project:

        {requirement}

        Requirements:
        1. Generate production-ready code.
        2. Create all required files.
        3. Use the File Writer tool to save every file.
        4. Include package.json, requirements.txt, README.md, etc. when needed.
        5. Follow best practices.
        6. Use modern technologies.
        7. Do not leave placeholders or TODO comments.
        8. Save everything inside the output directory.

        IMPORTANT:
        Never return code as plain text.
        Always use the File Writer tool.
        """,

        expected_output="""
        Complete project generated and saved inside output folder.
        """,

        agent=agent
    )