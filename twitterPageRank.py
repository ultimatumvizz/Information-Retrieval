import tweepy
import time
 
# Consumer keys and access tokens, used for OAuth
access_token = '181450691-gAQeedXug0R6btS7UReC3FscYqzXXu5uDyt8lH2m'
access_token_secret = 'W0CePwUSHMCDz42v2mEFCpTBix89H6EOlq0EKsVz4JanA'
consumer_key = 'NyXjLxbcZj396IzSu2am8jXy8'
consumer_secret = 'ov4pcck1eudwJooMdENfrlJKn7CnzcQUFF17WZmWuNBYYHdAbG'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
#api.update_status("Hello Twitter")

sleeptime = 4
#pages = tweepy.Cursor(api.followers, screen_name="SrBachchan").pages()

user = api.get_user('SrBachchan')
print user.screen_name
print user.followers_count
#print user.followers

count = 1
users = tweepy.Cursor(api.followers, screen_name='SrBachchan').items()
inbound_link_array = []
print count
while True:
    count += 1
    print count
    try:
        user = next(users)
        time.sleep(sleeptime)
    except tweepy.TweepError:
        time.sleep(1)
        user = next(users)
    except StopIteration:
        break
    print  user.followers_count
    inbound_link_array.append(user.followers_count)

f = open("followers1.txt","w")
f.write(str(inbound_link_array))
f.close()   



"""
while True:
    try:
        page = next(pages)
        time.sleep(sleeptime)
    except tweepy.TweepError: #taking extra care of the "rate limit exceeded"
        time.sleep(60*15) 
        page = next(pages)
    except StopIteration:
        break
    for user in page:
       print(user.id_str)
       print(user.screen_name)
       print(user.followers_count) """
