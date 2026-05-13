import os
import dotenv
from dataclasses import dataclass


dotenv.load_dotenv()


@dataclass
class DatabaseConfig:
    DB_NAME: str = os.getenv("DB_NAME")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")


@dataclass
class EmailConfig:
    EMAIL_FROM: str = os.getenv("EMAIL_FROM")
    EMAIL_PASSWORD: str = os.getenv("EMAIL_PASSWORD")
    EMAIL_SERVER: str = os.getenv("EMAIL_SERVER")
    EMAIL_PORT: int = os.getenv("EMAIL_PORT")
