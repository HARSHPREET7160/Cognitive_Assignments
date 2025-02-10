import numpy as np

array=np.array([10,52,62,16,16,54,453])

#(i)
print("Sorted array")
print(np.sort(array))

#(ii)
print("Indices of sorted array")
print(np.argsort(array))

#(iii)
print("4 smallest elements")
print(np.sort(array)[:4])

#(iv)
print("5 largest elements")
print(np.sort(array)[-5:])
print("\n")



#(b)
array=np.array([1.0,1.2,2.2,2.0,3.0,2.0])

print("Integer elements only")
integer_elements=array[array==np.floor(array)]
print(integer_elements)
print("\n")

print("Floating point elements only")
floating_elements=array[array!=np.floor(array)]
print(floating_elements)