#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


na_vals=['NA',"Missing"]


# In[3]:


df=pd.read_csv("surveypublic2019.csv", index_col='Respondent',na_values=na_vals)


# In[4]:


print(df)


# In[5]:


print(df.shape)


# In[6]:


pd.set_option('display.max_columns',48)


# In[7]:


sdf=pd.read_csv('survey_results_schema.csv')


# In[8]:


print(sdf)


# In[9]:


print(df.head())


# In[10]:


df.tail()


# In[11]:


print(df.head(2))


# In[12]:


persons={
    'first':['dileep','arjun','vikas','krishna'],
    'last':['golla','boddu','vatte','golla'],
     'age':[23,24,25,18],
     'place':['suryapet','hyderabad','kodad','suryapet']
}


# In[13]:


dfp=pd.DataFrame(persons)


# In[14]:


print(dfp)


# In[15]:


print(dfp['age'])


# In[16]:


print(type(dfp['age']))


# In[17]:


dfp.age  #if we dataframe as a method same as the our column then wit will show error sodf 
          #its better not use dot notation to acess the column


# In[18]:


print(dfp[['first','age']])


# In[19]:


print(type(dfp[['first','age']]))


# In[20]:


print(df.columns)


# In[21]:


print(dfp.columns)


# In[22]:


print(dfp.iloc[0])


# In[23]:


print(df.iloc[0])


# In[24]:


print(dfp.iloc[[0,1,2]])


# In[25]:


print(dfp.iloc[[0,1],[1,0]])


# In[26]:


print(dfp.loc[[0,1],['first','age']])


# In[27]:


print(dfp.iloc[0:2,0:2])


# In[28]:


print(dfp['age'].value_counts())


# In[29]:


print(df['Country'].value_counts())


# In[30]:


print(dfp.loc[0,'age'])


# In[31]:


print(dfp.loc[:,"first":'age'])


# In[32]:


print(dfp.iloc[:,0:2])


# In[33]:


print(dfp.loc[0:2,'first'])


# In[34]:


dfp.set_index('first')


# In[35]:


dfp


# In[36]:


dfp.set_index('first',inplace=True)


# In[37]:


dfp


# In[38]:


dfp.index


# In[39]:


dfp.loc['dileep']


# In[40]:


dfp.loc['dileep','age']


# In[41]:


dfp.iloc[0]


# In[42]:


dfp.reset_index(inplace=True)


# In[43]:


dfp


# In[44]:


df


# In[45]:


dfp.set_index('first',inplace=True)


# In[46]:


dfp


# In[47]:


dfp.sort_index()


# In[48]:


dfp.sort_index(inplace=True)


# In[49]:


dfp


# In[50]:


dfp.reset_index(inplace=True)


# In[51]:


dfp


# In[52]:


dfp.describe()


# In[53]:


filt = (dfp['last']=='golla')


# In[54]:


dfp[filt]


# In[55]:


dfp.loc[filt]


# In[56]:


dfp.loc[filt]


# In[57]:


filt2 = (dfp['last'] == 'golla') | ( dfp['first']  == 'dileep')


# In[58]:


dfp[filt2]


# In[59]:


filt2 = (dfp['last'] == 'golla') & ( dfp['first']  == 'dileep')


# In[60]:


dfp[filt2]


# In[61]:


filt2 = (dfp['last'] == 'golla') & ( dfp['first']  == 'dileep')


# In[62]:


dfp[~filt2]


# In[63]:


filt2 = (dfp['last'] == 'golla') | ( dfp['first']  == 'dileep')


# In[64]:


dfp[~filt2]


# In[65]:


df.head()


# In[66]:


filt3= (df['Age']=='18-24 years old')


# In[67]:


df.loc[filt3,'Country']


# In[ ]:





# In[68]:


filt3= (df['Age']=='18-24 years old') & (df['Gender']=="Man")


# In[69]:


df.loc[filt3, ['Age','Country','Gender','Trans'] ]


# In[70]:


countries=['Finland','India','Pakistan','Bangladesh']


# In[71]:


filt=df['Country'].isin(countries)


# In[72]:


df.loc[filt,'Country']


# In[73]:


filt=df['PlatformWorkedWith'].str.contains('Python', na=False)


# In[74]:


filt


# In[ ]:





# In[75]:


df.loc[filt, 'PlatformWorkedWith']


# In[76]:


dfp


# # Updating Columns

# In[77]:


