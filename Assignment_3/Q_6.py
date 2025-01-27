import pandas as pd
dataset={
    "Employee_ID":[101,102,103,104,105],
    "Name":["Alice","Bob","Charlie","Diana","Edward"],
    "Department":["HR","IT","IT","Marketing","Sales"],
    "Age":[29,34,41,28,38],
    "Salary":[50000,70000,65000,55000,60000],
    "Years_of_Experience":[4,8,10,3,12],
    "Joining_Date":["2020-03-15","2017-07-19","2013-06-01","2021-02-10","2010-11-25"],
    "Gender":["Female","Male","Male","Female","Male"],
    "Bonus":[5000,7000,6000,4500,5000],
    "Rating":[4.5,4.0,3.8,4.7,3.5]
}
df=pd.DataFrame(dataset)

csv_file = 'employees.csv'
df.to_csv(csv_file, index=False)

df_csv=pd.read_csv('employees.csv')
print(df_csv)
print("\n")

#(a)
print("Shape of the data frame",df.shape)

#(b)
print("Data Information:")
print(df.info())

#(c)
print("Descriptive Statistics")
print(df.describe())

#(d)
print("----------First 5 rows----------")
print(df.iloc[0:])
print("\n")
print("----------last 3 rows----------")
print(df.tail(3))
print("\n")

#(e)
print("Average salary of employees:",df["Salary"].mean())
print("Total Bonus:",df["Bonus"].sum())
print("Youngest Employee Age:",df["Age"].min())
print("Highest Rating:",df["Rating"].max())

#(f)
print("---------------Sorted salary column in decending order---------------")
sorted_df=df.sort_values(by="Salary", ascending=False)
print(sorted_df["Salary"])
print("\n")

#(g)
df["Performance"] = pd.cut(
df["Rating"],bins=[0, 4.0, 4.5, 5],labels=["Average", "Good", "Excellent"]
)
print(df[["Name", "Performance"]])
print("\n")

#(h)
print("Missing values")
print(df.isnull().sum())
print("\n")

#(i)
print("Renaming Employee_ID to ID")
df.rename(columns={"Employee_ID":"ID"},inplace=True)
print(df)
print("\n")

#(j)
print("Employees have more than 5 years of experience\n")
Data_required=df[(df["Years_of_Experience"]>5)]
print(Data_required)
print("\n")

print("Employees belong to IT department\n")
Data_required=df[(df["Department"]=="IT")]
print(Data_required)
print("\n")

#(k)
print("Adding a new colum Tax")
df["Tax"] = df["Salary"] * 0.1
print(df)

#(i)
df.to_csv('new_employees.csv',index=False)