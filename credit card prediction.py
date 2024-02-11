#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("bank-additional-full[1].csv", sep = ";")
df.head()


# In[3]:


df.columns


# **UNDERSTANDING THE DATA**
# ALL COLUMNS REPRESENT THE FOLLOWING : 
# 
# 1.age: The age of the client.
# 
# 2.job: The type of job held by the client (e.g., "admin.", "blue-collar", "entrepreneur", etc.).
# 
# 3.marital: The marital status of the client (e.g., "married", "single", "divorced").
# 
# 4.education: The level of education of the client (e.g., "basic.4y", "high.school", "university.degree").
# 
# 5.default: Indicates whether the client has credit in default (e.g., "no", "yes", "unknown").
# 
# 6.housing: Indicates whether the client has a housing loan (e.g., "no", "yes", "unknown").
# 
# 7.loan: Indicates whether the client has a personal loan (e.g., "no", "yes", "unknown").
# 
# 8.contact: Type of communication used to contact the client (e.g., "cellular", "telephone").
# 
# 9.month: The last contact month of the year (e.g., "jan", "feb", "mar", ..., "dec").
# 
# 10.day_of_week: The last contact day of the week (e.g., "mon", "tue", "wed", "thu", "fri").
# 
# 11.duration: The last contact duration, in seconds (note: this attribute highly affects the output target and should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model).
# 
# 12.campaign: The number of contacts performed during this campaign and for this client (includes last contact).
# 
# 13.pdays: The number of days that passed by after the client was last contacted from a previous campaign (999 means client was not previously contacted).
# 
# 14.previous: The number of contacts performed before this campaign and for this client.
# 
# 15.poutcome: The outcome of the previous marketing campaign (e.g., "failure", "nonexistent", "success").
# 
# 16.emp.var.rate: Employment variation rate - quarterly indicator (numeric).
# 
# 17.cons.price.idx: Consumer price index - monthly indicator (numeric).
# 
# 18.cons.conf.idx: Consumer confidence index - monthly indicator (numeric).
# 
# 19.euribor3m: Euribor 3 month rate - daily indicator (numeric).
# 
# 20.nr.employed: Number of employees - quarterly indicator (numeric).
# 
# 21.y: The target variable indicating whether the client has subscribed to a term deposit or not (e.g., "yes", "no").
# 
# **STORY OF DATA**
# 
# Imagine a bank that wants to understand its customers better, especially how likely they are to save money by opening a term deposit account, which is a type of savings account where you lock in your money for a certain period and get interest on it. To do this, the bank keeps a detailed record of its customers and their interactions with the bank's marketing campaigns.
# 
# Here's a simplified look at what the bank knows about its customers and their interactions:
# 
# Who the Customers Are: The bank collects basic information about the customers, like their age, what kind of job they have, whether they're married or single, and their level of education.
# 
# Customers' Financial Situation: The bank notes if customers have loans (housing or personal) and whether they've ever failed to pay back a loan (defaulted).
# 
# How the Bank Talks to Customers: The bank records how it contacts customers (by phone or in person), when they last talked (month and day of the week), and how long the conversation lasted.
# 
# Past Marketing Efforts: The bank also keeps track of how many times it has tried to convince each customer to open a term deposit account, both in the current campaign and in past efforts. If a customer was contacted in a previous campaign, the bank notes how long ago that was and whether the customer decided to open an account then.
# 
# Economic Environment: Because people's financial decisions can be influenced by the economy, the bank also looks at various economic indicators like employment rates, consumer prices, and interest rates.
# 
# The Big Question - Did the Customer Say Yes?: After all this effort, the bank records whether each customer decided to open a term deposit account.
# 
# In simpler terms, this dataset is like a storybook of how the bank tries to get customers to save money with them. It includes details about who the customers are, their financial habits, how the bank has tried to reach out to them, and whether those efforts were successful. This information helps the bank understand what works and what doesn't, so they can be better at convincing customers to save money with them in the future.
# 
# **The primary reasons why banks want customers to open term deposit accounts:**
# 
# Stable Source of Funds: Term deposits are a stable source of funding for banks. When customers commit their money for a fixed term, the bank knows it has that money available for a set period. This predictability allows the bank to plan its lending activities more effectively. Banks can lend this money to other customers in the form of loans or mortgages, which typically have higher interest rates than what the bank pays on term deposits, earning the bank a profit.
# 
# Liquidity Management: By managing term deposits effectively, banks can ensure they have enough liquidity to meet their day-to-day operational needs and regulatory requirements without having to resort to borrowing money from more expensive sources.
# 
# Profitability: The difference between the interest banks pay on term deposits and the interest they earn on loans (the interest rate spread) contributes to their profitability. Term deposits often offer lower interest rates to customers compared to the rates banks charge for loans, allowing banks to make a profit from the difference.
# 
# Customer Relationships: Offering term deposits helps banks build and maintain long-term relationships with their customers. When customers open a term deposit, they are more likely to use other banking products and services, increasing their overall engagement with the bank. This can lead to a more loyal customer base.
# 
# Risk Management: Term deposits are generally considered low-risk funding compared to other sources like short-term market borrowings. Since the funds are locked in for a specific period, banks have a reduced risk of sudden withdrawals, providing a more stable capital base.
# 
# Regulatory Compliance: Banks are required by regulatory authorities to maintain certain levels of stable funding to ensure they can withstand periods of financial stress. Term deposits contribute to this stable funding, helping banks comply with regulatory requirements and ensuring the overall stability of the financial system.
# 
# In summary, by encouraging customers to open term deposit accounts, banks secure a predictable and stable source of funds that supports their lending activities, enhances profitability, strengthens customer relationships, and helps manage liquidity and financial risks.

