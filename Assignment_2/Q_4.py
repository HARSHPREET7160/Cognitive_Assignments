A={34,56,78,90}
B={78,45,90,23}


# (i)
print("Union of set A and B is:",A.union(B))
print("\n")


# (ii)
print("Intersection of set A and B is:",A.intersection(B))
print("\n")

# (iii)
print("Symmetric Difference of set A and B is:",A.symmetric_difference(B))
print("\n")

# (iv)
print("Is A is a subset of B:",A.issubset(B))
print("\n")
print("Is B is a superset of A:",B.issuperset(A))
print("\n")


# (v)
X=int(input("Enter the score to be remove:"))
if X in A:
    A.remove(X)
    print("Score removed successfully")
else:
    print("Score not found in the set")
     

