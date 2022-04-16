
#import libraries
import pandas as pd
import numpy as np
from datetime import datetime


d_parser = lambda x: datetime.strptime(x, '%Y-%m-%d')
 # we can aslo add here to parse date df=pd.read_csv("/content/1inch.csv",parse-dates=df['Date'],date_parser=dateParser)
df = pd.read_csv('1inch.csv' ,parse_dates=['Date'], date_parser=d_parser)
print(df.head())
print(df.shape)
df.loc[0,"Date"]  # if it show error do dateformatting pd.t0_datetime(df['Date', format='%Y-%m-%d %I-%p'])
print(df.loc[0,"Date"].day_name())
df['Date']=pd.to_datetime(df['Date'])

print(df['Date'].dt.day_name())
df['DayofWeek']=df['Date'].dt.day_name()
print(df)
print(df['Date'].min())
print(df['Date'].max())

filt = (df['Date'] >= pd.to_datetime('2020-01-01')) & (df['Date'] < pd.to_datetime('2022-01-01'))
print(df.loc[filt])


df.set_index('Date', inplace=True)
print(df.head())
print(df['2022'])
print(df['2021-06':'2022-04'])
print(df['2021-06':'2022-04']['Close'].mean())
print(df['2022-01']['High'].max())
high=df['High'].resample("D").max()
print(high["2020-12-25"])



print(df.resample("w").mean())

df.resample('W').agg({'Close': 'mean', 'High': 'max', 'Low': 'min', 'Volume': 'sum'})

print(np.asarray(df["Open"]))
