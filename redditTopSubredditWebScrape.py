from bs4 import BeautifulSoup
import requests


url = requests.get("https://redditmetrics.com/") #web scraping tool


soup = BeautifulSoup(url.text, "html.parser")

with open ('.txt','w') as f:
    for subreddit in soup.find_all('a'):
        try:
            if 'r' in subreddit.string:
                f.write(subreddit.string[3:] + '\n')
        except: 
            TypeError
stuff = BeautifulSoup()



