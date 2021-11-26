# reddit-bot-with-markovify




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
  
  
  
  ```
  
</details>
