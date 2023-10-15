import os
import json
import yaml
import requests
from requests_oauthlib import OAuth1Session


class TwitterClient:
    def __init__(self):
        with open("config/twitter_api.yaml", "r") as f:
            config = yaml.safe_load(f)
        self.consumer_key = config['twitter-api']['consumer_key']
        self.consumer_secret = config['twitter-api']['consumer_secret']
        self.bearer_token = config['twitter-api']['bearer_token']
        self.access_token = config['twitter-api']['access_token']
        self.access_token_secret = config['twitter-api']['access_token_secret']
        self.client_id = config['twitter-api']['client_id']
        self.client_secret = config['twitter-api']['client_secret']

    def create_client(self):
        oauth_client = OAuth1Session(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=self.access_token,
            resource_owner_secret=self.access_token_secret,
        )
        return oauth_client

    def post_tweets(self, tweets):
        oauth_session = self.create_client()
        payload = {
            "text": tweets
        }
        response = oauth_session.post(url="https://api.twitter.com/2/tweets", json=payload)
        print(response.json())


if __name__ == '__main__':
    TwitterClient()




