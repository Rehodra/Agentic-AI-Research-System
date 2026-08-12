from agents import build_search_agent, build_scrape_agent, writer_chain, critic_chain
from rich import print

def run_research_pipeline(topic: str) -> dict:

    state = {}
    """
    Run the research pipeline for a given topic.
    This includes searching, scraping, writing, and critiquing.
    """
    print(f"[bold green]Starting research pipeline for topic:[/bold green] {topic}")
    # Step 1: Search for information
    print("[bold blue]Step 1: Search Agent working...[/bold blue]")
    search_agent = build_search_agent()
    search_results = search_agent.invoke({
        "messages":[("user", f"Search for recent and reliable information on the topic: {topic}")]
    })

    state["search_results"] = search_results["messages"][-1].content
    print(f"[bold green]Search Results:[/bold green]\n{state['search_results']}")

# Step 2: Scrape URLs for deeper reading
    print ("\n[bold blue]Step 2: Scrape Agent working...[/bold blue]")

    reader_agent = build_scrape_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
    })

    state["scraped_content"] = reader_result["messages"][-1].content
    print(f"[bold green]Scraped Content:[/bold green]\n{state['scraped_content']}")

    # Step 3: Write a research report
    print("\n[bold blue]Step 3: Writer Chain working...[/bold blue]")

    research_combined = f"Search Results:\n{state['search_results']}\n\nScraped Content:\n{state['scraped_content']}" #combined research results and scraped content

    writer_result = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    state["research_report"] = writer_result

    print(f"[bold green]Research Report:[/bold green]\n{state['research_report']}")

    # Step 4: Critique the research report
    print("\n[bold blue]Step 4: Critic Chain working...[/bold blue]")
    critic_result = critic_chain.invoke({
        "report": state["research_report"]
    })
    state["critique"] = critic_result
    print(f"[bold green]Critique:[/bold green]\n{state['critique']}")


    return state

if __name__ == "__main__":
    topic = input("Enter a research topic: ")
    run_research_pipeline(topic)