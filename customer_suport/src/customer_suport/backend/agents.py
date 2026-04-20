from pydantic_ai import Agent
from customer_suport.backend.constants import MODEL_MEDIUM
from dotenv import load_dotenv

load_dotenv()

# NOTE: change system prompt to load from MLFlow later
support_agent = Agent(
    model=MODEL_MEDIUM, system_prompt="You are a customer support agent"
)


@support_agent.tool_plain
def lookup_faq(category: str) -> str:
    """FAQ for customer support"""
    faq = {
        "refund": "Full refunds within 30 days with receipt.",
        "shipping": "Standard: 5-7 days. Express available.",
        "warranty": "1-year manufacturer warranty included.",
    }

    return faq.get(
        category,
        "Question not found. Inform customer that available categories are: refund, shipping, warranty",
    )