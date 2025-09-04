from crewai import Agent

frontend_engineer = Agent(
    role="Senior Frontend & AI Engineer",
    goal="Compile the results into a HTML file.",
    backstory="You are a skilled frontend engineer with decades of experience writing HTML/CSS, and you also understand AI research.",
    verbose=True,
)
