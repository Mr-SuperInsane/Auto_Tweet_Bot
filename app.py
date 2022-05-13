import tweepy
#import schedule
#from time import sleep

BEARER_TOKEN = ''
API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

client = tweepy.Client(BEARER_TOKEN,API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
client.create_tweet(text='ツイートしたいメッセージ')

'''
def tweet():
    client = tweepy.Client(BEARER_TOKEN,API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    client.create_tweet(text='ツイートしたいメッセージ')

#herokuにデプロイする場合「ツイートしたい時刻 - 9時間」した時刻を書いてね
schedule.every().day.at("23:00").do(tweet)
while True:
    schedule.run_pending()
    sleep(1)
'''