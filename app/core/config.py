from typing import List, Union, ClassVar
from dotenv import load_dotenv, dotenv_values
from pydantic_settings import BaseSettings
import os 

load_dotenv(".env")
creds= dotenv_values(".env")

class Settings(BaseSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[str] = eval(os.environ["BACKEND_CORS_ORIGINS"])
    DRIVER_NAME : str
    DB_USERNAME: str
    DB_HOST : str
    DB_NAME: str
    DB_PASSWORD: str
    DB_PORT: str

settings = Settings(
    PROJECT_NAME=os.environ["PROJECT_NAME"],
    DRIVER_NAME = os.environ["DRIVER_NAME"], 
    DB_USERNAME = os.environ["DB_USERNAME"],
    DB_HOST = os.environ["DB_HOST"], 
    DB_NAME = os.environ["DB_NAME"],
    DB_PASSWORD = os.environ["DB_PASSWORD"],
    DB_PORT = os.environ["DB_PORT"]
)