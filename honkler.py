import tweepy

consumer_key = "s2pEDUSe4SSTbSTlZaSlhwuzc"
consumer_secret = "27UYlhuitB7ZhbDzxjje5Yhhpn0Zasw1LNdHMpqMO1iARfbRM0"
access_token_key = "4737013222-GR5djR0ngZNslfkLbPAokMcaMgMBf9GkIrLVHzN"
access_token_secret = "gZTSN4v5Kg70Fnc9a2ruNjzsimVY55JZxxb1bkhbVp7Zr"

# consumer_key = 'consumer key'
# consumer_secret = 'consumer secrets'
# access_token = 'access token'
# access_token_secret = 'access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)


user = api.me()
print(user.name)

for friend in user.friends():
    print(friend)

