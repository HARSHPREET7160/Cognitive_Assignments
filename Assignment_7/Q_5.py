def swap_set_elements(s, elem1, elem2):
    lst = list(s)
    if elem1 in lst and elem2 in lst:
        i, j = lst.index(elem1), lst.index(elem2)
        lst[i], lst[j] = lst[j], lst[i] 
    return set(lst)


my_set = {10, 20, 30, 40, 50}
swapped_set = swap_set_elements(my_set, 20, 40)
print("Set after swapping:", swapped_set)
