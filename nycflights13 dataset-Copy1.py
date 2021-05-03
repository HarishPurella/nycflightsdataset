#!/usr/bin/env python
# coding: utf-8

# In[184]:


from nycflights13 import flights
from nycflights13 import airports


# In[185]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[ ]:


#### Read the data from the file


# In[186]:


df=pd.read_csv("Desktop/datafly.csv")


# In[83]:


df.head()


# In[110]:


df.isna().sum()


# In[112]:


df.shape


# In[ ]:





# In[ ]:


##### remove the unnecessary columns


# In[188]:


df.drop(["Unnamed: 0"],axis=1,inplace=True)


# In[189]:


df.head()


# In[ ]:





# In[ ]:


#####Divede the data into catagorical and numerical


# In[190]:


dfcat=df.select_dtypes(object)
dfnum=df.select_dtypes(np.number)


# In[196]:


dfcat


# In[ ]:


##### processing of the catagorical columns


# In[191]:


dfcat.isna().sum()


# In[ ]:


###### Import simpleImputer from sklearn to fill the catagorical null values


# In[ ]:





# In[192]:


from sklearn.impute import SimpleImputer
sImputer=SimpleImputer(strategy="most_frequent")


# In[193]:


sImputer.fit(dfcat)


# In[194]:


dfcatnaremoved=pd.DataFrame(sImputer.transform(dfcat),columns=dfcat.columns)


# In[195]:


dfcatnaremoved


# In[ ]:


#####processing of the numerical columns


# In[199]:


dfnum.isna().sum()


# In[ ]:





# In[ ]:


###### Import simpleImputer from sklearn to fill the numerical null values


# In[200]:


from sklearn.impute import SimpleImputer
sImputer1=SimpleImputer(strategy="mean")


# In[201]:


sImputer1.fit(dfnum)


# In[202]:


dfnumnaremoved=pd.DataFrame(sImputer1.transform(dfnum),columns=dfnum.columns)


# In[203]:


dfnumnaremoved.isna().sum()


# In[ ]:


####### concatenation of Both numerical and catagorical columns


# In[207]:


df1=pd.concat([dfcatnaremoved,dfnumnaremoved],axis=1)


# In[208]:


df1.head()


# In[ ]:





# In[ ]:





# In[ ]:


###########################################################
#### Using the flights data, Find all the flights that ####


# In[ ]:


####Q4. Had an delay in arrival of 3 or less hours


# In[209]:


df1[df1["arr_delay"] >= 120]


# In[ ]:


###### Q5. Flew to Houston (IAH or HOU)


# In[210]:


df1[(df1["dest"] == "IAH") | (df1["dest"] == "HOU")]


# In[ ]:


#######Q6. Were operated by United, American, or Delta


# In[211]:


df1[((df1['carrier']=="AA") | (df1['carrier']=='DL') | (df1['carrier']=='UA'))]


# In[ ]:


##### Q7. Departed in summer (July, August, and September)


# In[212]:


df1[((df1['month']==7) | (df1['month']==8) & (df1['month']==9))]


# In[ ]:





# In[81]:


##### Q8. Arrived more than two hours late, but didn???t leave late


# In[213]:


df1[df1['dep_delay']<=0]


# In[113]:


########Q8. Arrived more than two hours late, but didn???t leave late


# In[214]:


df1[((df1["arr_delay"]> 120) & (df1['dep_delay']<= 0))]


# In[115]:


######## Q9. Were delayed by at least an hour, but made up over 30 minutes in flight


# In[215]:


df1[((df1['dep_delay']>= 60) & ((df1["dep_delay"]-df1['arr_delay'])>30))]


# In[130]:


######Q10. Departed between midnight and 6am (inclusive)


# In[221]:


df1[(df1["dep_time"]<=600) | (df1["dep_time"]==2400)]


# In[217]:


df1['dep_time'].max


# In[218]:


df1['dep_time'].describe


# In[137]:


#####Q1. Write a function that given your birthday (as a date), returns how old you are in years.


# In[222]:


import datetime
birthdate=int(input("Enter birth year: "))
age=datetime.datetime.now().year - birthdate
print("your age is:",age,"years")


# In[219]:


#######Q3. How do you import default dataset presend in python to work session


# In[ ]:


###Ans::   data = pd.read_csv("filename.csv") 
#####      sns.load_dataset("filename")

