from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="/opt/.env",
        env_ignore_empty=True,
        extra="ignore",
    )

    model: str = "gpt-4o-mini-2024-07-18"
    openai_api_key: str = ""

    postgres_dsn: PostgresDsn = (
        "postgresql+psycopg://postgres:password@example.supabase.com:6543/postgres"
    )

    @computed_field
    @property
    def orm_conn_str(self) -> str:
        return self.postgres_dsn.encoded_string()

    @computed_field
    @property
    def checkpoint_conn_str(self) -> str:
        # NOTE: LangGraph AsyncPostgresSaver has some issues
        # with specifying psycopg driver explicitly
        return self.postgres_dsn.encoded_string().replace("+psycopg", "")


settings = Settings()
