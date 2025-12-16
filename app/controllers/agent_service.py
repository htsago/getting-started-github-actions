from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from app.core.config import settings

load_dotenv()

def get_agent_executor():

    model = init_chat_model(
        model=settings.model,
        model_provider=settings.model_provider,
        temperature=settings.temperature
    )

    agent = create_agent(
        model=model,
        tools = [],
        system_prompt=settings.system_prompt,
        checkpointer= InMemorySaver()
    )

    return agent
