import os
from dotenv import load_dotenv

# Try loading from .env, if that fails or keys missing, try config.env
if not load_dotenv(".env"):
    load_dotenv("config.env")
# Also explicitly try loading config.env to be sure if .env skipped
load_dotenv("config.env", override=True)

class Config:
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    HF_TOKEN = os.getenv("HF_TOKEN")
    MAX_LOOPS = int(os.getenv("MAX_LOOPS", 1))
    # Default to a cost-effective powerful model, user can override in .env
    LLM_MODEL = os.getenv("LLM_MODEL", "google/gemini-2.0-flash-lite-preview-02-05:free") 
    OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    CONTRADICTION_THRESHOLD = float(os.getenv("CONTRADICTION_THRESHOLD", 0.7))
    MAX_SUB_QUESTIONS = 5
    
    # Local Config
    LOCAL_LLM_BASE_URL = os.getenv("LOCAL_LLM_BASE_URL", "http://localhost:1233/v1")
    LOCAL_LLM_MODEL = os.getenv("LOCAL_LLM_MODEL", "hermes-3-llama-3.1-8b")

    @staticmethod
    def validate():
        if not Config.TAVILY_API_KEY:
            raise ValueError("TAVILY_API_KEY is not set in environment variables")
        if not Config.OPENROUTER_API_KEY:
            raise ValueError("OPENROUTER_API_KEY is not set in environment variables")
