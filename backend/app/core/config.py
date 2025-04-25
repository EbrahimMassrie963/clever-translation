import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    if DATABASE_URL is None:
        raise ValueError("DATABASE_URL is not set in the .env file")
    
    if GEMINI_API_KEY is None:
        raise ValueError("GEMINI_API_KEY is not set in the .env file")

settings = Settings()
