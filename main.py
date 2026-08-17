import os
from dotenv import load_dotenv
from  langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
load_dotenv()


def main():
    print("Hello....wait for a moment!")
 
    summary_template = """
    give me infomation about {person} and i want you to create in 2 points for each point:
    1. short summary on his life
    2. two interesting facts
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["person"], template=summary_template
        )
    llm = ChatOpenAI(temperature=0, model="gpt-5")
    #llm = ChatOllama(model="gemma3:270m")
    chain = summary_prompt_template | llm
    response= chain.invoke({"person": "Srinivasa Ramanujan"})
    print(response.content)


if __name__ == "__main__":
    main()
