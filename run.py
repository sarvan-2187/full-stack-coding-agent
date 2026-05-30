# Import the Crew class from CrewAI
# A Crew is responsible for managing agents and tasks
from crewai import Crew

# Import the coder agent from agents.py
from agents import coder

# Import the function that creates a task dynamically
from tasks import create_task


# Ask the user to enter a requirement through the terminal
# Example:
# Create a Flask API for user management
requirement = input("\nEnter your requirement:\n> ")


# Create a task using the user's requirement
# The task will be assigned to the coder agent
task = create_task(coder, requirement)


# Create a Crew instance
crew = Crew(
    
    # List of agents that can perform tasks
    agents=[coder],
    
    # List of tasks to execute
    tasks=[task],
    
    # Enable detailed logs in the terminal
    # Useful for debugging and understanding agent actions
    verbose=True
)


# Start the Crew execution
# The coder agent will:
# 1. Read the requirement
# 2. Generate the required code/project
# 3. Use FileWriterTool to save files into output/
crew.kickoff()


# Display a success message after execution completes
print("\nProject generated inside output folder.")