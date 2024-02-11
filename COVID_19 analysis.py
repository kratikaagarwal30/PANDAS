#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


data = pd.read_csv("transformed_data[1].csv")
data2 = pd.read_csv("raw_data[1].csv")


# In[3]:


data


# In[4]:


#The data we are using contains the data on covid-19 cases and their impact on GDP from December 31, 2019, to October 10, 2020.


# DATA PREPARATION

# In[5]:


data.head(5)


# In[6]:


data["CODE"].unique().shape[0]


# In[7]:


data2.head()


# In[9]:


#After having initial impressions of both datasets, I found that we have to combine both datasets by creating a new dataset.
#But before we create a new dataset, let’s have a look at how many samples of each country are present in the dataset:
data["COUNTRY"].value_counts(ascending = False)


# In[10]:


data.shape


# In[11]:


data.shape


# In[12]:


#Aggregating the data
data2.rename(columns = {"location" : "COUNTRY"}, inplace = True)


# In[13]:


data2


# In[14]:


merged_data = pd.merge(data, data2, on= "COUNTRY", how = "outer")


# In[15]:


#Aggregating values
aggregated_data = merged_data.groupby("COUNTRY").agg(
HDI = ("HDI", "mean"),
Total_Cases = ("total_cases", "sum"),
Total_Deaths = ("total_deaths", "sum"),
Stringency_Index = ("stringency_index", "mean"),
Population = ("population", "mean")).reset_index()


# In[16]:


aggregated_data


# In[17]:


country_codes = data[["COUNTRY", "CODE"]].drop_duplicates()


# In[18]:


country_codes.shape


# In[19]:


final_data = pd.merge(aggregated_data, country_codes, on = "COUNTRY", how = 'left')


# In[20]:


final_data = final_data[["CODE", "COUNTRY", "HDI", "Total_Cases", "Total_Deaths", "Stringency_Index", "Population"]]
final_data.head()


# In[21]:


final_data.info()


# In[22]:


final_data.describe()


# In[23]:


final_data.isnull().sum()


# 1. Find top countries with highest number of cases
# 

# In[24]:


data = aggregated_data.sort_values(by = "Total_Cases", ascending = False)


# In[25]:


print(data)


# In[26]:


data.columns


# In[27]:


# 1.  Filtering: Rows Where Number of Total Cases is Greater than 10,000
data[data["Total_Cases"] > 10000]


# In[28]:


#2.  Average Human Development Index (HDI) for Each Country
data.groupby("COUNTRY")["HDI"].mean()


# In[29]:


#3. Sorting Dataset by Number of Total Cases in Descending Order
data.sort_values(by = "Total_Cases", ascending = False)


# In[30]:


# 4. Sorting dataset by Number of Total Deaths in Descending Order
data.sort_values(by = "Total_Deaths", ascending = False)


# In[31]:


#5.  Calculate and Add a New Column for the Death Rate
data['death_rate'] = data['Total_Deaths']/ data['Total_Cases']


# In[32]:


data


# In[33]:


#6.Plot the total number of cases over time for a specific country
data.groupby("COUNTRY")["Total_Cases"].sum()


# In[34]:


#7.  find the correlation between HDI and total cases per capita
data["cases_per_capita"] = data["Total_Cases"]/ data["Population"]
data[["HDI", "cases_per_capita"]].corr()


# In[35]:


#8.  Ranking Countries by Total Cases and Total Deaths Separately
data["cases_rank"] = data["Total_Cases"].rank(method = "max", ascending = False)
data['deaths_rank'] = data['Total_Cases'].rank(method = "max", ascending = False)
data


# In[36]:


#9. Normalization of Total Cases and Total Deaths by Population
data['Cases_Per_100k'] = (data['Total_Cases'] / data['Population']) * 100000
data['Deaths_Per_100k'] = (data['Total_Deaths'] / data['Population']) * 100000


# In[37]:


data


# In[39]:


#10. Data Transformation: Categorizing Stringency_Index
data["Stringency_Index"] = pd.qcut(data["Stringency_Index"], q = 3, labels = ["Low", "Medium", "High"])


# In[40]:


data


# In[ ]:




