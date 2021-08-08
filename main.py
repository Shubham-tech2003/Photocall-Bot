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
