# multiple agents using agno

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
import os
from dotenv import load_dotenv

load_dotenv()

hackathon_researcher = Agent(
    model=Groq(id="qwen-2.5-32b"),
    description="Provide relevant answers based on the questions",
    instructions="You are a professional researcher",
    tools=[DuckDuckGoTools()],
    markdown=True
)

hackathon_top10 = Agent(
    model=Groq(id="qwen-2.5-32b"),
    description="You are a problem statements finder",
    instructions="Your job is to find the top scenarios based on the user query",
    tools=[DuckDuckGoTools()],
    markdown=True
    
)

hackathon_team = Agent(
    team=[hackathon_researcher, hackathon_top10],
    description="Your task is to collaborate with both the agents bring out a valid response. Look into sources",
    instructions=["Refer the sources","Responses should be in tabular format"],
    model=Groq(id="qwen-2.5-32b"),
    markdown=True
    
)

hackathon_team.print_response("I need to prepare for full stack developer hackathon")


