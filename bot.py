# imports
from re import sub
from types import ClassMethodDescriptorType
import praw
import random
import datetime
import time
import os
import markovify

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

# function to generate comments using Markov chain/markovify library
def generate_comment():
    comment = ''

    #choose randomly between three types of comments
    i = random.randint(0,3)

    # 1-4 markov chain sentences
    if i == 0:
        for j in range(0,random.randint(1,4)):
            comment = comment + model.make_sentence() + ' '
    
    # Markov chain sentence with a random starting point from the list
    if i == 1:
        comment = comment + model.make_sentence_with_start(random.choice(starting_points), strict=False) 

    # 1-3 markov chain sentences with a starting point from the list    
    if i == 2:
        for j in range(0,random.randint(1,3)):
            comment = comment + model.make_sentence_with_start(random.choice(starting_points), strict=False) + ' '

    # combination of 1-3 markov chain sentences with a starting point from the list + 1-4 markov chain sentences (for longer comments)        
    if i == 3:
        for j in range(0,random.randint(1,3)):
            comment = comment + model.make_sentence_with_start(random.choice(starting_points), strict=False) + ' '
        for j in range(0,random.randint(1,4)):
            comment = comment + model.make_sentence() + ' '

    # signature stating that this is a bot (ideally, figure out a better Markdown formatting, reddit seems to ignore parsing characters with praw)
    signature = '''  
    --------  
    I am a bot that is based on the tweets and speeches of Donald J. Trump. [Github link.](https://github.com/HugoMatousek/reddit-bot-with-markovify)'''        

    comment = comment + signature

    # return generated comment
    return(comment)

# dic with all the bots' configuration in praw.ini and their respected reddit username
bot_list = {'bot1':'polibot-cs40','bot2':'polibot-cs40_1','bot3':'polibot-cs40_2','bot4':'polibot-cs40_3','bot5':'polibot-cs40_4'}

# endless loop that should post a comment/reply each iteration
while True:

    # randomly chose a bot 1-5 and save its reddit username to bot_name
    bot = 'bot' + str(random.randint(1,5))
    bot_name = bot_list[bot]

    print('\n')

    # identify which bot will be used for the next iteration
    print('bot: '+bot + ' \nbotname: ' + bot_name)    

    # start praw/reddit with the given bot
    reddit = praw.Reddit(bot, user_agent='cs40')

    # mainly for hitting rate limit or other unexpected mistake    
    try:

        # choose a subreddit to which you will be posting
        subreddit = reddit.subreddit("BotTown_polibot2")

        # TASK 5 - COMPLETED
        # choosing a random submission, here you can select which submissions the bot should be contributing to
        # currently, it loads the 'hottest' ten (including the sticky submissions) and selects the first five not sticky
        num_sub = 0
        sub_list = []
        for submission in subreddit.hot(limit=20):
            print(submission.title)
            if not submission.stickied: 
                sub_list.append(submission)
                num_sub += 1
            if num_sub == 5:
                break
        
        # chooses a random submission from the list generated above
        submission = random.choice(sub_list)

        # printing the current time will help make the output messages more informative
        print('new iteration at:',datetime.datetime.now())
        print('submission.title=',submission.title)
        print('submission.id=',submission.id)
        print('submission.url=',submission.url)

        # TASK 0, TASK 1 - COMPLETED
        # load all comments in a submission
        submission.comments.replace_more(limit=None)

        # lists for all comments and list of comments not posted by the bot
        all_comments = []
        not_my_comments = []

        # iterate over all comments
        for comment in submission.comments.list():
            # add a comment to all_comments unless it was deleted (author == None)
            if str(comment.author) != 'None':
                all_comments.append(comment)
            # add a comment to not_my_comments unless by the not (author == bot_name)
            if str(comment.author) != bot_name:
                not_my_comments.append(comment)

        # print the num of all/not_my_comments
        print('len(all_comments)=',len(all_comments))
        print('len(not_my_comments)=',len(not_my_comments))

        # checks whether the two are the same and saves as True/False, if so, it means that no comment in the submission is by the bot
        has_not_commented = len(not_my_comments) == len(all_comments)

        # TASK 2 - COMPLETED
        # if not comment has been posted to the submission, submit a new top-level comment 
        if has_not_commented:
            submission.reply(generate_comment())

        # if already commented, try to find a comment to which the bot has not replied yet and reply to it
        else:

            #TASK 3 - COMPLETED
            comments_without_replies = []
            for comment in not_my_comments:

                # check for the replies to the selected comment
                child_comments = comment.replies
                # if not replies have been posted, the bot has not replied to it and so it can in this iteration, add to the list
                if len(child_comments) == 0:
                    comments_without_replies.append(comment)
                # if there are replies to the comment, check if one of them is of the bot
                else:
                    # assume the bot has not replied to the comment
                    no_replies = True
                    # check all the replies                    
                    for child_comment in child_comments:
                        # check if the both is the author of the reply, if so, correct the assumption
                        if child_comment.author == bot_name:
                            no_replies = False
                    # if none of the replies is authored by the bot, add this reply to the list of possible comments to reply to
                    if no_replies == True:        
                        comments_without_replies.append(comment)
            # print the number of comments that the not can reply to
            print('len(comments_without_replies)=',len(comments_without_replies))

            # TASK 4 - COMPLETED
            # pick one of the comments that the bot can reply to and reply to it
            try:
                # sort the comments by the number of upvotes
                comments_without_replies.sort(key=lambda comment: comment.score, reverse=True)
                # reply to most upvoted comment
                comments_without_replies[0].reply(generate_comment())
                # random pick alternative
                #random.choice(comments_without_replies).reply(generate_comment())
            # if there are not comments to reply to, print the info and the error and continue without replying
            except Exception as e:
                print('ERROR: There are probably no comments without replies. The full error:\n' + str(e))

        # randomly generate a waiting time, print this info        
        wait_time = random.randint(20,60)
        print('wait_time= ', wait_time)
        time.sleep(wait_time)

    # in case of the exception (likely hitting the rate limit) print the error and employ waiting
    # !!! this portion was done before expanding the script into multi-bot script, currently, this is not an efficient solution
    # probably, the more efficient would be to completely remove this
    # however, if I have time later, I will update it so that it iterates over the other bots and only waits if all the bots hit the rate limit
    # in posting more than 6000 comments, the rate limit was not hit once, so there is no pressure on fixing this
    # especially since it makes sure that the code keeps running even if some other problem occurs
    except Exception as e:

        print('ERROR: ' + str(e))
        sec = 0
        # try to parse the error message for the time needed to wait
        try:
            sec = int(str(e)[str(e).find('for ')+4:str(e).find(' ', str(e).find('for ')+4)])
            if 'seconds' in str(e):
                pass
            else:
                sec = sec*60
            print('wait for ' + str(sec))
            time.sleep(sec)
        except:
            pass