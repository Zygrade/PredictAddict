
# coding: utf-8

# In[178]:

import pandas as pd
import numpy as np
import json
import urllib2
import requests

request='myrequest'
data = requests.get(request)
json = data.json()
df = pd.DataFrame(json)
df = df.values

import sys

data = {}
data['sex'] = sys.argv[1]
data['address'] = sys.argv[2]
data['familysize'] = sys.argv[3]
data['Pstatus'] = sys.argv[4]
data['Medu'] = sys.argv[5]
data['Fedu'] = sys.argv[6]
data['Mjob'] = sys.argv[7]
data['Fjob'] = sys.argv[8]
data['traveltime'] = sys.argv[9]
data['studytime'] = sys.argv[10]
data['failures'] = sys.argv[11]
data['paid'] = sys.argv[12]
data['activities'] = sys.argv[13]
data['famrel'] = sys.argv[14]
data['goout'] = sys.argv[15]
data['percentage'] = sys.argv[16]


# In[179]:

data = pd.read_csv("student-mat.csv")


# In[180]:

data.head()


# In[181]:

y = np.array(data[["Dalc","Walc"]])


# In[182]:

labels = 2*y[:,0] + y[:,1]


# In[183]:

data.drop(["Dalc","Walc"], inplace=True, axis = 1)


# In[184]:

data.drop(["school", "age", "reason","guardian", "schoolsup", "famsup", "nursery", "higher","internet", "romantic", "freetime","health", "absences"], inplace = True, axis = 1)


# In[185]:

data


# In[186]:

grades = np.array(data[["G1","G2","G3"]])


# In[187]:

per = grades[:,0] + grades[:,1] + grades[:, 2]


# In[188]:

per = per*5/3


# In[189]:

per.shape


# In[190]:

data.drop(["G1", "G2", "G3"], inplace = True, axis = 1)


# In[191]:

data.head(10)


# In[192]:

data['address'].value_counts()


# In[193]:

data['sex'].value_counts()


# In[194]:

di = {'M' : 0, 'F' : 1}
data.replace({'sex':di}, inplace = True)


# In[195]:

di = { 'U' : 0, 'R' : 1}
data.replace({'address':di},inplace=True)


# In[ ]:




# In[196]:

data['famsize'].value_counts()


# In[197]:

di = {'LE3' : 0,'GT3' : 1}
data.replace({'famsize':di},inplace = True)


# In[198]:

data.head(6)


# In[199]:

di = { 'A' : 0, 'T' : 1}
data.replace({'Pstatus':di},inplace=True)


# In[200]:

data.head(6)


# In[201]:

data['Mjob'].value_counts()


# In[202]:

di = { 'teacher' : 0, 'health' : 1, 'services' : 2, 'at_home' : 3, 'other' : 4}
data.replace({'Mjob':di},inplace=True)


# In[203]:

data.head(6)


# In[204]:

data['Fjob'].value_counts()


# In[205]:

di = { 'teacher' : 0, 'health' : 1, 'services' : 2, 'at_home' : 3, 'other' : 4}
data.replace({'Fjob':di},inplace=True)


# In[206]:

data.head(6)


# In[207]:

data['paid'].value_counts()


# In[208]:

di = { 'no' : 0, 'yes' : 1}
data.replace({'paid':di},inplace=True)


# In[209]:

di = { 'no' : 0, 'yes' : 1}
data.replace({'activities':di},inplace=True)


# In[210]:

data.shape


# In[211]:

test = np.array(data)


# In[212]:

test


# In[213]:

test.shape


# In[214]:

train = np.zeros((395,16))


# In[215]:

train[:,:15] = test[:,:]


# In[216]:

train[:,15] = per


# In[217]:

train.shape


# In[218]:

labels = labels // 10


# In[219]:

labels.shape


# In[220]:

from sklearn.ensemble import RandomForestClassifier


# In[221]:

clf = RandomForestClassifier(n_estimators=60)


# In[222]:

)


# In[223]:

X_test.shape


# In[224]:

y_test.shape


# In[225]:

clf.fit(train, labels)


# In[226]:

y_A = clf.predict(df)


# In[227]:

y_A

print(y_A)
sys.stdout.flush()


# In[ ]:
