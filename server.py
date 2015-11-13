import config
import requests
from requests_oauthlib import OAuth1

class TweetFetcher():
    def __init__(self, consumer_key, consumer_secret, access_token,
                 access_token_secret):
        self.auth = OAuth1(consumer_key, consumer_secret, access_token,
                           access_token_secret)
        self.session = requests.Session()
    def fetch_by_user()



if __name__ == '__main__':
    main()
