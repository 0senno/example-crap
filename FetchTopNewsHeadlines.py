import requests

def fetch_top_headlines(api_key):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def display_headlines(data):
    if data["status"] == "ok":
        articles = data["articles"]
        print("Top Headlines:")
        for idx, article in enumerate(articles, start=1):
            print(f"{idx}. {article['title']}")
            print(f"   Source: {article['source']['name']}")
            print(f"   Published At: {article['publishedAt']}")
            print(f"   URL: {article['url']}")
            print()
    else:
        print("Failed to fetch top headlines.")

def main():
    api_key = "62cb1e7763a64a1c95b4912ecb0f7219"  # Replace "YOUR_API_KEY" with your actual API key from NewsAPI.org
    headlines_data = fetch_top_headlines(api_key)
    display_headlines(headlines_data)

if __name__ == "__main__":
    main()
