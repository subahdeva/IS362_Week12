#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

mushroom = {'number': {'e': 0, 'p':1}, 'name': {'e': 'Edible', 'p': 'Poisonous'}}

scent = {'number': {'a' : 0,'l' : 1,'c' : 2,'y' : 3,'f' : 4,'m' : 5,'n' : 6,'p' : 7,'s' : 8},
             'name': {'a' : 'Almond','l' : 'Anise','c' : 'Creosote','y' : 'Fishy',
                      'f' : 'Foul','m' : 'Musty','n' : 'None','p' : 'Pungent','s' : 'Spicy'}}

color = {'number': {'k':0,'n':1,'b':2,'h':3,'g':4,'r':5,
         'o':6,'p':7,'u':8,'e':9,'w':10,'y':11},
             'name': {'k':'Black','n':'Brown','b':'Buff','h':'Chocolate','g':'Gray','r':'Green',
         'o':'Orange','p':'Pink','u':'Purple','e':'Red','w':'White','y':'Yellow'}}

cols = ['Class Type', 'Odor', 'Gill Color']
colname = ['Class Name', 'Odor Name', 'Gill Color Name']

df = pd.read_table('agaricus-lepiota.data', delimiter=',', header=None, usecols=[0,5,9])
df.columns = cols

df2 = df.copy()
df2.columns = colname
df = pd.concat([df, df2], axis=1)
df["Class Type"] = df["Class Type"].map(mushroom['number'])
df["Odor"] = df["Odor"].map(scent['number'])
df["Gill Color"] = df["Gill Color"].map(color['number'])
df["Class Name"] = df["Class Name"].map(mushroom['name'])
df["Odor Name"] = df["Odor Name"].map(scent['name'])
df["Gill Color Name"] = df["Gill Color Name"].map(color['name'])

df.head()


# In[23]:


a = sns.countplot(x='Class Name', data=df)
plt.xlabel("Type",size = 15)
plt.ylabel("Count",size = 15)


# In[26]:


b = sns.countplot(x="Odor Name", data=df, hue='Class Name')
plt.xlabel("Scent",size = 15)
plt.ylabel("Count",size = 15)
plt.xticks(rotation=30)


# In[28]:


c = sns.countplot(x="Gill Color Name", data=df, hue='Class Name')
plt.xlabel("Gill Color",size = 15)
plt.ylabel("Count",size = 15)
plt.xticks(rotation=30)


# In[29]:


d = sns.lmplot(x='Class Type', y="Odor", data=df)
plt.title('Class Type and Odor', fontsize=20)
plt.xlabel("Class",size = 15)
plt.ylabel("Odor",size = 15)
plt.xticks([0, 1])


# In[31]:


e = sns.lmplot(x='Gill Color', y="Odor", data=df, hue='Class Type')
plt.title('Gill Color and Odor', fontsize=20)
plt.xlabel("Gill Color",size = 15)
plt.ylabel("Odor",size = 15)


# In[32]:


f = sns.lmplot(x='Class Type', y="Gill Color", data=df)
plt.title('Gill Color and Class', fontsize=20)
plt.xlabel("Class",size = 15)
plt.ylabel("Gill Color",size = 15)
plt.xticks([0, 1])


# In[34]:


# Looking at these columns of data can be helpful in determining which mushrooms are edible or poisonous especially
# when foraging. The best indicator is odor as that can tell you if the smell is bad that it can't be safe to eat.
# However, color is helpful in what is considered "normal" for mushrooms to be edible as well. In some cases, I 
# imagine, understanding the different classes and colors of mushrooms can also differentiate which mushrooms can be
# eaten raw or only cooked. 


# In[ ]:




