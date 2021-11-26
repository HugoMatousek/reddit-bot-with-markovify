import re
import os

#utility function for text cleaning
def text_cleaner(text):
  text = re.sub(r'--', ' ', text)
  text = re.sub('[\[].*?[\]]', '', text)
  text = re.sub(r'(\b|\s+\-?|^\-?)(\d+|\d*\.\d+)\b','', text)
  text = ' '.join(text.split())
  return text

dirname = os.path.dirname(__file__)
path = dirname + '/Text_only/'


content = ''
with open(path+'trump_tweets.txt', 'r', encoding='utf-8') as file:
     content = file.read()

content = text_cleaner(content)

content = content.replace('""','"')

f = open(path+'trump_tweets_string.txt', 'a', encoding='utf-8')
f.write(content)
f.close()