# **UNDERSTANDING DATA USING PANDAS**

# In[5]:


df["job"].unique()


# In[6]:


df["education"].unique()


# In[8]:


df["default"].unique()


# In[9]:


df["month"].unique()


# In[10]:


df["duration"].unique()


# In[11]:


df["campaign"].unique()


# In[12]:


df["poutcome"].unique()


# In[13]:


df["emp.var.rate"].unique()


# In[15]:


df["cons.price.idx"].unique()


# In[16]:


df["cons.conf.idx"].unique()


# In[17]:


df["euribor3m"].unique()


# In[18]:


df["nr.employed"].unique()


# In[19]:


df["y"].unique()


# In[20]:


df.shape


# In[21]:


df.head(5)


# In[22]:


df.info()


# In[23]:


#As dataset has no null values, so we don't need to fill the gaps


# In[24]:


#Let's understand descriptive analysis of the whole data
df.describe(include = "all")


# The outcome indicates that the typical client is categorized as administrative staff (job = admin.), has a marital status of married, and possesses a university degree (education = university.degree).

# In[27]:


#let's calculate how much percentage of people has taken term deposit
df["y"].value_counts(normalize = True)*100


# In[32]:


df_yes = df[df['y'] == 'yes']


# In[33]:


df


# In[34]:


#now i want to see that what percentage of data is married who have said yes to take term deposit
percentage_married_yes = (df_yes["marital"] == "married").mean()*100


# In[35]:


print(f"Percentage of married clients who said 'yes': {percentage_married_yes:.2f}%")


# In[39]:


df["day_of_week"].value_counts()


# In[40]:


df["month"].value_counts()


# In[41]:


#Let's sort the dataset
df.sort_values(by = "duration", ascending = False)


# In[44]:


df["duration"].sort_values(ascending = False)


# The sorting results show that the longest calls exceed one hour, as the value duration is more than 3600 seconds or 1 hour

# In[46]:


#sort by the column group
df.sort_values(by = ["age", "duration"], ascending = [True, False]).head()


# We see that the youngest customers are at the age of 17, and the call duration exceeded 3 minutes only for three clients, which indicates the ineffectiveness of long-term interaction with such clients.

# In[47]:


df.apply(np.max)


# The oldest client is 98 years old (age = 98), and the number of contacts with one of the customers reached 56 (campaign = 56).

# In[51]:


age_under_30 = df[df['age'] > 30]


# In[52]:


df


# In[54]:


#1. How do you group data by one column and calculate the sum of another column?
df.groupby("marital")["cons.price.idx"].sum()


# In[55]:


df.groupby("marital")["nr.employed"].sum()


# In[65]:


# 2. How do you set a column as the index of a DataFrame?
df.set_index('age')


# In[66]:


#3. Handling Missing Data by Filling in Missing Values
df["age"].fillna(df["age"].mean())


# In[69]:


#4. Sorting a DataFrame by Multiple Columns
df.sort_values(["age", "duration"], ascending = [True, False])


# In[72]:


#5. How do you aggregate data by grouping by multiple columns and applying different aggregation functions to different columns?
df.groupby(["age", "job"])[["cons.price.idx", "nr.employed"]].mean()


# In[122]:


