#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv("matches - matches.csv")


# In[3]:


df


# In[4]:


type(df)


# In[5]:


df.head()


# In[6]:


df.tail()


# In[7]:


df.sample(5)


# In[8]:


df.shape[0]


# In[9]:


df.info()


# In[10]:


df.describe()


# In[11]:


df.describe(include = "all")


# In[12]:


df.columns


# In[13]:


df["winner"]


# In[14]:


df.iloc[0:4]
#this will give 4 rows


# In[15]:


df.iloc[:, 0:4]
#this will give all rows and 4 columns


# In[16]:


df.loc[:, ['id', 'season']]


# In[17]:


type(df.iloc[1])
#When you use df.iloc[1] in pandas, it selects the row at index position 1 from the DataFrame df


# In[24]:


type(df.iloc[1,1])
#When you use df.iloc[1, 1] in pandas, it selects the element at the second row and second column of the DataFrame df, because indexing starts from 0.


# In[18]:


type(df.iloc[1:3])


# In[19]:


df.loc[:,[]]
#this will give all rows, no column


# In[20]:


df.iloc[:,1:4:2]
#this will give all rows, and columns from second to fourth with a step of 2 
#means it will give second and fourth column


# In[37]:


#filtering dataframe based on a certain given condition
mask = df['season'] == 2017
print(df[mask].shape)
print(mask)


# In[25]:


def get_city_match(city):
    mask = df["city"] == city
    return df[mask].shape[0]
#The provided code defines a function get_city_match(city) that counts the number of times a specified city appears in the "city" column of a DataFrame df. 
#give the no of times a particular city appeared fetching from all the rows


# In[26]:


get_city_match('Banglore')


# In[29]:


def count_city_occurrences(df, city):
    count = 0
    # Iterate over each column in the DataFrame
    for column in df.columns:
        # Sum up the occurrences of `city` in the current column
        count += (df[column] == city).sum()
    return count


# In[35]:


count_city_occurrences(df,'Banglore')


# In[39]:


df["city"].value_counts()


# In[40]:


df["winner"].value_counts()


# In[41]:


df["date"].value_counts()


# In[42]:


df["toss_winner"].value_counts()


# In[43]:


df["toss_decision"].value_counts()


# The Plot Function

# In[44]:


import matplotlib.pyplot as plt
df["winner"].value_counts().plot(kind = "bar")


# In[46]:


#for top 5
df["winner"].value_counts().head().plot(kind = "bar")


# In[47]:


df["winner"].value_counts().head().plot(kind = "barh")


# In[48]:


df["toss_decision"].value_counts().plot(kind = 'pie')


# In[52]:


df["win_by_runs"].plot(kind = "hist")


# In[53]:


#if two series has same indexes then you can add them also
df["team2"].value_counts()+ df["team1"].value_counts()


# In[54]:


#if two series has same indexes then you can multiply them also
df["team2"].value_counts() * df["team1"].value_counts()


# In[57]:


(df["team2"].value_counts()+ df["team1"].value_counts()).sort_values(ascending = False)


# In[58]:


df.sort_values("city")


# SORTING VALUES

# In[59]:


df.sort_values("city", ascending = False)


# In[60]:


df.sort_values(["city", "date"])


# In[61]:


df.sort_values(["city", "date"], ascending = False)


# In[62]:


#if you want one column in ascending order and another column in descending order or vice versa then pass parameters in ascending in a list only
df.sort_values(["city", "date"], ascending = [False, True])


# In[63]:


df.sort_values(["city", "date"], ascending = [True, False])


# DROPPING DUPLICATES

# In[64]:


df.drop_duplicates(subset = ["city"])


# In[67]:


#i want to get the winner of each season from 2008 to 2017
#so for keep function i will use last
df.drop_duplicates("season", keep = "last")[["season", "winner"]].sort_values("season")


# In[72]:


company = pd.read_csv("Fortune_500_Companies_US[1].csv", encoding='ISO-8859-1')


# In[73]:


company


# In[78]:


name = company.groupby("Company Name")


# In[79]:


name 


# In[80]:


len(company) #no of rows


# In[81]:


len(name) #length of groupby object


# In[82]:


name.size()  #tells size of each name in terms of no of companies


# In[83]:


name.size().sort_values(ascending = False)


# In[84]:


name.groups


# In[86]:


delivery = pd.read_csv("deliveries[1].csv")
delivery


# In[87]:


delivery.head()


# In[90]:


#top 5 batsman in terms of run scored
runs = delivery.groupby("batsman")
runs


# In[94]:


runs.get_group("V Kohli").shape


# In[96]:


