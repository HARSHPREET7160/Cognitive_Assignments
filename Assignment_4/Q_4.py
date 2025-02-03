import numpy as np

harshpreet=np.linspace(10,100,25)
print("Evenly spaced 25 numbers between 10 and 100 are:")
print(harshpreet)
print("\n")

print(f"Dimension of the array is {harshpreet.ndim}\n")

print(f"Shape of the array is {harshpreet.shape}\n")

print(f"Total elements of the array is {harshpreet.size}\n")

print(f"data type of each elements is {harshpreet.dtype}\n")

print(f"Total number of bytes consumed by the elements of the array is {harshpreet.nbytes}\n")

# print("Transpose using reshape()\n")
# print(harshpreet.reshape(25,25))

print("Transpose using .T\n")
print(harshpreet.T)



