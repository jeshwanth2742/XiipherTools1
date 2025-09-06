import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bearer token for X API v2 (App-only authentication)
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

if not BEARER_TOKEN:
    raise ValueError("BEARER_TOKEN not found in .env file. Please add it before running the app.")
