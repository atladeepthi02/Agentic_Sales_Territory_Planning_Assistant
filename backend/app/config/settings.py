from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "agentic-sales-territory-planning-assistant"
    environment: str = "development"

    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"
    openai_embedding_model: str = "text-embedding-3-small"

    database_url: str = "sqlite:///./sales.db"
    redis_url: str = "redis://localhost:6379/0"

    chroma_host: str = "localhost"
    chroma_port: int = 8000

    langchain_api_key: str = ""
    langchain_tracing_v2: str = "false"
    langchain_project: str = "sales-territory-planner"

    next_public_api_url: str = "http://localhost:8000"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
