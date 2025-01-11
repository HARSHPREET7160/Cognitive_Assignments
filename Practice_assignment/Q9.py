#9.1
import random
print("5 random numbers between 1 and 100:")
for _ in range(5):
    print(random.randint(1, 100))

#9.2
import random
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = random.randint(1, 100)
print(f"Generated number: {num}")
print(f"{num} is {'a prime' if is_prime(num) else 'not a prime'} number.")

#9.3
import random
def roll_die():
    return random.randint(1, 6)

print(f"You rolled a {roll_die()}.")


#9.4
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", numbers)
random.shuffle(numbers)
print("Shuffled list:", numbers)


#9.5
import random

items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("Original list:", items)
selected_item = random.choice(items)
print("Randomly selected item:", selected_item)


#9.6
import random
import string

def generate_password(length):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

length = int(input("Enter the desired password length: "))
print("Generated password:", generate_password(length))


#9.7
import random

def pick_random_card():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    card = f"{random.choice(ranks)} of {random.choice(suits)}"
    return card

print("Randomly picked card:", pick_random_card())
