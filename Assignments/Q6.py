#6.1
s="aeiouhjkl"
vowels="aeiouAEIOU"
vowels_count=0
for char in s:
    if char in vowels:
        vowels_count+=1
print("The number of vowels in the string are:",vowels_count)


#6.2
str="harsh"
reverse_str=str[::-1]
print("The reversed string is:",reverse_str)


#6.3
pal_string=input("Enter the string:")
if pal_string==pal_string[::-1]:
    print("The string is palindrome")
else:
    print("The string is not palindrome")