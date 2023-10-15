import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime


class HuanQiuSpider:
    def __init__(self):
        # homepage url
        self.base_url = 'https://world.huanqiu.com'

    def parse_homepage(self):
        # request the homepage
        response = requests.get(self.base_url)
        # parse html
        soup = BeautifulSoup(response.content, 'html.parser')
        # print(soup.prettify())
        return soup

    def parse_subpage(self, page_url):
        response = requests.get(page_url)
        page_soup = BeautifulSoup(response.content, 'html.parser')
        page_content = page_soup.find(class_="article-content")
        # print(page_content.prettify())
        article = ""
        img_url = ""
        for p_tag in page_content.find_all('p'):
            if p_tag.find('img'):
                img_url = "https:" + p_tag.find('img').get('src')
            article += (p_tag.text + '\n')
        return article, img_url

    def parse_hot_news(self):
        soup = self.parse_homepage()
        hot_news = soup.find(class_="csr_sketch_mix_hot")
        paragraphs = hot_news.find_all(class_="item")
        news = []
        for p in paragraphs[0:]:
            # print(p.prettify())
            id = p.find(class_="item-aid").text
            type = p.find(class_="item-addltype").text
            title = p.find(class_="item-title").text
            time = p.find(class_="item-time").text
            formatted_time = datetime.fromtimestamp(int(time)/1000).strftime('%Y-%m-%d %H:%M:%S')
            sub_title = p.find(class_="item-subtitle").text
            article_url = os.path.join(self.base_url, type, id)

            article, img_url = self.parse_subpage(page_url=article_url)
            news.append([id, type, formatted_time, title, article_url, img_url, article])
        news_df = pd.DataFrame(news, columns=['id', 'type', 'time', 'title', 'article_url', 'image_url', 'article'])
        return news_df



if __name__ == '__main__':
    today = datetime.today().strftime("%Y%m%d")
    news_df = HuanQiuSpider().parse_hot_news()
    news_df.to_csv(f"../../data/huanqiu_{today}.csv", index=False)
