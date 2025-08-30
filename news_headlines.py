import requests

API_KEY = "YOUR_NEWSAPI_KEY"  # Replace with your NewsAPI key
BASE_URL = "https://newsapi.org/v2/top-headlines"

def fetch_headlines(category="general"):
    params = {
        "country": "us",
        "category": category,
        "apiKey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        print("Error fetching news.")
        return []
    articles = response.json().get("articles", [])
    return [a["title"] for a in articles[:5]]

def main():
    category = input("Enter category (general, technology, sports): ").lower()
    headlines = fetch_headlines(category)
    print("\nLatest Headlines:")
    for i, h in enumerate(headlines, start=1):
        print(f"{i}. {h}")

if __name__ == "__main__":
    main()
