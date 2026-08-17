from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

class Source(BaseModel):
    """Schema for source used by the agent"""

    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for agent response with answers and sources"""

    answer:str = Field(description="The agent's answer to the query")
    sources: list[Source]= Field(default_factory=list, description="List of sources used to generate the answer" )


llm =ChatOpenAI(model="gpt-5")
tools= [TavilySearch()]
agent= create_agent(model=llm,tools=tools,response_format=AgentResponse)

def main():
    print("Hello...Welcome inn")
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job posting for ai devops engineer using langchain in houston on linkedin and list their details. make sure they are offering sponsership or h1b")})
    print(result)

if __name__ == "__main__":
    main()