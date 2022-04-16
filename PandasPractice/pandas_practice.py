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
print(dfp[['first','age']]) #for selecting the age and first columns
print(type(dfp[['first','age']]))
print(df.columns) #all columns in dataframe will be printed
print(dfp.columns)
print(dfp.iloc[0])#for slecting the first row of Dataframe
print(df.iloc[0])
print(dfp.iloc[[0,1,2]])
print(dfp.iloc[[0,1],[1,0]])
print(dfp.loc[[0,1],['first','age']])
print(dfp.iloc[0:2,0:2])
print(dfp['age'].value_counts()) #to print value counts of particular age
print(df['Country'].value_counts()) #to print value counts of columns
print(dfp.loc[0,'age'])
print(dfp.loc[:,"first":'age'])
print(dfp.iloc[:,0:2])
print(dfp.loc[0:2,'first'])

dfp.set_index('first') #to set index
print(dfp)
dfp.set_index('first',inplace=True) #inplace used to reflect change in dataframe if provided falses it creates new dataframe 
print(dfp)
print(dfp.index)
print(dfp.loc['dileep'])
print(dfp.loc['dileep','age']) #loc used to acess based on name of columns where iloc used while sleecting with index value

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
print(dfp.describe()) #uesd to disply all the information about dataframe
filt = (dfp['last']=='golla')
print(dfp[filt])
print(dfp.loc[filt])

filt2 = (dfp['last'] == 'golla') | ( dfp['first']  == 'dileep')
print(dfp[filt2])
filt2 = (dfp['last'] == 'golla') & ( dfp['first']  == 'dileep')

print(dfp[filt2])
filt2 = (dfp['last'] == 'golla') & ( dfp['first']  == 'dileep')
dfp[~filt2] #~ works as a not operator

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
filt=df['PlatformWorkedWith'].str.contains('Python', na=False) #checks for the string containing the string "Python"
print(filt)
df.loc[filt, 'PlatformWorkedWith'] #selects the table based on the filtered condition and gives the only one column as provdided
print(dfp)


# # Updating Columns
dfp.columns=['first name','last name','age','place']
print(dfp)


dfp.columns=[x.upper() for x in dfp.columns] #list comprehension on dataframe
print(dfp)
dfp.columns=dfp.columns.str.replace(' ','_') #to replace a particular element
print(dfp)

dfp.columns=dfp.columns.str.lower()  #dfp.columns=[x.lower() for x in dfp.columns] to convert into lower case
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

dfp.at[2,'first']='Uday Kiran'
print(dfp)


filt=dfp['place']=='kodad' #checks for the elememt in column with value "kodad
dfp[filt]['first']='abhi'
dfp.loc[filt,'first']='abhi'
print(dfp)

dfp['first'].str.upper()
dfp['first']=dfp['first'].str.upper()
print(dfp)

dfp['first'].apply(len) #to apply length function

def lowerCase(first):
    return first.lower()

dfp['first'].apply(lowerCase)
dfp['first']=dfp['first'].apply(lowerCase)
print(dfp)

dfp['first']=dfp['first'].apply(lambda i:i.upper())
print(dfp)

dfp.apply(len)  # here if we apply on whole dataframe then we get length of number of rows.
print(len(dfp['first']))

dfp.apply(len ,axis='columns')  # here if we apply on whole dataframe then we get length of number of columns.
print(dfp)

dfp.apply(pd.Series.min)
print(pd.Series.min)

dfp.rename(columns={'age':'study'}, inplace=True)
print(dfp)

dfp.rename(columns={'study':'age'}, inplace=True)
print(dfp)

persons={
    'first':['dileep','arjun','vikas','krishna'],
    'last':['golla','boddu','vatte','golla'],
     'study':['Btech','Degree','Tenth',"Inter"],
     'place':['suryapet','hyderabad','kodad','suryapet']
}
dfp1=pd.DataFrame(persons)
print(dfp1)
print(dfp1.applymap(len)) # len cannot apply to integers
dfp1=dfp1.applymap(str.upper)
print(dfp1)

dfp1['first'].map({'VIKAS':'Allu',"ARJUN":"RAM"})
dfp1['first']=dfp1['first'].replace({'VIKAS':'Allu',"ARJUN":"RAM"})
print(dfp1)

df['SOAccount'].map({'Yes':True,'No':False})

dfp1['first']+' '+dfp1['last']
dfp1['Name']=dfp1['first']+' '+dfp1['last']
print(dfp1)

dfp1.drop(columns=['first','last'],inplace=True)
print(dfp1)

dfp1[['first','last']]=dfp1['Name'].str.split(' ',expand=True)
print(dfp1)

dfp1=dfp1.append({'first':'Mark'},ignore_index=True)
print(dfp1)

persons={
    'first':['Ntr','RC'],
    'last':['nandy','koni'],
     'study':['mpc','bipc'],
     'place':['hyderabad','filmcity']
}

dfp2=pd.DataFrame(persons) #create dataframe
dfp1.append(dfp2,ignore_index=True) #sort=false sets sort error to false
dfp1=dfp1.append(dfp2,ignore_index=True) 
print(dfp1)
dfp1.drop(index=6)

dfp1=dfp1.drop(index=dfp1[dfp1['last']=='VATTE'].index)
print(dfp1)

cgroup=df.groupby('Country')
print(cgroup)
print(cgroup.get_group("India"))

print(cgroup['SocialMedia'].value_counts())
cgroup['ConvertedComp'].median().loc['Germany']
cgroup['ConvertedComp'].agg(['median','mean']).loc['Germany']

filt=df['Country']=='India'
df.loc[filt]["LanguageWorkedWith"].str.contains('Python').sum()
#cgroup["LanguageWorkedWith"].str.contains('Python').sum()


cgroup["LanguageWorkedWith"].apply(lambda x:x.str.contains('Python').sum()) #applied lamnda function
crespondent=df['Country'].value_counts()
print(crespondent)
Cusespython=cgroup["LanguageWorkedWith"].apply(lambda x:x.str.contains('Python').sum())
print(Cusespython)

p_df=pd.concat([crespondent,Cusespython], axis='columns', sort=False)
p_df

p_df.rename(columns={"Country":"NumRespondents","LanguageWorkedWith":"Nknowspython"}, inplace=True)
p_df['perKnowsPython'] = (p_df["Nknowspython"] / p_df['NumRespondents']) * 100
print(p_df)

p_df.sort_values(by="perKnowsPython" ,ascending=False, inplace=True)
p_df.head(50)
print(p_df.loc['Japan'])


# Cleaning  data
print(dfp1)
dfp0=pd.DataFrame({'study':['NaN',None,'NA'],'place':['NaN','NaN',"Missing"],'Name':['NaN','vijay','NA'],'first':['NaN','NaN','NA'],'last':[None,'NaN','NA'] })
dfp1=dfp1.append(dfp0,ignore_index=True)
print(dfp1)

dfp1.dropna()
(dfp1.dropna(axis='index',how='all')
dfp1.dropna(axis='index',how='any')
dfp1.dropna(axis='columns',how='any')
dfp1.dropna(axis='columns',how='all')
dfp1.dropna(axis='index',how='all',subset=['Name','first'])
dfp1.replace('NA',np.nan,inplace=True)
dfp1.replace('Missing',np.nan,inplace=True)
dfp1.replace('NaN',np.nan,inplace=True)
print(dfp1)
dfp1.dropna()
dfp1.dropna(axis='index',how='any')
dfp1.isna()
dfp1.fillna('Missing')
print(dfp)

dfp0=pd.DataFrame({'first':['NaN',None,'NA'],'last':['NaN','NaN',"Missing"],'age':[np.nan,10,'NA'],'place':[np.nan,None,'NA']})

dfp=dfp.append(dfp0, ignore_index=True)
print(dfp)

#Taking care of missing values
dfp.replace('NA',np.nan,inplace=True)
dfp.replace("NaN",np.nan,inplace=True)
dfp.replace("Missing",np.nan,inplace=True)
print(dfp.fillna(0)) #fills empty value with 0

print(dfp.dtypes)
print(dfp['age'].mean()) #mean for age column
print(dfp['age'])
print(dfp['age'].mean())
dfp['age']=dfp['age'].astype(float)
print(dfp['age'])

print(dfp['age'].mean())
print(type(dfp['age']))

sdf=pd.Series([10,20,30,40])
print(sdf)

df['YearsCode'].head()
print(df['YearsCode'].unique())

df['YearsCode'].replace('Less than 1 year',0 ,inplace=True)
df['YearsCode'].replace('More than 50 years',51 ,inplace=True)
df['YearsCode']=df['YearsCode'].astype(float)
print(df['YearsCode'].mean())
print(df['YearsCode'].median())
