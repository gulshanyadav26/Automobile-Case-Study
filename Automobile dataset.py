#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


auto = pd.read_csv('Automobile.csv')


# **Check the head of the DataFrame.**

# In[3]:


auto.head()


# ** How many rows and columns are there? **

# In[4]:


auto.info()


# ** What is the average Price of all cars in the dataset? **

# In[5]:


auto['price'].mean()


# ** Which is the cheapest make and costliest make of car in the lot? **

# In[6]:


auto[auto['price']==auto['price'].max()]


# In[7]:


auto[auto['price']==auto['price'].min()]


# ** How many cars have horsepower greater than 100? **

# In[8]:


auto[auto['horsepower']>100].count()


# ** How many hatchback cars are in the dataset ? **

# In[9]:


auto[auto['body_style'] == 'hatchback'].info()


# ** What are the 3 most commonly found cars in the dataset? **

# In[10]:


auto['make'].value_counts().head(3)


# ** Someone purchased a car for 7099, what is the make of the car? **

# In[11]:


auto[auto['price']==7099]['make']


# *** Which cars are priced greater than 40000? **

# In[12]:


auto[auto["price"] >40000] 


# ** Which are the cars that are both a sedan and priced less than 7000? **

# In[13]:


auto[(auto['body_style']=='sedan') & (auto['price']<7000)]

