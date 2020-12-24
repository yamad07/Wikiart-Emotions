#!/usr/bin/env python
# coding: utf-8

# In[70]:


import pandas as pd
import os


# In[71]:


df = pd.read_csv('WikiArt-annotations.csv')


# In[72]:


df = pd.read_csv("WikiArt-Emotions-All.tsv", delimiter='\t')
df_info = pd.concat([df["Image URL"], df['ID']], axis=1)



# In[88]:

emotions = ["happiness", "sadness", "anger", "fear", "love", "trust", "surprise"]
base_dir = '../wikiart-emotions/valence-arousal/train'

for emotion in emotions:
    emotion_dir_name = os.path.join(base_dir, emotion)
    if not os.path.exists(emotion_dir_name):
        os.mkdir(emotion_dir_name)

# In[89]:


import os
import pprint
import time
import urllib.error
import urllib.request

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except:
        print('err')


# In[ ]:


import ssl
ssl._create_default_https_context = ssl._create_unverified_context
for emotion in emotions:
    df_url = df.sort_values(by=["ImageOnly: {}".format(emotion)], ascending=False)[:500]["Image URL"]
    for i, url in enumerate(df_url):
        if i > 500:
            break
        if i % 10 == 0:
            print(url)
        img_name = url.split('/')[-1]
        download_file(url, os.path.join(base_dir, emotion, img_name))
