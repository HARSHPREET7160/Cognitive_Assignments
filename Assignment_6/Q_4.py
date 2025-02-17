import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url='https://raw.githubusercontent.com/AnjulaMehto/MCA/main/company_sales_data.csv'
data=pd.read_csv(url)
data.columns=data.columns.str.strip()

plt.figure(figsize=(10,6))
sns.lineplot(x=data['month_number'],y=data['total_profit'],marker='o')
plt.title('Total Profit of All Months')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

plt.figure(figsize=(10,6))
for column in ['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']:
    sns.lineplot(x=data['month_number'],y=data[column],label=column)
plt.title('Product Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.xticks(data['month_number'],rotation=45)
plt.legend(title='Products')
plt.grid(True)
plt.show()

data.set_index('month_number').plot(kind='bar',figsize=(12,8))
plt.title('Bar Chart for All Features')
plt.ylabel('Values')
plt.xlabel('Month Number')
plt.xticks(rotation=0)
plt.legend(title='Features')
plt.grid(axis='y')
plt.show()
