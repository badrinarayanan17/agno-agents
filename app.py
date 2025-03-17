# agentic flow using agno
# import the necessary packages

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
import os
from dotenv import load_dotenv
from agno.models.ollama import Ollama

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

agents = Agent(
    # model=Ollama(id="llama3"),
    model=Groq(id="qwen-2.5-32b"),  # alibaba cloud
    markdown=True,
    description="You are an assistant provide responses for the questions",
    tools=[DuckDuckGoTools()]
)

agents.print_response("Search badri narayanan working in neostats, tell about him")


