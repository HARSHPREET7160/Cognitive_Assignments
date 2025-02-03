import numpy as np

ucs420_harshpreet=np.array([[10,20,30,40],[50,60,70,80],[90,15,20,35]])
print("Array is")
print(ucs420_harshpreet)
print("\n")

print(f"mean of the array is {np.mean(ucs420_harshpreet)}\n")

print(f"median of the array is {np.median(ucs420_harshpreet)}\n")

print(f"Max of the array is {np.max(ucs420_harshpreet)}\n")

print(f"Min of the array is {np.min(ucs420_harshpreet)}\n")

print(f"Unique elements in the array are {np.unique(ucs420_harshpreet)}\n")

reshaped_ucs420_harshpreet=ucs420_harshpreet.reshape(4,3)
print("Array after reshaping is to four rows and three columns")
print(reshaped_ucs420_harshpreet)
print("\n")

resized_ucs420_harshpreet=np.resize(ucs420_harshpreet,(2,3))
print("Array after resizing is to two rows and three columns")
print(resized_ucs420_harshpreet)
