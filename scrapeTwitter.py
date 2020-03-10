#tweepy is accessed through twitter dev api
import tweepy 
import time 

# Authenticate to Twitter

consumer_key = "v6s8XoRvcyztT0c943MI0upaZ"
consumer_secret = "83aps60heRgWAWKHr4kfhakXh4PcylbO0dBHRRPDqeuYcRKiSq"
access_token = "2839069588-FEHe8nHmf1W81MIPkeo7CkNEegqHuq6yzZuGnjD"
access_token_secret = "1lstY1oh1S25ecKUdwteTxTnkbskBeEzIahFcwHJKDMdK"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret) 

# Create API object
api = tweepy.API(auth)

# Create a tweet
#api.update_status("Hello Tweepy")

api = tweepy.API(auth,wait_on_rate_limit=True)

tweets = []
username = '@realDonaldTrump'#'@kaylavangorder'
count = 100
try: 
# Pulling individual tweets from query
	for tweet in api.user_timeline(id=username, count=count):
# Adding to list that contains all tweets
		tweets.append((tweet.created_at,tweet.id,tweet.text))
		print(tweet.text) 
except BaseException as e:
      print('failed on_status,',str(e))
      time.sleep(3)
      
