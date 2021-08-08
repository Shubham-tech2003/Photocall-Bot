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
