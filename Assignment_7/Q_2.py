import numpy as np

array = np.array([[1, -2, 3], [-4, 5, -6]])

# i. Element-wise absolute value
absolute_values = np.abs(array)

# ii. Percentiles
flattened_25th = np.percentile(array, 25)
flattened_50th = np.percentile(array, 50)
flattened_75th = np.percentile(array, 75)

column_25th = np.percentile(array, 25, axis=0)
column_50th = np.percentile(array, 50, axis=0)
column_75th = np.percentile(array, 75, axis=0)

row_25th = np.percentile(array, 25, axis=1)
row_50th = np.percentile(array, 50, axis=1)
row_75th = np.percentile(array, 75, axis=1)

# iii. Mean, Median, and Standard Deviation
flattened_mean = np.mean(array)
flattened_median = np.median(array)
flattened_std = np.std(array)

column_mean = np.mean(array, axis=0)
column_median = np.median(array, axis=0)
column_std = np.std(array, axis=0)

row_mean = np.mean(array, axis=1)
row_median = np.median(array, axis=1)
row_std = np.std(array, axis=1)

# Printing the results
print("Element-wise Absolute Values:\n", absolute_values)
print("\nFlattened Percentiles - 25th:", flattened_25th, ", 50th:", flattened_50th, ", 75th:", flattened_75th)
print("Column Percentiles:\n 25th:", column_25th, "\n 50th:", column_50th, "\n 75th:", column_75th)
print("Row Percentiles:\n 25th:", row_25th, "\n 50th:", row_50th, "\n 75th:", row_75th)

print("\nFlattened Mean:", flattened_mean, ", Median:", flattened_median, ", Std Dev:", flattened_std)
print("Column-wise Mean:", column_mean, ", Median:", column_median, ", Std Dev:", column_std)
print("Row-wise Mean:", row_mean, ", Median:", row_median, ", Std Dev:", row_std)
