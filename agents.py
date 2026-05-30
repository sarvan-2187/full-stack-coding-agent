from crewai import Agent, LLM
from dotenv import load_dotenv
from tools import FileWriterTool
import os

load_dotenv()

llm = LLM(
    model=os.getenv("MODEL"),
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("BASE_URL"),
    temperature=float(os.getenv("TEMPERATURE", 0.2))
)

coder = Agent(
    role="Senior Full Stack Developer",
    goal="Generate production-ready code and save files",
    backstory="""
    You are an expert software engineer specializing in
    full-stack development, APIs, automation, and system design.
    """,
    llm=llm,
    tools=[FileWriterTool()],
    verbose=True
)