import os
import shutil

from flask import Flask, redirect, render_template, url_for, request
from instabot.bot.bot import Bot

import tweepy

app = Flask(__name__)
post_desc = input("Desc: ")

class TwitterAPI:
    consumer_key = "GgQb87lg23UM4dCBDU47NrLPG"
    consumer_secret = "jlJmy14zU0VW5xk57JiAt2qQxsW9z6tic7HCVNgm88C3HCdbD6"
    key = "1418207837277200392-VuJhk3Hrs1HAJYLBMiK4vxrqPKOr6V"
    secret = "Eu9ITJQ1qMLTz7bgT2MVbq2RFytpGdHHDav1SGMUrcWS8"

class InstaDetails:
    instagram_username = "demoforproject"
    instagram_password = "Shubham2003"


"""

while i <= int(accounts_number):
    account_type = input(f"Account {i} type: ")
    account_name = input(f"Account {i} name: ")
    account_password = input(f"Account {i} password: ")
    if(account_type == "tweet"):
        tweet_pc = input(f"Tweet picture filename (ex: picture.png) for account {i}: ")
        consumer_key = input(f"Twitter API consumer key for account {i}: ")
consumer_secret = input(f"Twitter API consumer secret key for account {i}: ")
        key = input(f"Twitter API access token for account {i}: ")
        secret = input(f"Twitter API access token secret for account {i}: ")
        consumer_keys.append(consumer_key)
        consumer_secrets.append(consumer_secret)
        keys.append(key)
        secret_keys.append(secret)
        tweet_pics.append(tweet_pic)
        instagram_pics.append("")
    elif(account_type == "insta"):
        insta_pic = input(f"Instagram post picture filename (ex: picture.png) for account {i}: ")
        instagram_pics.append(insta_pic)
        consumer_keys.append("")
        consumer_secrets.append("")
        keys.append("")
        secret_keys.append("")

    accounts.append(account_name)
    passwords.append(account_password)
    accounts_type.append(account_type)
    i += 1

"""



def PostTwitter(consumer_key, consumer_secret, key, secret, filename, post_description):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)

    api = tweepy.API(auth)

    api.update_with_media(f"TwitterPhoto/{filename}", post_description)

    mentions = api.mentions_timeline()

    for mention in mentions:
        print(str(mention.id) + " - " + mention.text)
        
        
    
    def PostInstagram(username, password, filename, post_description):
    bot = Bot()
    import time
    time.sleep(2)
    bot.login(username=username, password=password)

    bot.upload_photo(f"InstaPhoto/{filename}", caption=post_description)
