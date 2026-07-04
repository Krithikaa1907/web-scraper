import requests
from bs4 import BeautifulSoup

try:
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all("h2")

    with open("headlines.txt", "w", encoding="utf-8") as file:
        for i, headline in enumerate(headlines, start=1):
            text = headline.get_text(strip=True)
            if text:
                print(f"{i}. {text}")
                file.write(f"{i}. {text}\n")

    print("Headlines saved to headlines.txt")

except Exception as e:
    print("Error:", e)