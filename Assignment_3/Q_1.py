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