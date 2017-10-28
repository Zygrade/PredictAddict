
# coding: utf-8

# In[178]:

import pandas as pd
import numpy as np


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

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(train, labels, test_size=0.2)


# In[223]:

X_test.shape


# In[224]:

y_test.shape


# In[225]:

clf.fit(X_train, y_train)


# In[226]:

y_A = clf.predict(X_test)


# In[227]:

y_A


# In[228]:

y_test


# In[229]:

100*float((y_A==y_test).sum())/y_test.shape[0]


# In[ ]:



