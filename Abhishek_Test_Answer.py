#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
data1=pd.read_csv('https://raw.githubusercontent.com/Bungeetech/internship-test/master/input/main.csv',error_bad_lines=False)
type(False)
booleans=[]
for country in data1.COUNTRY:
    if 'USA' in country:
        booleans.append(True)
    else:
        booleans.append(False)
is_long=pd.Series(booleans)
data1[is_long]
c= pd.DataFrame(data1[is_long])
c.to_csv(r'C:\Users\POOJA\Downloads\output\filteredCountry.csv', index=False)


# In[15]:


import pandas as pd
df = pd.read_csv (r'C:\Users\POOJA\Downloads\output\filteredCountry.csv',usecols=['SKU', 'PRICE'])
df.groupby('SKU')['PRICE'].apply(list)
df1 = df.groupby('SKU')['PRICE'].apply(list).reset_index(name='PRICE')
c1= pd.DataFrame(df1)
c1.to_csv(r'C:\Users\POOJA\Downloads\working\TempF.csv', index=False)
data = pd.read_csv (r'C:\Users\POOJA\Untitled Folder\TempF.csv')
data['PRICE'] =  data['PRICE'].apply(lambda x: x.replace('[','').replace(']','').replace('$','').replace('.00','').replace('?',''))
new = data['PRICE'].str.split(", ", n = 5, expand = True)
data['FIRST_MINIMUM_PRICE']= new[0]
data['FIRST_MINIMUM_PRICE'] =  data['FIRST_MINIMUM_PRICE'].str.strip(" ' ")
data['SECOND_MINIMUM_PRICE']= new[1]
data['SECOND_MINIMUM_PRICE'] =  data['SECOND_MINIMUM_PRICE'].str.strip(" ' ")
data.drop(columns =["PRICE"], inplace = True)
data.dropna(inplace = True)
data
c2= pd.DataFrame(data)
c2.to_csv(r'C:\Users\POOJA\Downloads\output\lowestPrice.csv', index=False)


# In[ ]:




