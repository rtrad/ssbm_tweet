import config
import json
import player_info
import requests
from dao import MongoDao
from requests_oauthlib import OAuth1
from vaderSentiment.vaderSentiment import sentiment as vader


class TweetFetcher():

    def __init__(self, consumer_key=config.consumer_key,
                 consumer_secret=config.consumer_secret,
                 access_token=config.access_token,
                 access_token_secret=config.access_token_secret):
        self.auth = OAuth1(consumer_key, consumer_secret, access_token,
                           access_token_secret)
        self.session = requests.Session()
        self.db_interface = MongoDao()

    def fetch_by_users(self, twitter_handles):
        params = {'track' : ",".join(['@' + h for h in twitter_handles])}
        stream = self.session.post(url=config.api_url, auth=self.auth,
                                   data=params, stream=True)
        for line in stream.iter_lines():
            if line:
                print 'record found'
                post = json.loads(line)
                post.update(self._compute_sentiment(post['text']))
                self.db_interface.insert(post)
                print 'inserted record from {}'.format(post['user']['screen_name'])

    def _compute_sentiment(self, text):
        return vader(text.encode('utf8'))

if __name__ == '__main__':
    fetcher = TweetFetcher()
    players = player_info.player_dict.values()
    fetcher.fetch_by_users(players)