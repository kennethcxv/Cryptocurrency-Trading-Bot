import requests
from bs4 import BeautifulSoup

NEWS_URL = 'https://www.coindesk.com/'

def get_latest_news():
    response = requests.get(NEWS_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extracting headlines (this depends on the website's structure)
    headlines = soup.find_all('h4', class_='headline')
    return [headline.text for headline in headlines]
