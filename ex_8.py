import tweepy
from tweepy import OAuthHandler

consumer_key = 'kTZPJn7prgdgYgGrHj9FK426c'
consumer_secret = 'Dtcsw76IQJH2ZoSVFvhSmclUjajfG9lXeOoPJVk3B4QCBE7stm'
access_token = '834743958056099842-mKfn6QGKqzgs2CjrTQr0AlZCo6t28rJ'
access_secret = 'Bc2UGihhwVpPs2TgEUq6e5bLG18OYRewhPT1p1mq4i7cR'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
print "I'm using python to mine twitter!"
# Get a list of followers of a particular user

name1=raw_imput("Give name of 1st user you want--->")
name2=raw_imput("Give name of 2nd user you want--->")


twitter.followers.ids(screen_name=name1)
twitter.followers.ids(screen_name=name2)
