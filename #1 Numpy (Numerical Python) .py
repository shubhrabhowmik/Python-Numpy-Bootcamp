#!/usr/bin/env python
# coding: utf-8

# Array Creation and Initialization Function

# In[14]:


import numpy as np  #mathemetical functions


# In[15]:


# Creating 1D array

mylist1 = [101,102,103]
myArray = np.array(mylist1)

print(myArray)


# In[16]:


# Creating 2D array

mylist2 = [101,102,103]
myArray2D = np.array([mylist1,mylist2])

print(myArray2D)


# In[17]:


# Finding dimensions of the Array - Shape() function

print(myArray.shape)
print(myArray2D.shape)


# In[18]:


# Finding the datatype of Array - dtype() function

print(myArray.dtype)
print(myArray2D.dtype)


# In[19]:


# Array Creation and initialization function - Zeros

zero_array = np.zeros(5)
print(zero_array)

zero_array2D = np.zeros([3,2])
print(zero_array2D)


# In[20]:


# Array Creation and initialization function - Ones

ones_array = np.ones(5)
print(ones_array)

ones_array2D = np.ones([3,2])
print(ones_array2D)


# In[21]:


# Array Creation and Initialization Function - empty (any junk value will be printed)

empty_array = np.empty(5)
print(empty_array)

empty_array2D = np.empty([3,2])
print(empty_array2D)


# In[22]:


# Array creation and Initialization - eye (Digonal elements are same)

Identity_Array = np.eye(3)
print(Identity_Array)


# In[23]:


# Arange() Function - arange(start_value, end_value, difference)

AP_Array = np.arange(0,50,2)
print(AP_Array)


# In[ ]:




