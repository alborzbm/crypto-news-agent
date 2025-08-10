# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")

OLLAMA_API_URL = "http://localhost:11434/api/v1/completions" 
MODEL_NAME = "llama3.2:latest"