import numpy as np

#(a)
arr=np.array([1,2,3,4,5])
reversed_arr=arr[::-1]
print(f"Array after reversing is {reversed_arr}")

#(b)

#(i)
x=np.array([1,2,3,4,5,1,2,1,1,1])
print(f"Most frequent item in the array is {np.argmax(np.bincount(x))} and indices is {np.where(x==np.argmax(np.bincount(x)))}\n")

#(ii)
y=np.array([1,1,1,2,3,4,2,4,3,3])
print(f"Most frequent item in the array is {np.argmax(np.bincount(y))} and indices is {np.where(y==np.argmax(np.bincount(y)))}\n")


