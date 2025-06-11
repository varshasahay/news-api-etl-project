# Python script for News API
import requests
import pandas as pd
import time

api_key = '4b01d8cd151b4762b783caa3f524860b'
url = 'https://newsapi.org/v2/everything'
query = 'technology'
page_size = 100
total_pages = 5

all_articles = []

headers = {
    'User-Agent': 'Mozilla/5.0'
}

for page in range(1, total_pages + 1):
    print(f"Fetching page {page}...")
    params = {
        'q': query,
        'apiKey': api_key,
        'pageSize': page_size,
        'page': page,
        'language': 'en',
        'sortBy': 'publishedAt'
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])

        if not articles:
            print("No more articles found.")
            break

        for article in articles:
            all_articles.append({
                'source': article.get('source', {}).get('name', ''),
                'author': article.get('author', ''),
                'title': article.get('title', ''),
                'description': article.get('description', ''),
                'url': article.get('url', ''),
                'publishedAt': article.get('publishedAt', '')
            })

        time.sleep(1)

    elif response.status_code == 426:
        print(f"Failed at page {page}: Status Code 426 (Upgrade Required)")
        print("Free plans may be restricted for bulk fetch. Consider changing the query or reducing pages.")
        break
    else:
        print(f"Failed at page {page}, Status Code: {response.status_code}")
        break

df = pd.DataFrame(all_articles)
df.to_csv('c:/users/91626/Downloads/news_100_articles.csv', index=False)
print(f"Saved {len(df)} articles to CSV.")
