#5.1
l=[10,-2,0,20,4]
print("The list is:",l)
print("The maximum number in the list is:",max(l))
print("The minimum number in the list is:",min(l))


#5.2
dict={
    "Name":"Harshpreet",
    "Age":20,
    "Roll no":102317160
}
print(dict["Roll no"])

#5.3
list=[10,32,0,-2,4,5,0]
print("The list is(before sorting):",list)
list.sort()
print("The sorted list is(in ascending order):",list)
list.sort(reverse=True)
print("The sorted list is(in descending order):",list)


#5.4
dict1={
    "Name":"Harshpreet",
    "Age":20
}
dict2={
    "Roll no":102317160,
    "Branch":"CSE"
}
dict1.update(dict2)
print("The updated dictionary is:",dict1)