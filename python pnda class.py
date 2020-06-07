#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[8]:


import numpy as np


# In[ ]:





# In[6]:


d=pd.date_range('28/5/2020',periods=7,freq='Y')


# In[7]:


d


# In[ ]:





# In[9]:


np.arange(7)


# In[19]:


s=pd.Series(np.arange(2,9),index=[3,4,5,6,"vikas","singh",8])


# In[20]:


s


# In[21]:


import csv


# In[26]:


a=[1,2,9,0]
b=[5,6]
c=[4,8,9]
list(zip(a,b,c))


# In[33]:


obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"],"key1" :[1,2,34]},
              {"name": "Katie", "age": 38,
               "pets": ["Sixes", "Stache", "Cisco"]}]
}
"""


# In[34]:


import json


# In[35]:


j=json.loads(obj)
j


# In[36]:


j['siblings']


# In[39]:


pd.DataFrame(j['siblings'],columns=['name','pets'])


# In[41]:


d.to_json("ss.json",orient='records')


# In[44]:


import requests


# In[45]:


l=['a','b','c']
ll=[1,2,3,4]
d={'a':1,'b':2,'c':5}


# In[ ]:




