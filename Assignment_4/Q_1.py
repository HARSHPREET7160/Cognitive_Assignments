import numpy as np

array=np.array([1,2,3,4,5])
#(a)
array+=2
print(f"Array after adding 2 to each element is {array}")
print("\n")

#(b)
array*=3
print(f"Array after multiplying 3 to each element is {array}")
print("\n")

#(c)
array=array.astype(float)
array/=2
print(f"Array after dividing 2 to each element is {array}")
print("\n")
