from crewai import LLM

# Configure Ollama llama3 model
ollama_llm = LLM(
    model="ollama/llama3",   # Matches your installed model name
    base_url="http://localhost:11434"
)
