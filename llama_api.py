# llama_api.py
import requests
from config import MODEL_NAME

# The standard Ollama endpoint for generating text
OLLAMA_GENERATE_URL = "http://localhost:11434/api/generate"

def query_llama(prompt: str) -> str:
    """
    Sends a prompt to the local Llama model using Ollama's standard generate API.
    """
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,  # To get the full response at once
        "options": {
            "temperature": 0.7
        }
    }

    try:
        response = requests.post(OLLAMA_GENERATE_URL, json=payload, headers=headers)
        response.raise_for_status()  # Check for HTTP errors like 404 or 500

        data = response.json()
        
        # The main content is in the 'response' key for the generate API
        return data.get("response", "").strip()
    
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the Llama model: {e}")
        return "Analysis failed (connection error)."
    except KeyError:
        print("Error: Invalid response format from Llama. 'response' key not found.")
        return "Analysis failed (invalid response format)."