#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import the time module
import time
  
# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(2)
        t -= 2
      
    print('Fire in the hole!!')
  # input time in seconds
t = input("Enter the time in seconds: ")
  
# function call
countdown(int(t))

