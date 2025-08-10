# main.py
from news_fetcher import fetch_crypto_news
from llama_processor import analyze_news_title

def main():
    top_coins = ["bitcoin", "ethereum", "ripple", "litecoin", "cardano"]
    
    # Fetch news from API
    news_list = fetch_crypto_news()

    # Filter news that mention top coins (case insensitive)
    filtered_news = [
        news for news in news_list 
        if any(coin in news["title"].lower() for coin in top_coins)
    ]

    if not filtered_news:
        print("No crypto news found for the top coins today.")
        return

    print("# Daily Crypto News Report\n")

    for idx, news in enumerate(filtered_news, start=1):
        analysis = analyze_news_title(news["title"])
        print(f"## {idx}. {news['title']}")
        print(f"**Source:** {news['source']}\n")
        print(analysis)
        print("\n---\n")

if __name__ == "__main__":
    main()
