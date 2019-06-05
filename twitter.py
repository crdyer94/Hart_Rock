import os
import tweepy
import requests


TWITTER_CONSUMER = os.environ.get('TWITTER_CONSUMER')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS = os.environ.get('TWITTER_ACCESS')
TWITTER_ACCESS_SECRET = os.environ.get('TWITTER_ACCESS_SECRET')


auth = tweepy.auth.OAuthHandler(TWITTER_CONSUMER, TWITTER_CONSUMER_SECRET)
auth.secure=True
auth.set_access_token(TWITTER_ACCESS, TWITTER_ACCESS_SECRET)

api = tweepy.API(auth)



def get_tweets(name1, name2):
    """Gets the user's tweets from Twitter"""
    twitter_owners = [name1, name2]
    tweets = []

    for owner in twitter_owners:
        screen_name = get_screen_name(owner)

        twitter_objects = api.user_timeline(screen_name=screen_name,
                                            trim_user="true",
                                            include_rts="false",
                                            exclude_replies="true",
                                            count=10)
        for twitter_object in twitter_objects:

            tweet_object = twitter_object._json
            tweet = tweet_object["text"]

            tweets.append(tweet)


    return tweets


def get_screen_name(name):
    """Gets the user's twitter from the Twitter API"""
    
    twitter_user_object = api.search_users(q=name, count=1)[0]

    twitter_user_information = twitter_user_object._json

    twitter_screen_name = twitter_user_information.get("screen_name")


    return twitter_screen_name