#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import plotly.express as px


# In[2]:


df=pd.read_csv(r"C:\Users\LalithKishore 16\Downloads\complaints.csv\complaints.csv")


# In[3]:


df.head()


# In[14]:


df.info()


#  1) this data is about product delivery and Consumer complaint 
#  2) through visulazition we can indentify responces and make decision in bussines

# In[5]:


import seaborn as sns
sns.histplot(df['Product'], kde=False, bins=10)


# In[ ]:


import seaborn as sns

# Assuming 'df' is your DataFrame and 'ZIP code' is the column name
sns.countplot(x='ZIP code', data=df)


# In[ ]:


## Bar plot
sns.barplot(x='Complaint ID',y='ZIP code',data=df)


# # 2. Given an unsorted array of integers, find the length of the longest continuous
# increasing subsequence (subarray). 
# Example 1:
# Input: [1,3,5,4,7]
# Output: 3 
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1

# In[3]:


def findLengthOfLCIS(nums):
    if not nums:
        return 0
    
    max_len = 1
    current_len = 1
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1
    
    max_len = max(max_len, current_len)
    return max_len

# Get input from the user
user_input = input("Enter a list of integers separated by spaces: ")
nums = list(map(int, user_input.split()))

# Call the function and print the result
print("Length of the longest continuous increasing subsequence:", findLengthOfLCIS(nums))


# # 3. Given a list of non negative integers, arrange them such that they form the largest
# number.
#  
#  Example 1:
#  Input: [10,2]
#  Output: &quot;210&quot;
#  Example 2:
#  
#  Input: [3,30,34,5,9]
#  Output: &quot;9534330&quot;

# In[4]:


def largestNumber(nums):
    # Convert the integers to strings
    nums_str = list(map(str, nums))
    
    # Sort strings based on custom key
    nums_str.sort(key=lambda x: x*10, reverse=True)
    
    # Join the sorted list into a single string
    largest_num = ''.join(nums_str)
    
    # Edge case: when the list contains only zeros
    if largest_num[0] == '0':
        return '0'
    
    return largest_num

# Get input from the user
user_input = input("Enter a list of non-negative integers separated by spaces: ")
nums = list(map(int, user_input.split()))

# Call the function and print the result
print("Largest number formed is:", largestNumber(nums))


# # 4. Store all the &quot;servlet-name&quot;, and &quot;servlet-class&quot; to a csv file from the attached
# 

# In[6]:


import json
import csv

# Read the JSON data from a file
with open('DT A1 sample_json .json', 'r') as file:
    data = json.load(file)

# Extract servlet details
servlets = data["web-app"]["servlet"]

# Prepare the CSV file
with open('servlets.csv', 'w', newline='') as csvfile:
    fieldnames = ['servlet-name', 'servlet-class']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header
    writer.writeheader()
    
    # Write the servlet details
    for servlet in servlets:
        writer.writerow({'servlet-name': servlet['servlet-name'], 'servlet-class': servlet['servlet-class']})

print("Data has been written to servlets.csv")


# In[7]:


import pandas as pd


# In[8]:


d = pd.read_csv('servlets.csv')


# In[9]:


d


# In[ ]:




