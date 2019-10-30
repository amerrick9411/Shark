#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pyodbc
from datetime import datetime, timedelta
import csv


# In[15]:


conn = pyodbc.connect('DSN=Kubrick_SQL;UID=de14;PWD=password')
cur = conn.cursor() 


# In[16]:


shark_data = r'c:\Data\shark_attack_data.csv'


# In[17]:


attack_dates = []
case =[]
country =[]
activity = []
age =[]
gender = []
isfatal =[]
with open(shark_data, encoding = 'UTF-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        case.append(row['Case Number'])
        attack_dates.append(row['Date'])
        country.append(row['Country'])
        activity.append(row['Activity'])
        age.append(row['Age'])
        gender.append(row['Sex '])
        isfatal.append(row['Fatal (Y/N)'])


# In[8]:


cur.execute('truncate table Adrian.shark')


# In[9]:


data = zip(attack_dates, case, country, activity, age, gender, isfatal)


# In[10]:


cur.execute('truncate table Adrian.shark')


# In[11]:


query2 = 'insert into Adrian.shark(attack_date, case_number, country, activity, age, gender, isfatal) values (?,?,?,?,?,?,?)'


# In[12]:


for d in data: # for each row in data, insert the specified columns with the parameters in d (data is the zipped shark columns that should have been collected earlier)
    try:
        cur.execute(q, d)
        conn.commit()
    except:
        conn.rollback 


# In[ ]:




