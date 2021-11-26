# imports
import praw
import random
from textblob import TextBlob
import time

# keeps track of votes casted (apporximately, does not account for trying to vote on one sub/comment multiple times)
sub_votes = 0
com_votes = 0

# set bot's name for easy change later
bot_name = 'polibot-cs40_1'

# start reddit/praw
reddit = praw.Reddit('bot2', user_agent='cs40')

# define "negative" and "postive" politicans for upvoting for negative sentiment and downvoting for positive sentiment and vice versa, respectively
neg_list = ['Biden', 'Joe', 'Hillary', 'Clinton', 'Democrats', 'Bernie', 'AOC', 'Democrat',]
pos_list = ['GOP', 'Republican', 'Marco Rubio', 'Pence']

# run forever, check one comment/submission each iteration
while True:
    # choose a subreddit in which you will be voting
    subreddit = reddit.subreddit('BotTown2')

    # load all submissions
    submissions = subreddit.new(limit=None)

    # create a list of submissions as some subreddits have .random() blocked
    sub_list = []
    for each in submissions:
        sub_list.append(each)

    # choose a random subreddit
    submission = random.choice(sub_list)

    # choose randomly between evaluating a submission or a comment
    i = random.randint(0,1)

    # used for tracking a successful vote (applies to all mentiones of temp below)
    temp = 0    

    # evaluate a submission
    if i == 0:
        # get the title of the submission and print it with its id
        title = str(submission.title)
        print('submission: ' + title + '\nid: ' +str(submission.id))

        # check for people from the "negative" list being mentioned if present, print a confirmation and get sentiment
        if any(x in title for x in neg_list):
            print('`negative` politican present')
            sent = TextBlob(title)
            polar = sent.sentiment.polarity
            print('sentiment: ', sent.sentiment)

            # based on sentiment.polarity up/downvote the submission
            if polar < 0:
                submission.upvote()
                print('upvoted with sentiment:', polar )
                temp +=1
            if polar > 0:
                submission.downvote()
                print('downvoted with sentiment: ', polar)
                temp +=1
        # check for people from the "positive" list being mentioned if present, print a confirmation and get sentiment
        if any(x in title for x in pos_list):
            print('`positive` politican present')
            sent = TextBlob(title)
            polar = sent.sentiment.polarity
            print('sentiment: ', sent.sentiment)

            # based on sentiment.polarity up/downvote the submission
            if polar > 0:
                submission.upvote()
                print('upvoted with sentiment:', polar )
                temp +=1
            if polar < 0:
                submission.downvote()
                print('downvoted with sentiment: ', polar)
                temp +=1
        
        # if one vote was casted (meaning more than none and less than 2 which would cancel out each other), increase vote count on submissions
        if temp == 1:
            sub_votes += 1

    if i == 1:
        # get all comments within a submission
        submission.comments.replace_more(limit=None)

        # check for only comments by other people
        not_my_comments = []
        for comment in submission.comments.list():
            # add a comment to not_my_comments unless by the not (author == bot_name)
            if str(comment.author) != bot_name:
                not_my_comments.append(comment)

        # if there are no usable comments, skip iteration
        if len(not_my_comments) == 0:
            print('no comments here yet')
            continue
        
        # pick a random comment from the usable comments
        comment = random.choice(not_my_comments)

        # get the body of the comment, print it, and print the comment and submission id's
        text = str(comment.body)
        print('comment: ' + text + '\nid_sub: '+ str(submission.id) + ' id_comment: '+str(comment.id))
        # check for people from the "negative" list being mentioned if present, print a confirmation and get sentiment
        if any(x in text for x in neg_list):
            print('`negative` politican present')
            sent = TextBlob(text)
            polar = sent.sentiment.polarity
            print('sentiment: ', sent.sentiment)
            
            # based on sentiment.polarity up/downvote the comment
            if polar < 0:
                comment.upvote()
                print('upvoted with sentiment:', polar )
                temp +=1
            if polar > 0:
                comment.downvote()
                print('downvoted with sentiment: ', polar)
                temp +=1

        # check for people from the "positive" list being mentioned if present, print a confirmation and get sentiment
        if any(x in text for x in pos_list):
            print('`positive` politican present')
            sent = TextBlob(text)
            polar = sent.sentiment.polarity
            print('sentiment: ', sent.sentiment)

            # based on sentiment.polarity up/downvote the comment
            if polar > 0:
                comment.upvote()
                print('upvoted with sentiment:', polar )
                temp +=1
            if polar < 0:
                comment.downvote()
                print('downvoted with sentiment: ', polar)
                temp +=1

        # if one vote was casted (meaning more than none and less than 2 which would cancel out each other), increase vote count on comments
        if temp == 1:
            com_votes +=1


    # sleep for a random amount of time and print this amount on the screen
    sleep_time = random.randint(10,20)
    print('sub votes: ', sub_votes)
    print('com votes: ', com_votes)
    print('waiting for: ',sleep_time)
    time.sleep(sleep_time)



