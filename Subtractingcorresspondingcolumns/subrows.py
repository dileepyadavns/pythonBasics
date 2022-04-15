
import pandas as pd


df=pd.read_excel("multi_threading_activity.xlsx")


print(df)

df.value_counts()


df["B"]=pd.to_numeric(df["B"], errors="coerce")


df["A"]=pd.to_numeric(df["A"], errors="coerce")



df.replace("NaN",0)

df['sub']=df['A']-df['B']

print(df)


dict={ "A":[1,2,3,5,6],"B":[10,20,30,40,50],"C":[400,400,500,600,300]}


df2=pd.DataFrame(dict)
print(df2)

df2['sum2']=df2['A']+df2['B']+df2['C']

print(df2)

df.values.tolist()
persons={
    'first':['dileep','arjun','vikas','krishna'],
    'last':['golla','boddu','vatte','golla'],
     'study':['Btech','Degree','Tenth',"Inter"],
     'place':['suryapet','hyderabad','kodad','suryapet']
}

df1=pd.DataFrame(persons)

