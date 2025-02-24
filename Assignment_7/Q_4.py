def swap_elements(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


my_list = [1, 2, 3, 4, 5]
swap_elements(my_list, 1, 3)
print("List after swapping:", my_list)
