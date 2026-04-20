from pydantic_ai import Agent
from customer_suport.backend.constants import MODEL_MEDIUM
from dotenv import load_dotenv

load_dotenv()

# NOTE: change system prompt to load from MLFlow later
support_agent = Agent(
    model=MODEL_MEDIUM, system_prompt="You are a customer support agent"
)
