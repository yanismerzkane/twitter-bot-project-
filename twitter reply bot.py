#importer les librairies 
import tweepy
import time

# Initialisation du code 
api_key = get_info("api_key")
api_secret_key = get_info("api_secret_key")
access_token = get_info("access_token")
access_token_secret = get_info("access_token_secret")
auth = tweepy.OAuthHandler(api_key, api_secret_key) #l'entrée des clés d'authentification de compte  twitter 
auth.set_access_token(access_token, access_token_secret) #l'entrée des clés d'authentification secrétes de compte twitter 
api = tweepy.API(auth)

# déclaration des variables a utiliser dans ce robot twitter 
bot_id = int(api.me().id_str) #creation de l'identifiant du robot de twitter et le convertir en entier 
mention_id = 1
words = ["why", "how", "when", "what", "?"]
message = "si vous avez des questions , n'hesiter pas a les envoyer "

# The actual bot
while True:
    mentions = api.mentions_timeline(since_id=mention_id) # trouver les tweets ( question) qu'on recherche
    # iteration a chaque tweet trouvé (qu'on recherche)
    for mention in mentions:
        print("tweet trouvé")
        print(f"{mention.author.screen_name} - {mention.text}") #imprimer le tweet trouvé
        mention_id = mention.id
       
      if mention.in_reply_to_status_id is None and mention.author.id != bot_id:    # Vérifier si le tweet trouvé n'est pas une réponse et nous ne sommes pas l'auteur
            if True in [word in mention.text.lower() for word in words]:           # Vérifier que le tweet trouvé contient l'un des mots de notre liste de mots (words) afin que nous puissions déterminer si le tweet pourrait être une question.
                try: 
                    #maintenant c'est la réponse 
                    print("Attempting to reply...") 
                    api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str)
                    print("Successfully replied :)")
                except Exception as exc:
                    print(exc) 
    time.sleep(15) #Le bot ne vérifiera les tweet que toutes les 15 secondes, sauf si vous modifiez cette valeur
