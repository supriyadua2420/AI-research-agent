from crewai import Crew
from tasks.researcher_task import researcher_task
from tasks.reporting_task import reporting_task
from agents.researcher import researcher
from agents.frontend_engineer import frontend_engineer

arxiv_research_crew = Crew(
    agents=[researcher, frontend_engineer],
    tasks=[researcher_task, reporting_task],
    verbose=True,
)
