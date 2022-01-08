#!/usr/bin/env python
# coding: utf-8

# ##  Email slicer

# Get user email address

# In[67]:


email = input("Enter your email address: ").strip()


# Slice out user name

# In[68]:


user = email[:email.index("@")]


# Slice out domain name

# In[69]:


domain = email[email.index("@")+1:]


# Displaying message

# In[70]:


message = "Your Email address is {}\nYour email user name is {}\nYour email domain name is {}"


# In[71]:


output = message.format(email, user, domain)


# In[72]:


print(output)


# Format Shortcut

# In[75]:


message = "Your Email address is {}\nYour email user name is {}\nYour email domain name is {}".format(email, user, domain)


# In[76]:


print(message)


# In[ ]:




