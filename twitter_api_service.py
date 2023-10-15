import os
import json
import requests
from requests_oauthlib import OAuth1Session


class TwitterClient:
    def __init__(self):
        self.consumer_key = "Mq8IiiRrUnGsxV0wGjbF0upe5"
        self.consumer_secret = "sUQmuCzABCoV2CYTW4zmUCJcL76O9m8YYNmc2kFFbrnmbOEDLX"
        self.bearer_token = "AAAAAAAAAAAAAAAAAAAAAH36qQEAAAAA1D0z0rruIRVULQPK5W0Y9rG148s%3D0paTwokB5c8HlGqF41m9zRkgV0G19AV7OmW4VULAiiHLpyM5O3"
        self.access_token = "1712790134725427200-I6lK0eNlLOdA6LYEQUW8VTqmhiT0rr"
        self.access_token_secret = "MwdMhqtfqizQgFEup2XytCyFLP6oXeomDQVAbddnUqdQD"
        self.client_id = "MWMyYzBYc3JGcHZCOVd1aHFvTE06MTpjaQ"
        self.client_secret = "aKHvdu1DfuxPfKvj0WlnY4XYPDTuGmGHlNWkxLYGKH4HrUYhJT"

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
    TwitterClient().post_tweets()




