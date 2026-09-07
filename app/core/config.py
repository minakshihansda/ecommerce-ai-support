from dotenv import load_dotenv
import os

load_dotenv("app/.env")


GROQ_API_KEY = os.getenv("GROQ_API_KEY")