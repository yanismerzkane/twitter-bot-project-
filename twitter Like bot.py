#importer les librairies et les modules 
import tweepy
# Initialisation et authentification
api_key = get_info("api_key")
api_secret_key = get_info("api_secret_key")
access_token = get_info("access_token")
access_token_secret = get_info("access_token_secret")
auth = tweepy.OAuthHandler(api_key, api_secret_key)  #l'entrée des clés d'authentifications
auth.set_access_token(access_token, access_token_secret) #l'entrée des clés d'authentification secrétes
api = tweepy.API(auth)

# Creation d'un ecouteur de flux(tweet)
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, tweet): #permet de retrouver les tweets que nous cherchons 
        print("Tweet Found!") #tweet trouvé 
        print(f"TWEET: {tweet.author.screen_name} - {tweet.text}") #imprimer l'auteur du tweet ainsi que le tweet
        if tweet.in_reply_to_status_id is None and not tweet.favorited: #permet de vérifier si le tweet n'est pas une réponse a un autre tweet et que les tweet n'est pas déja liker 
            try:
                print("Attempting like...")
                api.create_favorite(tweet.id) #permet de liker le twwet 
                print("Tweet successfully liked :)")
            except Exception as err:
                print(err)

#creation d'une instance de l'ecouteur de flux(tweet)
stream_listener = MyStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["Python"], languages=["en"]) #permet de trouver les tweets q'on recherche ' ici par exemple on cherche les tweets en anglais qui contiennet le mot clé Python
