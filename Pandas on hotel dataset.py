#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("hotel_bookings[1].csv")


# In[3]:


df


# In[4]:


df.columns


# In[5]:


df.info()


# In[6]:


df.describe(include = "all")


# In[8]:


#no of rows and columns
df.shape


# In[9]:


#TASK: Is there any missing data? If so, which column has the most missing data?
df.isnull().sum()


# In[10]:


#TASK: Drop the "company" column from the dataset.
df.drop("company", axis = 1)


# In[13]:


#TASK: What are the top 5 most common country codes in the dataset?
df["country"].value_counts().head()


# In[14]:


df["name"]


# In[15]:


#TASK: Which hotel paid the highest ADR (average daily rate)? How much was their ADR?
df.groupby("hotel")["adr"].sum().sort_values(ascending = False)


# In[16]:


#TASK: The adr is the average daily rate for a person's stay at the hotel. What is the mean adr across all the hotel stays in the dataset?
round(df['adr'].mean(),2)


# In[20]:


#TASK: What is the average (mean) number of nights for a stay across the entire data set? Feel free to round this to 2 decimal point
df["stays_in_nights"] = df["stays_in_weekend_nights"] + df["stays_in_week_nights"]
round(df["stays_in_nights"].mean(), 2)


# In[23]:


df.columns


# In[25]:


#TASK: What is the average total cost for a stay in the dataset? Not average daily cost, but total stay cost. (You will need to calculate total cost your self by using ADR and week day and weeknight stays). Feel free to round this to 2 decimal points.
df["amount_spend"] = df["adr"] * df["stays_in_nights"]
round(df["amount_spend"].mean(), 2)


# In[27]:


#TASK: What percentage of hotel stays were classified as "repeat guests"? (Do not base this off the name of the person, but instead of the is_repeated_guest column)
round(100*sum(df["is_repeated_guest"] == 1) / len(df), 2)


# In[28]:


#TASK: What are the top 5 most common country name in the dataset?
df["country"].value_counts().tail()


# In[34]:


#TASK: What are the names of the hotel who had booked the most number children and babies for their stay
df["total_babies"] = df["children"] + df["babies"]
df["total_babies"]
df.sort_values('total_babies', ascending = False)[["hotel", "total_babies"]]


# In[35]:


df.groupby("hotel")["total_babies"].value_counts().sort_values(ascending = False)


# In[36]:


#TASK: How many arrivals took place between the 1st and the 15th of the month (inclusive of 1 and 15)
df['arrival_date_day_of_month'].apply(lambda day: day in range(1,16)).sum()


# In[ ]:




