import tweepy

def lambda_handler(event, context):

    # grumpy twitter account
    CONSUMER_KEY = "yLIi0DRVcq0EmM9aqBfKuMGlt"
    CONSUMER_SECRET = "vxgoBxh9vTi0rexMMWVZfitzQxq4QIDR04MqUoVnMOwI6yr741"
    ACCESS_TOKEN = "1225580764789497857-iIIzE0LP09szc2OCQ68MjvDrr2HMTD"
    ACCESS_SECRET = "HG7A7txr2AqDF7qfviFK1NiR71J2druFT3F5MrgH442Di"

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    #search_results = api.search(q="フォロー RT 応募 OR @9999 -filter:retweets -filter:replies filter:verified", count=10)
    #search_results = api.search(q="フォロー RT 応募 filter:verified") #他人へのリプライに対してもRTしてしまっている
    search_results = api.search(q="フォロー RT 応募 filter:verified -filter:replies")

    for result in search_results:
        tweet_id = result.id
        user_id = result.user._json['id']
        print(tweet_id)
        try:
            #api.create_favorite(tweet_id)
            api.create_friendship(user_id)
            api.retweet(tweet_id)
            print(user_id)
        except Exception as e:
            print(e)

lambda_handler("","")