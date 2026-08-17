from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()


llm =ChatOpenAI(model="gpt-5")
tools= [TavilySearch()]
agent= create_agent(model=llm,tools=tools)

def main():
    print("Hello...Welcome inn")
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job posting for ai devops engineer using langchain in houston on linkedin and list their details")})
    print(result)

if __name__ == "__main__":
    main()