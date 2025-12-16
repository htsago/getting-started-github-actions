import random
from fastapi import APIRouter, HTTPException
import logging
from app.controllers.agent_service import get_agent_executor
from app.models.models import ChatRequest

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    try:
        agent  = get_agent_executor()
        thread_id = random.randint(999,99999)
        config = {"configurable": {"thread_id":thread_id }}

        response = agent.invoke(
            {"messages": [{"role": "user", "content": request.question}]},
            config=config
        )

        last_message = response["messages"][-1]
        return {"answer": last_message.content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))