#we want no of runs scored by every batsman in sorted order so that we can find top 5
runs["batsman_runs"].sum().sort_values(ascending = False)


# In[98]:


#for top 5
runs["batsman_runs"].sum().sort_values(ascending = False).head()


# In[99]:


#batsman who has scored max no of fours
mask = delivery["batsman_runs"] == 4  #means i need only those rows where natsman_runs = 4
#this will generate a binary(true or false) series
#we will bring this series and port it to dataframe
new_delivery = delivery[mask]
#means in this series we will get only those rows where dataframe has true values


# In[101]:


#aaj tk ipl mein fours kitne hue hein
new_delivery.shape[0]


# In[102]:


#aaj tk ipl mein chakke kitne lge hein
sixes = delivery["batsman_runs"] == 6
delivery_sixes = delivery[sixes]


# In[104]:


delivery_sixes.shape[0]


# In[106]:


new_delivery.groupby('batsman')['batsman_runs'].count().sort_values(ascending = False)


# In[110]:


#virat kohli has scored maximum runs against which teams
high = delivery[delivery["batsman"] == 'V Kohli']


# In[111]:


high.shape


# In[112]:


high.groupby("bowling_team")["batsman_runs"].sum().sort_values(ascending = False)


# In[115]:


#kisi bhi batsman ka naam do aur vo return kr dega ki usne sbse zyada runs kis team ke against bnaaye
def run_scored(batsman_name):
    high = delivery[delivery["batsman"] == batsman_name]
    return high.groupby("bowling_team")["batsman_runs"].sum().sort_values(ascending = False).index[0]


# In[116]:


run_scored("V Kohli")


# In[117]:


run_scored("DA Warner")


# isin()

# In[119]:


#find the most destructive death over batsman in the history of IPL
#on the basis of strike rate
#strike rate = (no of runs/ no of balls)/100
#100 ball khelkr batsman ne kitne run maare
#minimum no of balls played by batsman = 200 in over 16-20


# In[124]:


death_over = delivery[delivery["over"]>15]


# In[128]:


all_batsman = death_over.groupby("batsman")["batsman_runs"].count()
x = all_batsman>200


# In[130]:


all_batsman[x]


# In[131]:


all_batsman[x].shape


# In[133]:


batsman_list = all_batsman[x].index.tolist()


# In[136]:


#runs scored by all these 43 batsman
#balls played by all these 43 batsman
delivery[delivery["batsman"].isin(batsman_list)]


# In[137]:


final = delivery[delivery["batsman"].isin(batsman_list)]


# In[140]:


runs = final.groupby("batsman")["batsman_runs"].sum()


# In[141]:


balls = final.groupby("batsman")["batsman_runs"].count()


# In[142]:


strike_rate = (runs/balls)*100


# In[143]:


strike_rate


# MERGE

# In[144]:


#list of orange cap holder(guy who made maximum runs in a particular season)


# In[ ]:


#both the datasets match(df), delivery has a common column match_id


# In[146]:


delivery.merge(df,left_on = "match_id", right_on = "id")


# In[151]:


new = delivery.merge(df,left_on = "match_id", right_on = "id")


# In[148]:


delivery.shape


# In[149]:


df.shape


# In[153]:


new.groupby(["season", "batsman"])["batsman_runs"].sum()
#multi index series will be created


# In[159]:


#we have to find out top batsman in every season
new.groupby(["season", "batsman"])["batsman_runs"].sum().reset_index()


# In[163]:


new.groupby(["season", "batsman"])["batsman_runs"].sum().sort_values(ascending=False).reset_index()


# In[167]:


new.groupby(["season", "batsman"])["batsman_runs"].sum().sort_values(ascending=False).reset_index().drop_duplicates(subset = "season", keep = "first").sort_values("season")[["season", "batsman"]]


# pivot table

# In[168]:


mask = delivery["batsman_runs"] == 6
six = delivery[mask]
six.head()


# In[169]:


six.shape  #aaj tk ipl mein kitne sixes lge


# In[172]:


pivot = six.pivot_table(index = "over", columns = "batting_team", values = "batsman_runs" , aggfunc = "count")


# In[173]:


import seaborn as sns
sns.heatmap(pivot)


# In[175]:


delivery.corr()


# In[176]:


df.set_index("id")


# MISSING VALUES

# In[179]:


df["umpire3"].isnull().sum()


# In[183]:


d = df["umpire3"].dropna()


# In[184]:


d.shape


# In[182]:


df["umpire3"].isnull().sum()


# In[185]:


df.shape


# In[186]:


df.dropna(axis = 1).shape


# In[ ]:




