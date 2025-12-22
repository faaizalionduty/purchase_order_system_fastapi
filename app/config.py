from pydantic_settings import BaseSettings
import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
ENV_FILE = os.path.join(BASE_DIR, '.env')

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI:str
    SECRET_KEY:str
    ALGORITHM:str
    PROJECT_NAME:str = "Purchase-Order-Management-System"

    class Config:
        env_file = ENV_FILE
        env_file_encoding = 'utf-8'

settings = Settings()
