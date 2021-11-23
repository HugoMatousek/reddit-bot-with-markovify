import os
import random
import markovify

path = os.path.dirname(__file__)



content = ''
with open(path+'/model_data.txt', 'r', encoding='utf-8') as file:
     content = file.read()

     


model = markovify.Text(content)

starting_points = ['Biden', 'Sleepy Joe', 'Hillary', 'Democrats', 'Republicans', 'GOP', 'Trump', 'I think']


for i in range(0,1):
    text = model.make_sentence_with_start(random.choice(starting_points), strict=False)
    text = text + model.make_sentence_with_start(text, strict=False)
    print(text)

print('Next: \n')



for i in range(0,4):
    print(model.make_sentence())
    