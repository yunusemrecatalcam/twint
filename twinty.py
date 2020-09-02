import twint
import requests

def lets_ban_together():

    c = twint.Config()
    c.Search = "from:gabeviveros3"
    c.Store_object = True
    c.Limit = 20
    twint.run.Search(c)
    tlist = twint.output.tweets_list
    print(tlist)

lets_ban_together()

c = twint.Config()
c.Username = 'gabeviveros3'
c.User_id = 'randomstring'
c.Limit = 20
twint.run.Search(c)
c = twint.Config()
c.Username = 'gabeviveros3'
c.Store_object = True
c.Store_object_users_list = []
c.User_full = True
c.User_id = None
twint.run.Lookup(c)
user_info = c.Store_object_users_list[0]

c = twint.Config()
c.Search = "from:gabeviveros3"
c.Store_object = True
c.Limit = 20
twint.run.Search(c)
tlist = twint.output.tweets_list

c = twint.Config()
c.Username = "riotgames"
c.User_id = tlist[0].user_id
c.Store_object = True
c.Limit = 20
twint.run.Favorites(c)
tweets_fav = c.favorited_tweets_list

c = twint.Config()
c.Username = "riotgames"
c.User_id = tlist[0].user_id
c.Store_object = True
c.Limit = 20
twint.run.Following(c)
followings = twint.output.follows_list
twint.output.follows_list = []

c = twint.Config()
c.User_id = tlist[0].user_id
c.Username = "riotgames"
c.Limit = 20
c.Store_object = True
twint.run.Followers(c)
followers = twint.output.follows_list
twint.output.follows_list = []

session = requests.Session()
rx = session.get('https://twitter.com/LeagueOfLegends')
print('take a ride')