import numpy as np

#(a)

first_intial='H'
last_intial='P'
X=ord(first_intial)+ord(last_intial)

sales_array=np.array([X,X+50,X+100,X+150,X+200],dtype=float)
print(f"Required dataset is {sales_array}\n")

#(b)
tax_rate=((X%5)+5)/100
sales_after_tax = sales_array*(1 -tax_rate)
print(f"Sales after tax is {sales_after_tax}\n")
print("\n")

#(c)
discount_sales_array=np.copy(sales_array)
discount_sales_array[sales_array<X+100] *= 0.95
discount_sales_array[sales_array>=X+100] *= 0.90
print(f"discounted array is {discount_sales_array}")
print("\n")

#(d)
week_multipliers = 1 + np.arange(3).reshape(3, 1) * 0.02
sales_array = sales_array*week_multipliers
print(sales_array)
