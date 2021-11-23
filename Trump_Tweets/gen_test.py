import os
import markovify

dirname = os.path.dirname(__file__)
path = dirname + '/Text_only/'


content1 = ''
with open(dirname+'/speeches.txt', 'r', encoding='utf-8') as file:
     content1 = file.read()
     
content2 = ''
with open(path+'trump_tweets_string.txt', 'r', encoding='utf-8') as file:
     content2 = file.read()
     
     
model1 = markovify.Text(content1)
model2 = markovify.Text(content2)

model = markovify.combine([model1,model2])


for i in range(0,4):
    print(model.make_sentence_with_start('Biden', strict=False))
    

print('Next: \n')



for i in range(0,4):
    print(model.make_sentence())
    