dfp.columns=['first name','last name','age','place']


# In[78]:


dfp


# In[79]:


dfp.columns=[x.upper() for x in dfp.columns]


# In[80]:


dfp


# In[81]:


dfp.columns=dfp.columns.str.replace(' ','_')


# In[82]:


dfp


# In[83]:


dfp.columns=dfp.columns.str.lower()  #dfp.columns=[x.lower() for x in dfp.columns]


# In[84]:


dfp


# In[85]:


dfp.rename(columns={'first_name':'first','last_name':'last'}, inplace=True)


# In[86]:


dfp


# # Updating rows:

# In[87]:


dfp.loc[2]=['kitti','golla',22,'aregudem']


# In[88]:


dfp


# In[89]:


dfp.loc[2,['first','age']]=['pandu',10]


# In[90]:


dfp


# In[91]:


dfp.loc[0,'first']='varun'


# In[92]:


dfp


# In[93]:


dfp.at[2,'first']='Uday Kiran'


# In[94]:


dfp


# In[95]:


filt=dfp['place']=='kodad'


# In[96]:


dfp[filt]['first']='abhi'


# In[97]:


dfp.loc[filt,'first']='abhi'


# In[98]:


dfp


# In[99]:


dfp['first'].str.upper()


# In[100]:


dfp['first']=dfp['first'].str.upper()


# In[101]:


dfp


# In[102]:


dfp['first'].apply(len)


# In[103]:


def lowerCase(first):
    return first.lower()


# In[104]:


dfp['first'].apply(lowerCase)


# In[105]:


dfp['first']=dfp['first'].apply(lowerCase)


# In[106]:


dfp


# In[107]:


dfp['first']=dfp['first'].apply(lambda i:i.upper())


# In[108]:


dfp


# In[109]:


dfp.apply(len)  # here if we apply on whole dataframe then we get length of number of rows.


# In[110]:


len(dfp['first'])


# In[111]:


dfp.apply(len ,axis='columns')  # here if we apply on whole dataframe then we get length of number of columns.


# In[112]:


dfp


# In[113]:


dfp.apply(pd.Series.min)


# In[114]:


pd.Series.min


# In[115]:


dfp.rename(columns={'age':'study'}, inplace=True)


# In[116]:


dfp


# In[117]:


dfp.rename(columns={'study':'age'}, inplace=True)


# In[118]:


dfp


# In[119]:


persons={
    'first':['dileep','arjun','vikas','krishna'],
    'last':['golla','boddu','vatte','golla'],
     'study':['Btech','Degree','Tenth',"Inter"],
     'place':['suryapet','hyderabad','kodad','suryapet']
}


# In[120]:


dfp1=pd.DataFrame(persons)


# In[121]:


dfp1


# In[122]:


dfp1.applymap(len) # len cannot apply to integers


# In[123]:


dfp1=dfp1.applymap(str.upper)


# In[124]:


dfp1


# In[125]:


dfp1['first'].map({'VIKAS':'Allu',"ARJUN":"RAM"})


# In[126]:


dfp1['first']=dfp1['first'].replace({'VIKAS':'Allu',"ARJUN":"RAM"})


# In[127]:


print(dfp1)


# In[128]:


df['SOAccount'].map({'Yes':True,'No':False})


# In[129]:


dfp1['first']+' '+dfp1['last']


# In[130]:


dfp1['Name']=dfp1['first']+' '+dfp1['last']


# In[131]:


dfp1


# In[132]:


dfp1.drop(columns=['first','last'],inplace=True)


# In[133]:


dfp1


# In[134]:


dfp1[['first','last']]=dfp1['Name'].str.split(' ',expand=True)


# In[135]:


dfp1


# In[136]:


dfp1=dfp1.append({'first':'Mark'},ignore_index=True)


# In[137]:


dfp1


# In[138]:


persons={
    'first':['Ntr','RC'],
    'last':['nandy','koni'],
     'study':['mpc','bipc'],
     'place':['hyderabad','filmcity']
}


# In[139]:


dfp2=pd.DataFrame(persons)


# In[140]:


dfp1.append(dfp2,ignore_index=True) #sort=false sets sort error to false


# In[141]:


dfp1=dfp1.append(dfp2,ignore_index=True) 


# In[142]:


dfp1


# In[143]:


dfp1.drop(index=6)


# In[144]:


dfp1=dfp1.drop(index=dfp1[dfp1['last']=='VATTE'].index)


