import os
import uuid
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime


class ReutersSpider:
    def __init__(self):
        # the homepage url
        self.base_url = 'https://www.reuters.com'

    def parse_homepage(self):
        # request the homepage
        response = requests.get(self.base_url)
        # parse html
        soup = BeautifulSoup(response.content, 'html.parser')
        # print(soup.prettify())
        return soup

    def parse_hot_news(self):
        soup = self.parse_homepage()
        paragraphs = soup.find_all(class_="home-page-grid__story__iu-Dj")
        news = []
        for idx, p in enumerate(paragraphs[0:]):
            # print(p.prettify())
            id = f"reuters_{str(uuid.uuid4())}"
            type = p.find('div').get('data-testid')
            time = p.find('time').get('datetime')
            title = ''
            article_url = ''
            for a_tag in p.find_all('a'):
                if a_tag.get('data-testid') == 'Heading':
                    title = a_tag.text
                    article_url = self.base_url + a_tag.get('href')
            if title and article_url:
                news.append([id, type, time, title, article_url])
        news_df = pd.DataFrame(news, columns=['id', 'type', 'time', 'title', 'article_url'])
        return news_df


if __name__ == '__main__':
    res = ReutersSpider().parse_hot_news()
