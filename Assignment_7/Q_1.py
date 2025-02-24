import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Part I: Randomized Sales Data Generation


roll_number = 102317160
np.random.seed(roll_number)


sales_data = np.random.randint(1000, 5001, size=(12, 4))

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
categories = ["Electronics", "Clothing", "Home & Kitchen", "Sports"]
df = pd.DataFrame(sales_data, columns=categories, index=months)



# Part II: Data Manipulation and Analysis

print(df.head())
print(df.describe())

total_sales_per_category = df.sum()
total_sales_per_month = df.sum(axis=1)
df["Total Sales"] = total_sales_per_month

growth_rate = df.pct_change().mean() * 100
print(growth_rate)
df["Growth Rate"] = df["Total Sales"].pct_change() * 100

if roll_number % 2 == 0:
    df["Electronics"] *= 0.9
else:
    df["Clothing"] *= 0.85
    


# Part III: Visualizations

plt.figure(figsize=(10, 5))
for category in categories:
    plt.plot(df.index, df[category], marker='o', label=category)
plt.title("Monthly Sales Trends")
plt.xlabel("Month")
plt.ylabel("Sales Units")
plt.legend()
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 5))
sns.boxplot(data=df[categories])
plt.title("Sales Distribution by Category")
plt.xlabel("Product Category")
plt.ylabel("Sales Units")
plt.show()
