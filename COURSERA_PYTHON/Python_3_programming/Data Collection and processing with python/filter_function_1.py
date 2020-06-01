def evens(lst):
    new_list=filter(lambda value:value%2==0,lst)
    return list(new_list)
print(evens([2,4,5,7,8]))