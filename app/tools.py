import os

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langchain.tools import tool
import requests
from tavily import TavilyClient
from rich import print

load_dotenv()

tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


@tool
def web_search(query: str) -> str:
    """
    Perform a web search using the Tavily API and return
    the results including URLs, titles, and snippets.
    """
    try:
        response = tavily_client.search(
            query=query,
            max_results=5
        )

        out = []

        for r in response["results"]:
            out.append(
                f"Title: {r['title']}\n"
                f"URL: {r['url']}\n"
                f"Snippet: {r['content'][:300]}\n"
            )

        return "\n----\n".join(out)

    except Exception as e:
        return f"An error occurred while performing the web search: {str(e)}"

@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"