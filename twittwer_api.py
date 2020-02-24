 # Holds the twitter API keys in a GITIGNORED file
import keys
# Imports the tweepy library
import tweepy


auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth)

def Get_twitter(hashtag): #return the text message in a list
    #get the hashtages or handles for the function
    tag = hashtag + ' -filter:retweets'

    text = []
    #search the entire tweets in English, filter out the retweets. the number of the tweets is 10.
    for tweet in tweepy.Cursor(api.search, q=tag, tweet_mode='extended', lang='en').items(10):
    # add the texts to the list
        text.append(tweet.full_text)
    return text