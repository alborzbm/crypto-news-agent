# news_fetcher.py
import requests
from config import GNEWS_API_KEY

def fetch_crypto_news():
    """
    Fetch news articles related to top 5 cryptocurrencies from GNews API.
    """
    query = "bitcoin OR ethereum OR ripple OR litecoin OR cardano"
    url = f"https://gnews.io/api/v4/top-headlines?token={GNEWS_API_KEY}&lang=en&q={query}&max=50"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Debug print to inspect API response structure
        print("DEBUG: GNews API response received")

        articles = data.get("articles", [])
        news_list = []
        for article in articles:
            title = article.get("title", "")
            source_name = article.get("source", {}).get("name", "")
            news_list.append({"title": title, "source": source_name})
        return news_list

    except Exception as e:
        print(f"Error fetching news: {e}")
        return []
