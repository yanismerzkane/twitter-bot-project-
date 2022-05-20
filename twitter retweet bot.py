# Importer les librairies et les modules 
import tweepy
from textblob import TextBlob
import time
#on utilsie la librairie textblob pour traiter les données contextuelles et décider si un tweet est positif ou négatif
# Initialization
api_key = get_info("api_key")
api_secret_key = get_info("api_secret_key")
access_token = get_info("access_token")
access_token_secret = get_info("access_token_secret")
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Getting Bot ID
bot_id = int(api.me().id_str)

mention_id = 1

# Retweet Bot with Mentions
while True:
    mentions = api.mentions_timeline(since_id=mention_id)
    for mention in mentions:
        print("Mention Tweet found!")
        print(f"MENTION: {mention.author.screen_name} - {mention.text}")
        mention_id = mention.id
        mention_analysis = TextBlob(mention.text)
        mention_analysis_score = mention_analysis.sentiment.polarity
        print(f"Tweet has polarity score of {mention_analysis_score}")
        if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
            if mention_analysis_score >= 0.3 and not mention.retweeted:
                try:
                    print("trying retweet...")
                    api.retweet(mention.id)
                    print("Tweet successfully retweeted!\n")
                except Exception as err:
                    print(err)
            else:
                print("Tweet will not be retweeted.\n")
    time.sleep(15)
