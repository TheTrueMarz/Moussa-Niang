#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(100, -1, -10)


# In[2]:


for x in range(100, -1, -10)


# In[3]:


for x in range(100, -1, -10):
    print(x)


# In[4]:


#Class Example
grades = [[79, 95, 60],
 [95, 60, 61],
 [99, 67, 84],
 [76, 76, 97],
 [91, 84, 98],
 [70, 69, 96],
 [88, 65, 76],
 [67, 73, 80],
 [82, 89, 61],
 [94, 67, 88]]
    


# In[5]:


grades[0][2]


# In[6]:


grades[1]


# In[15]:


[mid[0] for mid in grades]


# In[21]:


[mid[0] for mid in grades]


# In[22]:


[mid[0] for mid in grades[:3]]


# In[33]:


new_list = list(zip(*grades))


# In[34]:


print(new_list)


# In[38]:


import numpy


# In[40]:


x = numpy.mean(grades)


# In[41]:


print(x)


# In[ ]:




