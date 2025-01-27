import pandas as pd

dataset={
    "Tid":[1,2,3,4,5,6,7,8,9,10],
    "Refund":["Yes","No","No","Yes","No","No","Yes","No","No","No"],
    "MaritialStatus":["single","married","single","married","divorced","married","divorced","single","married","single"],
    "TaxableIncome":["125K","100K","70K","120K","95K","60K","220K","85K","75K","90K"],
    "Cheat":["No","No","No","No","Yes","No","No","Yes","No","Yes"]
}

df=pd.DataFrame(dataset)
print(df)

#(1)
print("\n")
print("----------Rows from index 3 to 7-----------")
print(df.iloc[3:8])

#(2)
print("\n")
print("----------Rows from index 4 to 8 and Column 2 to 4-----------")
print(df.iloc[4:9,2:5])

#(3)
print("\n")
print("----------All rows with column index 1 to 3 (include 3)-----------")
print(df.iloc[:,1:4])