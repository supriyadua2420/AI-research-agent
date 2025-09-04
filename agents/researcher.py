from crewai import Agent
from tools.fetch_arxiv import FetchArxivPapersTool

arxiv_search_tool = FetchArxivPapersTool()

researcher = Agent(
    role="Senior Researcher",
    goal="Find the top 10 papers from the search results from ArXiv on {date}. Rank them appropriately.",
    backstory="You are a senior researcher with a deep understanding of AI research. You identify the best papers based on title and abstract.",
    verbose=True,
    tools=[arxiv_search_tool],
)
