import os
from dotenv import load_dotenv

print("Attempting to load .env...")
try:
    load_dotenv(".env")
    print(".env loaded (unexpectedly)")
except Exception as e:
    print(f".env load failed: {e}")

print("Attempting to load config.env...")
try:
    load_dotenv("config.env", override=True)
    print("config.env loaded")
except Exception as e:
    print(f"config.env load failed: {e}")

print(f"OPENROUTER_API_KEY: {os.getenv('OPENROUTER_API_KEY')}")
