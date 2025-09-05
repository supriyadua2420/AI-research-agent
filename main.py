from dotenv import load_dotenv
import os
from crew.arxiv_research import arxiv_research_crew

# Load environment variables from .env file
load_dotenv()

crew_inputs = {
    "date": "2025-03-12"  # Change date as needed
}

if __name__ == "__main__":
    result = arxiv_research_crew.kickoff(inputs=crew_inputs)
    print(result)
