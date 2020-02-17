#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[9]:


bank_data=pd.read_csv('bank.csv', sep=';')


# In[10]:


bank_data


# In[11]:


bank_data.head()


# In[12]:


bank_data.tail()


# In[13]:


bank_data.tail(11)


# If  you run head()

# In[25]:


bank_data.info()


# In[26]:


bank_data.shape


# In[29]:


bank_data.describe()


# Explanation:
# * count means amount of entries, overall 4521
# 
# 
# * mean is adding all variables and dividing by their amount
# 
# * mean of 'age' means the average of age variations, it is 41.170095
# * mean of 'balance' means the average of balance variations, it is 1422.657819
# * mean of 'day' means the average of the number of last contact day of the month, it is 15.915284
# * mean of 'duration' is the average of last contact durations, it is 263.961292
# * mean of 'campaign' means the average of the number of contacts performed during this campaign and for this client, it is 2.793630
# * mean of 'pdays' is the average of the number of days that passed by after the client was last contacted from a previous campaign, it is 39.766645
# * mean of 'previous' means the average of the number of contacts performed before this campaign and for this client , it is 0.542579
# 
# 
# * std is standard deviation of columns, measure of how spread out numbers. The formula is: is the square root of the Variance, while Variance defined as the average of the squared differences from the Mean.
# 
# * std of 'age' is 10.576211
# * std of 'balance' is 1422.657819
# * std of the number of last contact day of the month is 8.247667
# * std of last contact duration is 259.856633
# * std of the number of contacts performed during this campaign and for this client is 3.109807
# * std of the number of days that passed by after the client was last contacted from a previous campaign is 100.121124
# * std of the number of contacts performed before this campaign and for this client is 1.693562
# 
# 
# * min is the minimum variable of each column
# 
# * min of 'age' is 19
# * min of 'balance' is -3313
# * min of the number of last contact day of the month is 1
# * min of last contact duration is 4
# * min of the number of contacts performed during this campaign and for this client is 1
# * min of the number of days that passed by after the client was last contacted from a previous campaign is -1
# * min of the number of contacts performed before this campaign and for this client is 0
# 
# 
# * max is the maximum variable of each column
# 
# * max of 'age' is 87
# * max of 'balance' is 71188
# * max of the number of last contact day of the month is 31
# * max of the last contact duration is 3025
# * max of the number of contacts performed during this campaign and for this client is 50
# * max of the number of days that passed by after the client was last contacted from a previous campaign is 871
# * max of the number of contacts performed before this campaign and for this client is 25
# 
# * 25% shows the variable in the 25th percentale column, and respectively with 50% and 75%.
# 

# In[33]:


from pandas import DataFrame


# In[34]:


print(bank_data.corr())


# In[35]:


print(bank_data.cov())


# Explanation(2):
# 
# * Table of correlation shows the relationship and connection between two variables in the table
# 
# * For example: age and age is same, because of this correlation is 1; but age and balance is increasing and decreasing with the relationship of 0.083820, it means that they are actually not dependent to each other
# * Obviously, age, balance, day, duration, campaign, pdays, and previous do not closely correleated to each other, because the numbers which shows us the correlation are too small.
# 
# 
# 

# In[ ]:




