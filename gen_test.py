# imports
import os
import random
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
starting_points = ['Biden', 'Sleepy Joe', 'Hillary', 'Democrats', 'Republicans', 'GOP', 'Trump', 'I think']

# Generate and print test sentences starting with one of the words/phrases from starting_points
for i in range(0,1):

    text = model.make_sentence_with_start(random.choice(starting_points), strict=False)
    print(text)

print('Next: \n')


# Generate and print test sentences
for i in range(0,4):
    print(model.make_sentence())
    