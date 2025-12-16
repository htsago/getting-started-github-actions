class Settings:
    project_name: str = "Chatbot"
    system_prompt: str ="""You are a helpful assistant!"""
    model: str = "openai/gpt-oss-120b"
    model_provider: str ="groq"
    temperature: float = 0.5

settings = Settings()
