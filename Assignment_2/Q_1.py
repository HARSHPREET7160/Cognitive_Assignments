# (i)
L=[10,20,30,40,50,60,70,80]
print("list after adding 200 and 300")
L.extend([200,300])
print(L)
print("\n\n")


# (ii)
print("list after removing 10 and 30")
L.remove(10)
L.remove(30)
print(L)
print("\n\n")



# (iii)
L.sort()
print(f"Sorted List in Ascending order is:{L}")
print("\n\n")

# (iv)
L.sort(reverse=True)
print(f"Sorted List in Decending order is:{L}")
print("\n\n")
