
import os

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.prompts import ChatPromptTemplate
from tools import web_search, scrape_url


groq_api_key = os.getenv("GROQ_API_KEY")
groq_api_key2 = os.getenv("GROQ_API_KEY2")
groq_api_key3 = os.getenv("GROQ_API_KEY3")
groq_api_key4 = os.getenv("GROQ_API_KEY4")
groq_model = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

# 2. Model
#loading the LLM model
search_llm = init_chat_model(groq_model, temperature=0, model_provider="groq", groq_api_key=groq_api_key) 
scrape_llm = init_chat_model(groq_model, temperature=0, model_provider="groq", groq_api_key=groq_api_key2)
writer_chain_llm = init_chat_model(groq_model, temperature=0.7, model_provider="groq", groq_api_key=groq_api_key3) 
critic_chain_llm = init_chat_model(groq_model, temperature=0.5, model_provider="groq", groq_api_key=groq_api_key4) 


#1st agent
def build_search_agent():
    """
    Build a search agent that can perform web searches and scrape URLs.
    """
    agent = create_agent(
    model=search_llm,
    tools=[web_search],
)
    return agent

def build_scrape_agent():
    """
    Build a scrape agent that can scrape URLs for deeper reading.
    """
    agent = create_agent(
        model=scrape_llm,
        tools=[scrape_url],
    )
    return agent

#writer chain 

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | writer_chain_llm | StrOutputParser()

#critic_chain 

critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | critic_chain_llm | StrOutputParser()