# In[145]:


dfp1


# In[146]:


cgroup=df.groupby('Country')


# In[147]:


cgroup


# In[148]:


cgroup.get_group("India")


# In[149]:


cgroup['SocialMedia'].value_counts()


# In[150]:


cgroup['ConvertedComp'].median().loc['Germany']


# In[151]:


cgroup['ConvertedComp'].agg(['median','mean']).loc['Germany']


# In[152]:


filt=df['Country']=='India'
df.loc[filt]["LanguageWorkedWith"].str.contains('Python').sum()


# In[153]:


#cgroup["LanguageWorkedWith"].str.contains('Python').sum()


# In[154]:


cgroup["LanguageWorkedWith"].apply(lambda x:x.str.contains('Python').sum())


# In[155]:


crespondent=df['Country'].value_counts()


# In[156]:


crespondent


# In[157]:


Cusespython=cgroup["LanguageWorkedWith"].apply(lambda x:x.str.contains('Python').sum())


# In[158]:


Cusespython


# In[159]:


p_df=pd.concat([crespondent,Cusespython], axis='columns', sort=False)
p_df


# In[160]:


p_df.rename(columns={"Country":"NumRespondents","LanguageWorkedWith":"Nknowspython"}, inplace=True)


# In[161]:


p_df['perKnowsPython'] = (p_df["Nknowspython"] / p_df['NumRespondents']) * 100
p_df


# In[162]:


p_df.sort_values(by="perKnowsPython" ,ascending=False, inplace=True)


# In[163]:


p_df.head(50)


# In[164]:


p_df.loc['Japan']


# # Cleaning  data
# 

# In[165]:


dfp1


# In[166]:


dfp0=pd.DataFrame({'study':['NaN',None,'NA'],'place':['NaN','NaN',"Missing"],'Name':['NaN','vijay','NA'],'first':['NaN','NaN','NA'],'last':[None,'NaN','NA'] })


# In[167]:


dfp1=dfp1.append(dfp0,ignore_index=True)


# In[ ]:





# In[168]:


dfp1


# In[ ]:





# In[169]:


dfp1.dropna()


# In[170]:


dfp1.dropna(axis='index',how='all')


# In[171]:


dfp1.dropna(axis='index',how='any')


# In[172]:


dfp1.dropna(axis='columns',how='any')


# In[173]:


dfp1.dropna(axis='columns',how='all')


# In[174]:


dfp1.dropna(axis='index',how='all',subset=['Name','first'])


# In[175]:


dfp1.replace('NA',np.nan,inplace=True)


# In[176]:


dfp1.replace('Missing',np.nan,inplace=True)
dfp1.replace('NaN',np.nan,inplace=True)


# In[177]:


dfp1


# In[178]:


dfp1.dropna()


# In[179]:


dfp1.dropna(axis='index',how='any')


# In[180]:


dfp1.isna()


# In[181]:


dfp1.fillna('Missing')


# In[182]:


dfp


# In[183]:


dfp0=pd.DataFrame({'first':['NaN',None,'NA'],'last':['NaN','NaN',"Missing"],'age':[np.nan,10,'NA'],'place':[np.nan,None,'NA']})


# In[184]:


dfp=dfp.append(dfp0, ignore_index=True)


# In[185]:


dfp


# In[186]:


dfp.replace('NA',np.nan,inplace=True)
dfp.replace("NaN",np.nan,inplace=True)
dfp.replace("Missing",np.nan,inplace=True)
dfp.fillna(0)


# In[187]:


dfp.dtypes


# In[188]:


dfp['age'].mean()


# In[189]:


dfp['age']


# In[190]:


dfp['age'].mean()


# In[191]:


dfp['age']=dfp['age'].astype(float)


# In[192]:


dfp['age']


# In[ ]:





# In[193]:


dfp['age'].mean()


# In[194]:


type(dfp['age'])


# In[195]:


sdf=pd.Series([10,20,30,40])


# In[196]:


sdf


# In[197]:


df['YearsCode'].head()


# In[198]:


df['YearsCode'].unique()


# In[199]:


df['YearsCode'].replace('Less than 1 year',0 ,inplace=True)
df['YearsCode'].replace('More than 50 years',51 ,inplace=True)


# In[200]:


df['YearsCode']=df['YearsCode'].astype(float)


# In[201]:


df['YearsCode'].mean()


# In[202]:


df['YearsCode'].median()


# In[ ]:




