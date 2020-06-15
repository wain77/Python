#! python3
import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='jn-FDYP_jou3PQ',
                     client_secret='sOpLGWntK6vC9r-3LVZMznAQqLE',
                     user_agent='windows:PRAWTesting:v1.0.0',
                     username='wain77',
                     password='i9CYMQytzs')


##subredditName = input('Please enter the displayname of the subreddit you want to scrape: ')
##subreddit = reddit.subreddit(subredditName)
##
##subredditTop = subreddit.top(time_filter='day', limit=10)
##
##for submission in subredditTop:
##    print('Title:',submission.title)

inbox = reddit.inbox
messages = []

for message in inbox.messages():
    messages.append(message)
