from typing import List, Union, ClassVar
from dotenv import load_dotenv, dotenv_values
from pydantic_settings import BaseSettings
import os 

load_dotenv(".env")
creds= dotenv_values(".env")

class Settings(BaseSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[str] = eval(os.environ["BACKEND_CORS_ORIGINS"])

settings = Settings(
    PROJECT_NAME=os.environ["PROJECT_NAME"]
)
