import os
from pathlib import Path
from typing import List
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

# 1. Point directly to your .env file inside the app folder
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

class Settings(BaseSettings):
    # This prevents Pydantic from automatically reading fields from os.environ
    model_config = SettingsConfigDict(env_prefix="NONE_")

    PROJECT_NAME: str = os.environ.get("PROJECT_NAME", "Dispatch Management System")
    DB_URL: str = os.environ.get("DB_URL", "postgresql://postgres:root@localhost:5432/fastapi_test_db")
    BACKEND_CORS_ORIGINS: List[str] = []

# 2. Instantiate cleanly
settings = Settings()

# 3. Manually parse the CORS string safely without eval() or JSON decoding errors
raw_cors = os.environ.get("BACKEND_CORS_ORIGINS", "*")
settings.BACKEND_CORS_ORIGINS = [x.strip() for x in raw_cors.split(",") if x.strip()]
