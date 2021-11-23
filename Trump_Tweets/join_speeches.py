import glob
import os


path = os.path.dirname(__file__)

text = ''

file_list = glob.glob(os.path.join(os.getcwd(), 'Speeches', '*.txt'))


for file in file_list:
    with open(file,encoding='utf-8') as f:
        text = text + '\n' + f.read()


final = open(path+'/speeches.txt', 'a', encoding='utf-8')
final.write(text)
final.close()