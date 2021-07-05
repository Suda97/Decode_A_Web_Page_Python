import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
source = requests.get(base_url)
soup = BeautifulSoup(source.text, 'html.parser')

for story_heading in soup.find_all('li'):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
