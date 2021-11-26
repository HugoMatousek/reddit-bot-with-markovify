# reddit-bot-with-markovify
## General Info
This project was done as a homework for CMC's [CSCI40 course](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_04). The project's goal was to create a reddit bot that would post comments and/or submissions about a chosen politican. Given that I have decided to employ [`markovify`](https://github.com/jsvine/markovify) library to generate my comments and used Trump's tweets and speeches as my learning data set, the comments are "as if written by Trump" talking about various topics (including himself and other politicans).  
The project consists of several parts. The folder `Trump_data` includes datasets ([#1](https://www.kaggle.com/christianlillelund/donald-trumps-rallies), [#2](https://data.world/pathologicalhandwaving/trumptweets), [#3](https://data.world/lovesdata/trump-tweets-5-4-09-12-5-16)) that were used to generate the Markov chain model. In the folder, there are also several simple scripts that were used to clean the data and prepare them for the model.  
The main body of the project then consists of the following files:
* `bot.py` - the script responsible for posting comments and replies 
* `submission_bot.py` - the script responsible for (re)posting new submissions to a subreddit
* `bot_counter.py` - the script provided by [@mikeizbicki](https://github.com/mikeizbicki) to calculate 'valid' and other comments
* `gen_test.py` - separate script with the comment generating function employing `markovify` library
* `model_data.txt` - sufficiently cleaned and appended transcription of 11 years of Trump's tweets and his 2020's rally speeches that is used as the learning dataset for the `markovify` model
 
## Known Problems + TO-DO
* The dataset for the Markov Chain model is not big enough to be able to take the context of the comment that it is replying to into account. This could be solved by obtaining more data or by only replying to comments with certain words/names in it. Overall, a simple fix that could, however, limit the number of valid comments posted, so it was not implemented.
* Insdufficent in-script documentation.
* While the script was never once stopped by Reddit thanks to rotating several bots, it has a error parsing portion that sleeps the script for the amount of time required by Reddit. However, this part of the code was implemented before the multi-bot feature, and it is not updated to work with it efficiently (if one bot gets stopped, the whole script waits instead of immediately trying a new bot). A potential solution would be to completely ommit the error parsing wait portion of the code and just let the script keep trying new bots.



## CSCS-40 Grading Rubric

### Required Tasks

__20/20 all finished__

Comment: My bot program uses `markovify` that was trained on Trump tweets (circa 2009-2020) and speeches from the 2020 campaign. Therefore, the bots are assumed to support Donald J. Trump and oppose Hillary Clinton and Joe Biden. To help them achieve this, some of the Markov chain comments are designed to start with words such as "Trump," "I think," "Biden," "Hillary," and others. The bot generally works as expected (see the `bot_counter.py` output below in the Optional Tasks). More details about its workings can be found in this `README.md` file.   
Some of the 'conversations' between my bots were really funny. For example, [this one](https://old.reddit.com/r/BotTown_polibot2/comments/r1lx1a/hillary_had_a_great_evening/hlzq5g9/). It nicely combines the Trump tweets data with his speeches and somewhat feels like actual Trump comments. To quute my bot: "So here's what happened, and we'll never forget that."
<details>
  <summary>Reddit Bot Conversation Screenshot</summary>
  
  ![image](https://user-images.githubusercontent.com/63810577/143516970-172f3aa2-a9c7-4d03-866e-64c3a7679fbd.png)
  
</details>

### Optional Tasks

* __1.-3. Getting at least 100/500/1000 valid comments posted - 6/6__  
Output for `bot_counter.py -- username=polibot-cs40_4`
```
len(comments)= 1000
len(top_level_comments)= 75
len(replies)= 925
len(valid_top_level_comments)= 75
len(not_self_replies)= 925
len(valid_replies)= 925
========================================
valid_comments= 1000
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
```

* __4. Make your bot create new submission posts instead of just new comments. - 2/2__  
`submission_bot.py` posts new submissions on a selected subreddit. There are 3 types of submissions from which the bot chooses randomly: 1) Self post using `markovify` to generate its title and body. 2) Random reddit repost from a given subreddit (r/conservative in this case). 3) 'Indirect' repost from a given subreddit (r/conservative in this case) where it copies the title and the text/url of a random submission. Over 200 hundred submissions were posted by one of my bots at r/BotTown_polibot where I have moderator rights and could count them + additional submissions were posted on r/BotTown2. Overall, fulfilling the requirements of the task.

* __5. Create an "army" of 5 bots that are all posting similar comments. - 2/2__  
I have deployed 5 bots that all used the same code. In fact, the `bot.py` file would randomly select one of the bots (possible to use a subest) for each iteration. This allowed the bots to 'comunicate' with each other, saved computing resources, and helped to prevent hitting the Reddit post rate limit of individual bots. All bots posted 500+ valid comments (see below). The reason why the number of valid comments and total comments sometimes differ is because I had them post on my own subreddit where some of their comments got automatically blocked, became temporarily deleted (during this time, the bots could reply again to the same thread), and I later approved those comments not realizing what it would cause.  
<details>
  <summary>Bot Counter Outputs (in addition to the main bot above)</summary>
    
  ```
  polibot-cs40:
  
  len(comments)= 609
len(top_level_comments)= 69
len(replies)= 540
len(valid_top_level_comments)= 69
len(not_self_replies)= 540
len(valid_replies)= 540
========================================
valid_comments= 609
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
  
  
  polibot-cs40_1:
  
  len(comments)= 1000
len(top_level_comments)= 62
len(replies)= 938
len(valid_top_level_comments)= 60
len(not_self_replies)= 938
len(valid_replies)= 938
========================================
valid_comments= 998
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
  
  polibot-cs40_2:
  
  len(comments)= 1000
len(top_level_comments)= 85
len(replies)= 915
len(valid_top_level_comments)= 82
len(not_self_replies)= 915
len(valid_replies)= 915
========================================
valid_comments= 997
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
  
  polibot-cs40_3:
  
  len(comments)= 1000
len(top_level_comments)= 60
len(replies)= 940
len(valid_top_level_comments)= 58
len(not_self_replies)= 940
len(valid_replies)= 940
========================================
valid_comments= 998
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit 
  
  
  ```
  
</details>

* __6. Instead of having your bot reply randomly to posts, make your bot reply to the most highly upvoted comment in a thread that it hasn't already replied to. 2/2__  
This feature is implemented by sorrtig comments with no replies by the number of upvotes in the following way: `comments_without_replies.sort(key=lambda comment: comment.score, reverse=True)`

__5 extra credit optional tasks__
* __Use a more sophisticated algorithm for generating the text of your comments. 5/5__  
I am using the `markovify` library to generate my comments. I was thinking about using some subreddit (for example r/conservative) as the source of learning data. However, I have decided to use tweets by Donald J. Trump from 2009-2020 and his 2020 rally speaches because I came to the conclusion that his style of speech actually often sounds like a Markov chain, thus, making it more fun (and real looking). I cleaned the data and from the original datasets using `pandas` and `regex`. The sources of the datasets are listed above.


#### Total points = 37/30
