#!/usr/bin/env python
# coding: utf-8

# In[15]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[16]:


url = 'https://www.worldometers.info/world-population/population-by-country/'
response = requests.get(url)
response


# In[17]:


soup= BeautifulSoup(response.text, 'html.parser')
soup


# In[18]:


rows= soup.find('table', {'id':'example2'}).find('tbody').find_all('tr')
len(rows)


# In[21]:


countries_list = []
for row in rows:
    dic = {}
    dic['Country']= row.find_all('td')[1].text
    dic['Population 2023']= row.find_all('td')[2].text.replace(',','')
    dic['yearly change']= row.find_all('td')[3].text
    dic['Net Change']= row.find_all('td')[4].text
    dic['Density(P/km2)']= row.find_all('td')[5].text
    dic['Land Area(km2)']= row.find_all('td')[6].text.replace(',','')
    dic['Migrants(net)']= row.find_all('td')[7].text.replace(',','')
    dic['Fert Rate']= row.find_all('td')[8].text
    dic['Med. Age']= row.find_all('td')[9].text
    dic['Urban Pop.']= row.find_all('td')[10].text
    dic['World share']= row.find_all('td')[11].text
    countries_list.append(dic)
countries_list[1]


# In[24]:


df = pd.DataFrame(countries_list)
df.to_csv(r'C:\Users\user\OneDrive\Desktop\extras\Data analysis projects/countries_data.csv', index=False)


# In[ ]:





# In[ ]:





# In[ ]:




