import pandas as pd

df_csv=pd.read_csv('LossFromNetCrime.csv')
print(df_csv.head())

print("CSV file after deleting row 4 and column 3")
df_csv.drop(4,axis=0,inplace=True)
df_csv.drop(df_csv.columns[3],axis=1,inplace=True)
print(df_csv.head())
