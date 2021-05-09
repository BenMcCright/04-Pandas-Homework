#!/usr/bin/env python
# coding: utf-8

# # A Whale off the Port(folio)
# ---
# 
# In this assignment, you'll get to use what you've learned this week to evaluate the performance among various algorithmic, hedge, andmutual fund portfolios and compare them against the S&P 500 Index.

# In[1]:


# Initial Imports

import pandas as pd
import numpy as np
import datetime as dt
from pathlib import Path

get_ipython().run_line_magic('matplotlib', 'inline')


# # Data Cleaning
# 
# In this section, you will need to read the CSV files into DataFrames and perform any necessary data cleaning steps. After cleaning, combine all DataFrames into a single DataFrame.
# 
# Files:
# 
# * `whale_returns.csv`: Contains returns of some famous "whale" investors' portfolios.
# 
# * `algo_returns.csv`: Contains returns from the in-house trading algorithms from Harold's company.
# 
# * `sp500_history.csv`: Contains historical closing prices of the S&P 500 Index.

# ## Whale Returns
# 
# Read the Whale Portfolio daily returns and clean the data

# In[7]:


# Reading whale returns
path = "C:/Users/bmccr/smu-virt-fin-pt-04-2021-u-c/smu-virt-fin-pt-04-2021-u-c/04-Pandas/Pandas Homework/Starter_Code/Resources/"
whale_df = pd.read_csv(path + "whale_returns.csv")
whale_df["Date"] = pd.to_datetime(whale_df["Date"])
whale_df.head()


# In[13]:


whale_df.shape


# In[12]:


# Count nulls
whale_df.isnull().count()


# In[14]:


# Drop nulls
whale_df.dropna(inplace = True)


# In[15]:


whale_df.shape


# ## Algorithmic Daily Returns
# 
# Read the algorithmic daily returns and clean the data

# In[ ]:


# Reading algorithmic returns


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


combined_df = pd.merge(whale_df,algo_df, how ="inner", on = "Date")

combined_df = combined_df.T.drop_duplicates().T
combined_df

