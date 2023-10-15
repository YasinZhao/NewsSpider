import pandas as pd
import time
from datetime import datetime

from spider.news.huanqiu import HuanQiuSpider
from spider.news.reuters import ReutersSpider
from twitter_api_service import TwitterClient

today = datetime.today().strftime("%Y%m%d")


def main():
    news_df = pd.DataFrame()
    huanqiu_news_df = HuanQiuSpider().parse_hot_news()
    reuters_news_df = ReutersSpider().parse_hot_news()

    news_df = pd.concat([news_df, huanqiu_news_df, reuters_news_df]).reset_index(drop=True)
    news_df.to_csv(f"data/news_{today}.csv", index=False)
    # print(news_df)

    for i in range(news_df.shape[0]):
        article_title = news_df.loc[i, 'title']
        article_url = news_df.loc[i, 'article_url']
        # article = news_df.loc[i, 'article']
        # article_summary = article.split('\n')[0]

        tweets = f"{str(article_title)} {str(article_url)}"
        # print(tweets)
        try:
            TwitterClient().post_tweets(tweets=tweets)
            time.sleep(15)
        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':
    main()