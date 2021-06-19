#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 13:12:41 2021

@author: maitha
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

iran_data_feb2021 = pd.read_csv("/Users/maitha/Desktop/Assessment/February2021/Iran/iran_tweet_data_feb_2021.csv")
#total dataset size 
iran_data_feb2021.info()


iran_data_oct2020 = pd.read_csv("/Users/maitha/Desktop/Assessment/October2020/Iran/iran_tweet_data_oct_2020.csv")
iran_data_oct2020.info()

iran_data_june2019_set1 = pd.read_csv("/Users/maitha/Desktop/Assessment/June2019/Iranset1/iran_tweet_data_june_2019.csv")
iran_data_june2019_set1.info()

iran_data_june2019_set2 = pd.read_csv("/Users/maitha/Desktop/Assessment/June2019/Iranset2/iran_tweet_data_june_2019.csv")
iran_data_june2019_set2.info()

iran_data_june2019_set3 = pd.read_csv("/Users/maitha/Desktop/Assessment/June2019/Iranset3/iran_tweet_data_june_2019.csv")
iran_data_june2019_set3.info()

iran_data_january2019_1 = pd.read_csv("/Users/maitha/Desktop/Assessment/January2019/Iran/Irantweet/iran1.csv")
iran_data_january2019_1.info()

iran_data_january2019_2 = pd.read_csv("/Users/maitha/Desktop/Assessment/January2019/Iran/Irantweet/iran2.csv")
iran_data_january2019_2.info()

iran_data_january2019_3 = pd.read_csv("/Users/maitha/Desktop/Assessment/January2019/Iran/Irantweet/iran3.csv")
iran_data_january2019_3.info()

iran_data_january2019_4 = pd.read_csv("/Users/maitha/Desktop/Assessment/January2019/Iran/Irantweet/iran4.csv")
iran_data_january2019_4.info()

iran_data_oct2018 = pd.read_csv("/Users/maitha/Desktop/Assessment/October2018/Iran/iran_tweet_data_october_2018.csv")
iran_data_oct2018.info()

#merging all datasets into one
iran_whole_data=pd.concat([iran_data_feb2021,iran_data_oct2020,iran_data_june2019_set1, iran_data_june2019_set3, iran_data_june2019_set2,iran_data_january2019_1, iran_data_january2019_2, iran_data_january2019_3, iran_data_january2019_4,iran_data_oct2018])

#total dataset size 
iran_whole_data.info()

#split between tweets and retweets 
Iran_split= pd.DataFrame(iran_whole_data,columns=("tweetid","is_retweet"))

#number of unique users involved 
iran_unique_users = iran_whole_data.userid.unique()

#metric of conectivity of involved users; the line graph shows as the number of likes
#per tweet increased, their retweets also increased
iran_whole_data.plot.line(x="like_count",y="retweet_count")

#average interaction received by tweets in terms of likes
interaction_iran_data=pd.DataFrame(iran_whole_data,columns=["tweet_text","like_count"])
interaction_iran_data.sort_values(by=["like_count"],ascending=False,inplace=True)

#Time series construction
#Changing the tweet_time from object to date time data type in order to plot it
iran_whole_data["tweet_time"]=pd.to_datetime(iran_whole_data["tweet_time"],format="%Y-%m-%d %H:%M")

#setting the index
iran_whole_data=iran_whole_data.set_index("tweet_time")
iran_whole_data.index

#Creating new columns with the index
iran_whole_data['year']=iran_whole_data.index.year
iran_whole_data.sample(5,random_state=0)
iran_whole_data['month']=iran_whole_data.index.month
iran_whole_data['date']=iran_whole_data.index.date
iran_whole_data['hour']=iran_whole_data.index.hour



#The graph shows the number of likes that occured per hour in the Iran Campaign
iran_whole_data.plot.scatter(x="hour",y="like_count")
iran_whole_data.plot.scatter(x="year",y="like_count")


#User Graph Construction
#creating a new dataframe with two columns, hashtags and userid
iran_graph_data = iran_whole_data[["hashtags", "userid"]]


#G = nx.from_pandas_dataframe(edges, "tweet_text")
G=nx.Graph()

#hashtags as edges and userids as nodes
G = nx.from_pandas_edgelist(iran_graph_data, "hashtags", "userid")

#python library for plots 
from matplotlib.pyplot import figure
figure(figsize=(10, 8))
nx.draw_shell(G, with_labels=True)


# topic Modeling
tweets= iran_whole_data[["tweet_text"]]
tweets.info()
# finding out the character length of the tweets (the majority of the tweets are this length)
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,6))
doc_lens = [len(d) for d in tweets]
plt.hist(doc_lens, bins = 100)
plt.title('Distribution of Tweets character length')
plt.ylabel('Number of Tweets')
plt.xlabel('Tweets character length')
sns.despine();






#for word visualization, creating a word cloud visualization
#importing matplot
import matplotlib as mpl 
from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS
#setting the figure's size
mpl.rcParams['figure.figsize']=(12.0,12.0)  
mpl.rcParams['font.size']=12            
mpl.rcParams['savefig.dpi']=100             
mpl.rcParams['figure.subplot.bottom']=.1 
stopwords = set(STOPWORDS)
wordcloud = WordCloud(
                          background_color='white',
                          stopwords=stopwords,
                          max_words=500,
                          max_font_size=40,
                          random_state=100
                         ).generate(str(tweets))
print(wordcloud)
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
plt.show();
















