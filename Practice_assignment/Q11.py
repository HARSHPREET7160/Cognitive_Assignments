#11.1
import math

number = float(input("Enter a number: "))
sqrt_value = math.sqrt(number)
print(f"The square root of {number} is {sqrt_value}.")


#11.2
import datetime

current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)


#11.3
import os

files = os.listdir('.')
print("Files in the current directory:")
for file in files:
    print(file)
