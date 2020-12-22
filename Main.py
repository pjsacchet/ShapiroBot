# Purpose of this script is to implement main functionailty
# This script will:
    # 1) Start threading objects for our emailing, texting, and our Discord bot
    # 2) Call functionality from Tweeter to wait for Ben Shapiro to tweet
    # 3) Upon recognizing tweet, will flip global flag that will signal all other flags to receive content and link of new tweet
    # 4) Each thread will carry out its separate functionality, pinging Adam and sending messages
    # 5} Wait for all threads to finish, log errors, and return to 1

# Import native libraries and additional modules needed
import threading
import os
import logging

# Import personal libraries
import Email
import Tweeter
import TextMessage
import DiscordBot

# Use this variable as a flag to tell other running threads when to execute, and what with
SHAPIRO_TWEETED = False
TWEET_CONTENT = ""
TWEET_LINK = ""
# Name of our log for other modules to use
LOG_NAME = "SHAPIROLOG.log"

def main():
    # Create logger and log startup
    global LOG_NAME
    logging.basicConfig(filename=LOG_NAME, level=logging.DEBUG)
    logging.info("Starting Shapiro bot setup...")

    msg = TextMessage.TextMessage()
    msg.content = "LOL loser"
    msg.SendMessage()



if __name__ == '__main__':
    # Create threads for separate tasks
    main()
