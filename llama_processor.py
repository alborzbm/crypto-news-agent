# llama_processor.py
from llama_api import query_llama

def analyze_news_title(title: str) -> str:
    """
    Use LLaMA model to generate summary, keywords, and sentiment for a news title.
    """
    prompt = (
        "You are a crypto news analyst.\n"
        "Analyze the following news title and provide output in this format:\n"
        "Summary:\nKeywords:\nSentiment:\n\n"
        f"News title: {title}"
    )
    response = query_llama(prompt)
    return response
