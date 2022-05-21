# Importer les librairies et les modules 
import tweepy
from textblob import TextBlob
import time
#on utilsie la librairie textblob pour traiter les données contextuelles et décider si un tweet est positif(qui nous mentionne de facon positif) ou négatif(qui nous mentionne de facon négtatif)
# Initialisation 
api_key = get_info("api_key")
api_secret_key = get_info("api_secret_key")
access_token = get_info("access_token")
access_token_secret = get_info("access_token_secret")
#entreé des clés d'authentification 
auth = tweepy.OAuthHandler(api_key, api_secret_key) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#l'idientifiant du bot ( nous meme)
bot_id = int(api.me().id_str) 

mention_id = 1

# Retweet bot qui nous mentionne 
while True:
    mentions = api.mentions_timeline(since_id=mention_id) #permet de lister touts les tweets qui nous mentionne
    for mention in mentions: #iteration a chaque tweet qui nous mentionne
        print("Mention Tweet found!") #tweet qui nous mentionne trouvé
        print(f"MENTION: {mention.author.screen_name} - {mention.text}")     #  imprimer le tweet qui nous mentionne
        mention_id = mention.id  #cela impeche d'imprimer toujours le meme tweet mentionné
        mention_analysis = TextBlob(mention.text) #permet de tester si le tweet mentionné est positif ou négatif 
        mention_analysis_score = mention_analysis.sentiment.polarity  #permet de calculer approximativement le score (a quel point le tweet est positif ou négatif)
        print(f"Tweet has polarity score of {mention_analysis_score}") #permet d'imprimer le score dans lequel le tweet mentionné est positif ou négatif
        if mention.in_reply_to_status_id is None and mention.author.id != bot_id: #on vérifie si le tweet n'est pas un réponse a un autre tweet et que l'auteur du tweet n'est pas nous meme 
            if mention_analysis_score >= 0.3 and not mention.retweeted: #permet de vérifier si le score d'analyse >=0.3 (tweet positif pour le retweeter) et que le tweet n'est pas déja retweeté
                try:
                    print("trying retweet...")
                    api.retweet(mention.id) #retweeter le tweet 
                    print("Tweet successfully retweeted!\n")
                except Exception as err:
                    print(err)
            else: #si le tweet est négatif
                print("Tweet will not be retweeted.\n")
    time.sleep(15)  #Le bot ne vérifiera les tweets qui nous mentionne  toutes les 15 secondes, sauf si on modifie la valeur

