#!/usr/bin/env python
# coding: utf-8

from twitter_scraper import get_tweets
import numpy as np
import datetime as dt
from collections import Counter
import pandas
tweettimearr=[]
tweettimearr2=[]
for tweet in get_tweets('user', pages=50):
    if tweet['isRetweet']==False:
        times=tweet['time'].strftime("%H:%M:%S")
        tweettimearr.append(times)

for hour in tweettimearr:
    tweettimearr2.append(hour[:2])
    
count = Counter(tweettimearr2)
df = pandas.DataFrame.from_dict(count, orient='index')
df.sort_index(inplace=True)
df.plot(kind='bar')
