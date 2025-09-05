from typing import Type, List
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
import arxiv
import time
import datetime


class FetchArxivPapersInput(BaseModel):
    """Input schema for FetchArxivPapersTool."""
    target_date: str = Field(
        ..., description="Target date to fetch papers for in format YYYY-MM-DD"
    )


class FetchArxivPapersTool(BaseTool):
    name: str = "fetch_arxiv_papers"
    description: str = (
        "Fetches all ArXiv papers from selected categories submitted on the target date."
    )
    args_schema: Type[BaseModel] = FetchArxivPapersInput

    def _run(self, target_date: str) -> List[dict]:
        # Convert string to datetime.date
        try:
            target_date_obj = datetime.datetime.strptime(target_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format: {target_date}. Use YYYY-MM-DD.")

        # Define categories (AI-related)
        AI_CATEGORIES = ["cs.CL"]  # NLP/Computational Linguistics
        # You can add more: ["cs.AI", "cs.LG", "cs.CV", "cs.MA", "cs.RO"]

        # Define date range
        start_date = target_date_obj.strftime("%Y%m%d%H%M")
        end_date = (target_date_obj + datetime.timedelta(days=1)).strftime("%Y%m%d%H%M")

        # Initialize ArXiv client
        client = arxiv.Client(
            page_size=100,      # Fetch 100 results per page
            delay_seconds=3     # Delay between requests to respect rate limits
        )

        all_papers = []

        for category in AI_CATEGORIES:
            print(f"Fetching papers for category: {category}")

            search_query = f"cat:{category} AND submittedDate:[{start_date} TO {end_date}]"

            search = arxiv.Search(
                query=search_query,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                max_results=None  # Fetch all available results
            )

            category_papers = []
            for result in client.results(search):
                category_papers.append({
                    "title": result.title,
                    "authors": [author.name for author in result.authors],
                    "summary": result.summary,
                    "published": result.published,
                    "url": result.entry_id
                })
                time.sleep(3)  # Respect rate limits

            print(f"Fetched {len(category_papers)} papers from {category}")
            all_papers.extend(category_papers)

        return all_papers
