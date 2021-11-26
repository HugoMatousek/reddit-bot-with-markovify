# imports
from re import sub
from types import ClassMethodDescriptorType
import praw
import random
import datetime
import time
import os
import markovify
from praw.reddit import Submission, Subreddit

# set path to the location of the script
path = os.path.dirname(__file__)

# read data for Markov chain model
content = ''
with open(path+'/model_data.txt', 'r', encoding='utf-8') as file:
     content = file.read()

# create Markov chain model using the data in content 
model = markovify.Text(content)

# starting words for sentences
starting_points = ['Biden', 'Sleepy Joe', 'Hillary', 'Democrats', 'Republicans', 'GOP', 'Trump', 'I think',]

# signature that will be added to the end of the self posts
signature = '''  
    --------  
    I am a bot that is based on the tweets and speeches of Donald J. Trump. [Github link.](https://github.com/HugoMatousek/reddit-bot-with-markovify)'''        

# start praw
reddit = praw.Reddit('bot1', user_agent='cs40')

# select subreddit where submissions will be posted
subred = 'BotTown_polibot2'

# endless loop, each iteration posts a submission
while True:

    # randomy choose between the three option: 0) self post using markov chain, 1) manual repost, 2) reddit repost
    i = random.randint(0,2)

    # self post using markov chain
    if i == 0:
        subreddit = reddit.subreddit(subred)
        subreddit.submit(model.make_sentence_with_start(random.choice(starting_points),strict = False), (model.make_sentence() + ' ' + model.make_sentence() + signature))
        print('posted markov')

    # manual repost taking title and text or url from a random submisson from a selected subreddit
    if i == 1:
        subreddit = reddit.subreddit('conservative')
        submission = subreddit.random()
        title = str(submission.title)
        content = str(submission.selftext)
        url = str(submission.url)

        subreddit = reddit.subreddit(subred)

        # posted checks to make sure that the bot has not posted the same submission in the past (based on title)
        posted = False
        for post in reddit.redditor("polibot-cs40").submissions.new(limit=None):
            if str(post.title) == title:
                posted = True
        # if the same post has been posted in the past, start new iteration
        if posted:
            continue 

        # checks whether the selected submission is a self post or link
        if len(content) != 0:
            subreddit.submit(title,content)
        elif 'reddit' not in url:
            subreddit.submit(title,url=url)

        print('posted from other')

    # reddit repost
    if i == 2:
        subreddit = reddit.subreddit('conservative')
        submission = subreddit.random()  

        # checks for already posted submission, see above
        posted = False
        for post in reddit.redditor("polibot-cs40").submissions.new(limit=None):
            if str(post.title) == str(submission.title):
                posted = True
        if posted:
            continue        

        submission.crosspost(subreddit=subred,send_replies=False)     
        print('posted repost') 

    # sleep the bot for a random number of seconds
    sleep = random.randint(10,20)   
    print('sleep for: ',sleep)
    time.sleep(sleep)





