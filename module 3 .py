#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandasql import sqldf


# In[35]:



#dataset for csv 1 
df1 = pd.read_csv('/Users/sky-walker/Downloads/module3_assignment_data_1.csv')
df1.head(25)


# In[53]:


#dataset for csv 2 
df2 = pd.read_csv('/Users/sky-walker/Downloads/module3_2.csv')
df2.head(25)


# In[29]:


#append the datsets 
df_append = df1.append(df2) 
df_append.describe(include='all')


# In[30]:


#query to only select the customers that have a loyalty status of gold
sqldf("select first_name, loyalty_status from df_append where loyalty_status = 'Gold';")


# In[38]:


#query to select first_name, email, total spend, and most traveled state
sqldf("select first_name, email, total_spend_2021, most_traveled_state from df_append;")


# In[39]:


#query to select first name, last name, email, and loyalty status from the dataset
sqldf('select first_name, email, loyalty_status from df_append;')


# In[47]:


#query for loyalty status, education, and total spend where the most traveled state is New York.
sqldf("select loyalty_status, education, total_spend_2021, most_traveled_state from df_append where most_traveled_state = 'NY';")


# In[48]:


#Delete rows that are missing in the first dataset
df1.dropna(inplace=True)
df1.head(25)


# In[52]:


#Recode gender and education columns

df_dc = pd.get_dummies(df_append, columns=['gender', 'education'])
df_dc.head()


# In[ ]:




