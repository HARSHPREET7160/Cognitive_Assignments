import random
from sympy import isprime

List_random = [random.randint(100,900) for _ in range(100)]
print("List of randon numners(100,900:")
print(List_random)
print("\n")


# (i)
list_odd_num=[num for num in List_random if num%2!=0]
print("List of Odd Numbers:")
print(list_odd_num)
print("\n")

# (ii)
list_even_num=[num for num in List_random if num%2==0]
print("List of Even Numbers:")
print(list_even_num)
print("\n")

# (iii)
list_prime_num=[num for num in List_random if isprime(num)]
print("List of Prime Numbers:")
print(list_prime_num)
print("\n")