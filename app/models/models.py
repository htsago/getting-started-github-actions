from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str
    thread_id: str


class ResponseFormat(BaseModel):
    response: str
