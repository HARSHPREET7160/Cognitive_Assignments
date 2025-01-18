# (i)
scores=(45,89.5,76,45.4,89,92,58,45)
print(f"Highest score is:{max(scores)}")
print("\n")

# (ii)
print(f"Lowest score is:{min(scores)}")
print("\n")


# (iii)
reversed_score = list(scores[::-1])
print(f"Reversed List of Scores is:{reversed_score}")
print("\n")

# (iv)
checker=int(input("Enter the score to check:"))
if checker in scores:
    print(f"{checker} is present in the list at index {scores.index(checker)}")
else:
    print(f"{checker} is not present in the list")