#!/usr/bin/env python
# coding: utf-8

# # Data analysis project

# In[2]:


import pandas as pd


# In[3]:


data=pd.read_csv(r"D:\Downloads\file.csv")


# In[4]:


data


# In[6]:


data.shape


# In[7]:


data.index


# In[10]:


data.columns


# In[11]:


data.dtypes


# In[13]:


data["Weather"].unique()


# In[15]:


data.nunique()


# In[16]:


data.count()


# In[17]:


data["Weather"].value_counts


# In[19]:


data["Temp_C"].value_counts()


# In[20]:


data["Weather"].value_counts()


# In[21]:


data.info()


# ## 1) Finding all unique 'Wind Speed' values in data frame

# In[6]:


data['Wind Speed_km/h'].unique()


# ## 2) Finding number of times when Wether is exactly 'Clear'

# In[7]:


data['Weather'].value_counts()


# ## 3) Finding number of times when Wind Speed was exactly 4km/h

# In[9]:


data['Wind Speed_km/h'].value_counts()


# ## 4) Finding all null values in data frame

# In[10]:


data.isnull().sum()


# ## 5) Renaming column Weather to Weather conditions

# In[7]:


data.rename(columns = {'Weather': 'Weather conditions'}, inplace= True)


# In[8]:


data.head()


# ## 6) Finding mean Visibility

# In[15]:


data['Visibility_km'].mean()


# ## 7) Finding standard deviation of Pressure

# In[16]:


data.Press_kPa.std()


# ## 8) Finding variance of Relative Humidity

# In[18]:


data['Rel Hum_%'].var()


# ## 9) Finding every instance where 'Snow' was recorded

# In[9]:


data[data['Weather conditions'] == 'Snow']


# ## 10) Finding all instances where Wind speed is above 24 and Visibility is 25

# In[11]:


data[(data['Wind Speed_km/h']>24)&(data['Visibility_km']==25)]


# ## 11) Finding mean value of each column against 'Weather condition'

# In[13]:


data.groupby('Weather conditions').mean()


# ## 12) Finding minimum and maximum value of each column against 'Weather condition'

# In[14]:


data.groupby('Weather conditions').min()


# In[15]:


data.groupby('Weather conditions').max()


# ## 13) Show all records where Weather condition is Fog

# In[16]:


data[data['Weather conditions']== 'Fog']


# ## 14) FInding all instances where Visibility is greater than 40 or Weather is Clear

# In[17]:


data[(data['Weather conditions']== 'Clear')| (data['Visibility_km']> 40)]


# ## 15) Finding all instances where Weather is Clear and Humidity is greather than 50 or Visibility is above 40

# In[19]:


data[(((data['Weather conditions']== 'Clear')&(data['Rel Hum_%']>50))|(data['Visibility_km']>40))]


# In[ ]:




