from crewai import Task
from agents.frontend_engineer import frontend_engineer
from tasks.researcher_task import researcher_task

reporting_task = Task(
    description="Compile the results into a detailed HTML report.",
    expected_output=(
        "An HTML file:\n"
        "Top 10 AI Research Papers published on {date}\n"
        "- Title (clickable link)\n"
        "- Authors\n"
        "- Short abstract summary (2–4 sentences)"
    ),
    agent=frontend_engineer,
    context=[researcher_task],
    output_file="./ai_research_report.html",
    human_input=True,
)
