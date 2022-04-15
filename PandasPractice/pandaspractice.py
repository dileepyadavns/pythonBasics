#importing libraries
import pandas as pd
import numpy as np

na_vals=['NA',"Missing"] #to check for null values

df=pd.read_csv("surveypublic2019.csv", index_col='Respondent',na_values=na_vals) # read dataframe

print(df)

print(df.shape)

pd.set_option('display.max_columns',48) #to make adjust how many columns and rows to be printed in dataframe

sdf=pd.read_csv('survey_results_schema.csv') #read dataframe

print(sdf)

print(df.head()) #top 5 rows in dataframe

print(df.tail()) #bottom 5 rows

print(df.head(2))

#dictionary for creating dataframe
persons={
    'first':['dileep','arjun','vikas','krishna'],
    'last':['golla','boddu','vatte','golla'],
     'age':[23,24,25,18],
     'place':['suryapet','hyderabad','kodad','suryapet']
}

dfp=pd.DataFrame(persons) #created dataframe

print(dfp)
print(dfp['age']) #prints age column
print(type(dfp['age'])) #gives type of column

dfp.age  #if we dataframe as a method same as the our column then wit will show error sodf 
          #its better not use dot notation to acess the column

print(dfp[['first','age']])

print(type(dfp[['first','age']]))
print(df.columns) #all columns in dataframe will be printed

print(dfp.columns)

print(dfp.iloc[0])
print(df.iloc[0])
print(dfp.iloc[[0,1,2]])


print(dfp.iloc[[0,1],[1,0]])

print(dfp.loc[[0,1],['first','age']])

print(dfp.iloc[0:2,0:2])

print(dfp['age'].value_counts())

print(df['Country'].value_counts())

print(dfp.loc[0,'age'])

print(dfp.loc[:,"first":'age'])

print(dfp.iloc[:,0:2])

print(dfp.loc[0:2,'first'])

dfp.set_index('first') #to set index

print(dfp)

dfp.set_index('first',inplace=True)

print(dfp)

print(dfp.index)
print(dfp.loc['dileep'])

print(dfp.loc['dileep','age'])

print(dfp.iloc[0])

dfp.reset_index(inplace=True)

print(dfp)

print(df)

dfp.set_index('first',inplace=True)

print(dfp)

print(dfp.sort_index())
dfp.sort_index(inplace=True)


print(dfp)

dfp.reset_index(inplace=True)

print(dfp)
print(dfp.describe())
filt = (dfp['last']=='golla')
print(dfp[filt])
print(dfp.loc[filt])

filt2 = (dfp['last'] == 'golla') | ( dfp['first']  == 'dileep')
print(dfp[filt2])
filt2 = (dfp['last'] == 'golla') & ( dfp['first']  == 'dileep')

print(dfp[filt2])
filt2 = (dfp['last'] == 'golla') & ( dfp['first']  == 'dileep')

dfp[~filt2]

filt2 = (dfp['last'] == 'golla') | ( dfp['first']  == 'dileep')

dfp[~filt2]

df.head()


filt3= (df['Age']=='18-24 years old')

df.loc[filt3,'Country']


filt3= (df['Age']=='18-24 years old') & (df['Gender']=="Man")

df.loc[filt3, ['Age','Country','Gender','Trans'] ]

countries=['Finland','India','Pakistan','Bangladesh']

filt=df['Country'].isin(countries)

df.loc[filt,'Country']
filt=df['PlatformWorkedWith'].str.contains('Python', na=False)

print(filt)


df.loc[filt, 'PlatformWorkedWith']

print(dfp)


# # Updating Columns

dfp.columns=['first name','last name','age','place']


print(dfp)


dfp.columns=[x.upper() for x in dfp.columns]

print(dfp)
dfp.columns=dfp.columns.str.replace(' ','_')

print(dfp)
dfp.columns=dfp.columns.str.lower()  #dfp.columns=[x.lower() for x in dfp.columns]
print(dfp)
dfp.rename(columns={'first_name':'first','last_name':'last'}, inplace=True)

print(dfp)


# Updating rows:


dfp.loc[2]=['kitti','golla',22,'aregudem']

print(dfp)

dfp.loc[2,['first','age']]=['pandu',10]

print(dfp)

dfp.loc[0,'first']='varun'


print(dfp)


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




