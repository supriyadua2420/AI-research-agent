from crewai import Task
from agents.researcher import researcher

researcher_task = Task(
    description="Find the top 10 research papers from ArXiv on {date}.",
    expected_output=(
        "A list of top 10 research papers with:\n"
        "- Title\n"
        "- Authors\n"
        "- Abstract\n"
        "- Link to the paper"
    ),
    agent=researcher,
    human_input=True,
)
