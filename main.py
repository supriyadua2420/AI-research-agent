# import os
# import datetime
# import time
# from typing import Type, List
# from pydantic import BaseModel, Field
# from dotenv import load_dotenv
# import arxiv
# from datetime import date

# # CrewAI imports
# from crewai.tools import BaseTool
# from crewai_tools import (
#     DirectoryReadTool,
#     FileReadTool,
#     SerperDevTool,
#     WebsiteSearchTool
# )

# load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")
# model_name = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
# serper_api_key = os.getenv("SERPER_API_KEY")

# os.environ["OPENAI_API_KEY"] = openai_api_key
# os.environ["OPENAI_MODEL_NAME"] = model_name
# os.environ["SERPER_API_KEY"] = serper_api_key

# class FetchArxivPapersInput(BaseModel):
#     """Input schema for FetchArxivPapersTool."""
#     target_date: datetime.date = Field(..., description="Target date to fetch papers for.")

# class FetchArxivPapersTool(BaseTool):
#     name: str = "fetch_arxiv_papers"
#     description: str = "Fetches all ArXiv papers from selected categories submitted on the target date."
#     args_schema: Type[BaseModel] = FetchArxivPapersInput

#     def _run(self, target_date: datetime.date) -> List[dict]:
#         AI_CATEGORIES = ["cs.CL"]
#         start_date = target_date.strftime('%Y%m%d%H%M')
#         end_date = (target_date + datetime.timedelta(days=1)).strftime('%Y%m%d%H%M')

#         client = arxiv.Client(page_size=10, delay_seconds=3)
#         all_papers = []

#         for category in AI_CATEGORIES:
#             print(f"Fetching papers for category: {category}")
#             search_query = f"cat:{category} AND submittedDate:[{start_date} TO {end_date}]"
#             search = arxiv.Search(query=search_query,
#                                   sort_by=arxiv.SortCriterion.SubmittedDate,
#                                   max_results=None)
#             category_papers = []
#             for result in client.results(search):
#                 category_papers.append({
#                     'title': result.title,
#                     'authors': [author.name for author in result.authors],
#                     'summary': result.summary,
#                     'published': result.published,
#                     'url': result.entry_id
#                 })
#                 time.sleep(3)
#             print(f"Fetched {len(category_papers)} papers from {category}")
#             all_papers.extend(category_papers)

#         return all_papers



# docs_tool = DirectoryReadTool(directory='./')
# file_tool = FileReadTool()
# search_tool = SerperDevTool()
# web_rag_tool = WebsiteSearchTool()
# arxiv_tool = FetchArxivPapersTool()  # <— your custom ArXiv tool


# Example: fetch papers from Jan 1, 2024
# papers = arxiv_tool._run(target_date=date(2024, 1, 1))
# print(f"Fetched {len(papers)} papers")
# if papers:
#     print("First paper title:", papers[0]['title'])

from dotenv import load_dotenv
import os
from crew.arxiv_research import arxiv_research_crew

# Load environment variables from .env file
load_dotenv()

# (Optional) Debug: check if key is loaded
# if not os.getenv("OPENAI_API_KEY"):
#     raise ValueError("❌ OPENAI_API_KEY not found. Please set it in your .env file.")

crew_inputs = {
    "date": "2025-03-12"  # Change date as needed
}

if __name__ == "__main__":
    result = arxiv_research_crew.kickoff(inputs=crew_inputs)
    print(result)
