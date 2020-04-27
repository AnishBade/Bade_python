'''
current_largest_value = -1
for num in [1,4,54,53,75,567,9087,666,56,3888,77]:
    if num>current_largest_value:
        current_largest_value = num
    print(current_largest_value,num)
print("the larrgest value is: ",current_largest_value)
'''

# None is a FLAG VALUE
largest_so_far=None
for num in [1,4,54,53,75,567,9087,666,56,3888,77]:
    if largest_so_far is None:
        largest_so_far=num
    elif num>largest_so_far:
        largest_so_far=num
    print(num,largest_so_far)
print("largest number is:",largest_so_far)