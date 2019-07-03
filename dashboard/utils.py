from urllib.request import HTTPError, Request, urlopen
from bs4 import BeautifulSoup
import requests
from .models import *


header = {'User-Agent'  : 'Mozilla/5.0'}

def post_scrapping(url):
    try:
        r = requests.get(url)
    except Exception as e:
        return message.error
    url = r.text
    soup = BeautifulSoup(url, 'html.parser')
    c = soup.find('h1', {'class':'entry-title'})
    title = c.text
    
    content = soup.find('div', {'class':'pf-content'})
    content = content.text
    Post.objects.create(url=url, title=title, content=content)

