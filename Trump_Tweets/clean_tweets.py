import pandas as pd
import os
import re


dirname = os.path.dirname(__file__)
path = dirname + '/Original_files/'

df = pd.DataFrame()
df_final = pd.DataFrame()

for i in range(1,8):    

    dftemp = pd.read_csv(path+'Trump_'+str(i)+'.csv')
    
    df = pd.concat([df,dftemp['tweet']],ignore_index=True)
    
df_final['tweet'] = df[0].apply(lambda x: re.split('(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)', str(x))[0])

df_final = df_final.dropna()

df_final.to_csv(dirname + '/Text_only/trump_tweets.csv', encoding='utf-8-sig', index = False)