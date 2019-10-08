#!/usr/bin/env python
# coding: utf-8

# In[1]:


#! python3

#imports
import praw
import pandas as pd
import datetime as dt

#constants
N = 500 #number of posts you want to scrape
OUT_NAME = 'scrape_results.txt' #name of the output file


# In[2]:


#initialise API 
reddit = praw.Reddit(client_id='14_CHAR_KEY_HERE',
                     client_secret='27_CHAR_KEY_HERE',
                     user_agent='APP_NAME',
                     username='REDDIT_USERNAME',
                     password='REDDIT_PASSWORD')

#pick the subreddit for scraping
scraped_sub = reddit.subreddit('love')


# In[3]:


#scrape the top N posts of the subreddit of choice
top_posts = scraped_sub.top(limit = N)


# In[4]:


#add the bodies of the top N posts to a list
post_bodies = list()
for post in top_posts:
    post_text = post.selftext
    #optional: filter excessively long posts
    if (len(post_text) > 800):
        continue
    post_bodies.append(post.selftext)
    
print(post_bodies[0]) #test to see if we're working


# In[5]:


#replace all end-of-sentence punctuation marks with fullstops
for i in range(len(post_bodies)): #index of a string in list of strings
    current = post_bodies[i] #string in list of strings
    current = current.replace('!', '.')
    current = current.replace('?', '.')
    current = current.replace(';', '.') #don't necessarily need this
    post_bodies[i] = current #replace original body with modified

print(post_bodies[0]) #test to see if we're working 2: electric boogaloo


# In[6]:


#split the bodies of the posts into individual sentences in another list
sentences = list();
for textpost in post_bodies:
    post_split_post = textpost.split('.') #post-split post
    for sen in post_split_post:
        sentences.append(sen)

print(sentences[0]) #test to see if we're working 3: revenge of the tests


# In[7]:


#get rid of blank lines
no_blanks = list()
for s in sentences:
    if (s != '' and s != ' '):
        no_blanks.append(s)

sentences = no_blanks


# In[8]:


#output my sentences to a file
outfile = open(OUT_NAME, 'w+', encoding = 'utf-16') #w+ will create the file if it doesn't exist
for sentence in sentences:
    outfile.write(sentence + '\n')

outfile.close()






