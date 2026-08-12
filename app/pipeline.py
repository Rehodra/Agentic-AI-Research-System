from agents import build_search_agent, build_scrape_agent, writer_chain, critic_chain
from cli_formatter import (
    print_pipeline_start,
    print_step,
    print_search_results,
    print_scraped_content,
    print_research_report,
    print_critique,
)

def run_research_pipeline(topic: str) -> dict:

    state = {}
    """
    Run the research pipeline for a given topic.
    This includes searching, scraping, writing, and critiquing.
    """
    print_pipeline_start(topic)
    # Step 1: Search for information
    print_step(1, "Search Agent")
    search_agent = build_search_agent()
    search_results = search_agent.invoke({
        "messages":[("user", f"Search for recent and reliable information on the topic: {topic}")]
    })

    state["search_results"] = search_results["messages"][-1].content
    print_search_results(state['search_results'])

# Step 2: Scrape URLs for deeper reading
    print_step(2, "Scrape Agent")

    reader_agent = build_scrape_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
    })

    state["scraped_content"] = reader_result["messages"][-1].content
    print_scraped_content(state['scraped_content'])

    # Step 3: Write a research report
    print_step(3, "Writer Chain")

    research_combined = f"Search Results:\n{state['search_results']}\n\nScraped Content:\n{state['scraped_content']}" #combined research results and scraped content

    writer_result = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    state["research_report"] = writer_result

    print_research_report(state['research_report'])

    # Step 4: Critique the research report
    print_step(4, "Critic Chain")
    critic_result = critic_chain.invoke({
        "report": state["research_report"]
    })
    state["critique"] = critic_result
    print_critique(state['critique'])


    return state

if __name__ == "__main__":
    topic = input("Enter a research topic: ")
    run_research_pipeline(topic)