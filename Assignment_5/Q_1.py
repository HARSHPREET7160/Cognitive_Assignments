import numpy as np

gfg=np.matrix([[4,1,9],[12,3,1],[4,5,6]])

#(i)
print(f"sum of all elements of matrix is {np.sum(gfg)}\n")

#(ii)
print(f"sum of all elements row wise is")
print(np.sum(gfg,axis=1))
print("\n")

#(ii)
print(f"sum of all elements column wise is")
print(np.sum(gfg,axis=0))
