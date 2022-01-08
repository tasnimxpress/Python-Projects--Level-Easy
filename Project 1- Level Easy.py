#!/usr/bin/env python
# coding: utf-8

# ## Hey, Hello!

# Ask user for name

# In[3]:


name = input("What's your name?\n")


# Ask user for age

# In[4]:


age = input("How old are you?\n")


# Ask user for city

# In[5]:


city = input("Which city are you form?\n")


# Ask user what they enjoy

# In[8]:


interest = input("What do you enjoy most?\n")


# Using Concatination

# In[28]:


message = "Hey! Genious! We got you here.\nYour name is " + name +"." + "\nYou are "+ str(age) +" years old.\nYou live in "+ city +".\nYou love "+ interest +".\nThese is all we know about you. Hope you are doing fine."


# In[29]:


print(message)


# Using string format

# In[37]:


message = "Hey! Genious! We got you here.\nYour name is {}.\nYou are {} years old.\nYou live in {}.\nYou love {}.\nHope you are doing fine!\nFor now, These is all we know about you." 


# In[38]:


output = message.format(name, age, city, interest)


# In[39]:


print(output)


# In[ ]:




