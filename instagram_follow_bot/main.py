from instabot import InstaBot
import os
import time

# --------CONSTANTNS--------
username = os.environ.get("username")
password = os.environ.get("password")
INSTA_ACC_TO_GET_FOLLOWERS = "ANY INSTA ACCOUNT"

bot = InstaBot()
bot.login(username,password)
time.sleep(2)
bot.find_followers(INSTA_ACC_TO_GET_FOLLOWERS)
time.sleep(2)
bot.follow()