#6. How can you calculate cumulative statistics (e.g., cumulative sum) across a DataFrame?
cumulative_sum = df['age'].cumsum()
import matplotlib.pyplot as plt
plt.plot(cumulative_sum)


# In[80]:


cumulative_mean = df["age"].expanding().mean()
cumulative_mean
plt.plot(cumulative_mean)


# In[82]:


cum_prod = df["age"].cumprod()
plt.plot(cum_prod)


# In[84]:


df['job'].str.extract('(pattern)', expand=True)


# In[85]:


df['marital'].str.extract('(pattern)', expand=True)


# In[90]:


df.columns


# ALL THE FUNCTIONS OF PANDAS

# In[121]:


import pandas as pd

# Assuming 'banking_data.csv' is your dataset
df = pd.read_csv('bank-additional-full[1].csv' , sep = ";")

# Display the first 5 rows
print(df.head())

# Display the last 5 rows
print(df.tail())

# Display a random sample of 5 rows
print(df.sample(5))

# Summary information about DataFrame
df.info()

# Data types of each column
print(df.dtypes)

# Shape of DataFrame
print(df.shape)

# Total number of elements
print(df.size)

# Number of dimensions
print(df.ndim)

# Descriptive statistics
print(df.describe())

# Unique values in a column (e.g., 'job')
print(df['job'].unique())

# Number of unique values in 'job'
print(df['job'].nunique())

# Check for missing values
print(df.isnull())

# Fill missing values (e.g., in 'age' with the mean age)
df['age'].fillna(df['age'].mean(), inplace=True)

# Sorting by multiple columns
df_sorted = df.sort_values(by=['age', 'job'], ascending=[True, False])

# Value counts in 'marital' column
print(df['marital'].value_counts())

# Get n largest values from 'balance'
print(df['cons.price.idx'].nlargest(5))

# Get n smallest values from 'duration'
print(df['duration'].nsmallest(5))

# Copy DataFrame
df_copy = df.copy()

# Rename 'education' column to 'edu_level'
df_renamed = df.rename(columns={'education': 'edu_level'})

# Drop 'education' column
df_dropped = df.drop(columns=['education'])

# Group by 'marital' and calculate mean 'cons.price.idx'
df_grouped = df.groupby('marital')['cons.price.idx'].mean()

# Correlation matrix
correlation_matrix = df.select_dtypes(include=['number']).corr()
print(correlation_matrix)

# Insert a new column
df.insert(2, 'new_column', df['age'] * 2)

# Sum of 'balance'
print(df['cons.price.idx'].sum())

# Mean of 'age'
print(df['age'].mean())

# Median of 'duration'
print(df['duration'].median())

# Standard deviation of 'age'
print(df['age'].std())

# Apply a custom function (e.g., adding 10 to 'age')
df['age_plus_10'] = df['age'].apply(lambda x: x + 10)

# Merge two DataFrames (assuming df2 exists and has a common 'id' column)
#df_merged = pd.merge(df, df2, on='id', how='left')

# Change data type of 'age' to 'float'
df['age'] = df['age'].astype(float)

# Set 'id' as the index
df.set_index('age')

# Reset index
df_reset = df.reset_index()

# Saving DataFrame to CSV without the index
#df.to_csv('output.csv', index=False)

# Cumulative sum of 'age'
cumulative_sum = df['age'].cumsum()

# Iterating over rows
#for index, row in df.iterrows():
    #print(index, row['age'])

# Iterating over (column name, series) pairs
#for column, series in df.iteritems():
    #print(column, series.head())

# Convert 'date' column to datetime
#df['date'] = pd.to_datetime(df['date'])

# Convert 'age' column to numeric
df['age'] = pd.to_numeric(df['age'])

# Concatenate df with df_copy vertically
df_concatenated = pd.concat([df, df_copy])

# Calculate covariance between 'age' and 'balance'
print(df[['age', 'emp.var.rate']].cov())

# Drop duplicates
df_unique = df.drop_duplicates()

# Drop rows with any missing values
df_clean = df.dropna()

# Calculate the difference between consecutive 'balance' values
df['balance_diff'] = df['cons.price.idx'].diff()

# Rank 'age' in descending order
df['age_rank'] = df['age'].rank(ascending=False)

# Resample time series data (assuming 'date' is a datetime index)
#df_resampled = df.resample('M').mean()

# Replace values (e.g., replace 'unknown' in 'job' with NaN)
df['job'].replace('unknown', pd.NA, inplace=True)

# Save DataFrame to Excel file
df.to_excel('output.xlsx', index=False)




# In[ ]:




