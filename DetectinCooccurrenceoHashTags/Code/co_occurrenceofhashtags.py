# -*- coding: utf-8 -*-
"""Co-occurrenceofHashtags.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vPZk0BacmtqHY4km6nuT7adq70e8f4bs
"""

import pandas as pd
from itertools import combinations
import collections
import os
import locale
import sys

reload(sys)
sys.setdefaultencoding('utf8')

df = pd.read_pickle('AllCountryData.pkl')
print(df.shape)

contents = []
contents = list(df['Contents'])
print('Length of contents',len(contents))

hash_tags = []
hash = '#'
for content in contents:
    temp=str(content).split()
    for i in temp:
        if hash in i:
            hash_tags.append(i)

print('Length of hash tags', len(hash_tags))

df_rows =[]
ctr = collections.Counter(hash_tags)
df_rows = ctr.most_common(100)
hash_tags_df = pd.DataFrame(df_rows, columns=['Hash_Tag','Count'])
hash_tags_df

top_100_hashtags = []
top_100_hashtags = list(hash_tags_df['Hash_Tag'])
top_100_hashtags

def getCombinations(seq):
    combos = list()
    for i in range(0,len(seq)):
        for j in range(i+1,len(seq)):
            combos.append([seq[i],seq[j]])
            print(len(combos))
    
    return combos

combinations =list()
combinations = getCombinations(top_100_hashtags)

combinations

result_df_rows =[]

# for i in range(0,len(hash_tags)):
#     for j in range(i+1,len(hash_tags)):
#         count =0
#         for content in contents:
#             if str(hash_tags[i]) in str(content):
#                 if str(hash_tags[j]) in str(content):
#                     count = count +1
#         result_df_rows.append(tuple([str(hash_tags[i]),str(hash_tags[j]), count]))
#         print(len(result_df_rows))

for combo in combinations:
    count = 0
    for content in contents:
        if str(combo[0]) in str(content):
            if str(combo[1]) in str(content):
                count = count+1
    result_df_rows.append(tuple([str(combo[0]),str(combo[1]), count]))
    print('Combo',combo,'Processed...')

result_df_columns = ['Hashtag1', 'Hashtag2','Co-occurrence']

result_df = pd.DataFrame(result_df_rows, columns=result_df_columns)
result_df.to_pickle('ResultData.pkl')
result_df.to_csv('ResultData.csv')
print('Result data exported')