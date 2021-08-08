import os
import shutil

from flask import Flask, redirect, render_template, url_for, request
from instabot.bot.bot import Bot

import tweepy