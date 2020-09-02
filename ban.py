import twint
from multiprocessing import Process
import multiprocessing

def lets_ban_together():

    c = twint.Config()
    c.Search = "grafana"
    c.Store_object = True
    c.Limit = 100
    c.Proxy_host = "tor"
    c.Proxy_port = 9300
    twint.run.Search(c)
    tlist = twint.output.tweets_list
    print("tlist")


while True:

    lets_ban_together()
    print("hacked that out")