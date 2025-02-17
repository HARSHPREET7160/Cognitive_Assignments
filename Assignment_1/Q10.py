#10.1
import sys

if len(sys.argv) != 3:
    print("Please provide exactly two numbers as arguments.")
else:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.") # python Q10.py 5 10

#10.2
import sys

if len(sys.argv) != 2:
    print("Please provide exactly one string as an argument.")
else:
    input_string = sys.argv[1]
    print(f"The length of the string is {len(input_string)}.") # python Q10.py "harsh"