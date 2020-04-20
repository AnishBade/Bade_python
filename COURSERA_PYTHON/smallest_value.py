#  current_smallest_value=100000000000
#for num in [10,20,3000,40,3000,355,3444,5,3,444,55,66,2,1]:
 #   if num<current_smallest_value:
  #      current_smallest_value=num
#      print(num,current_smallest_value)
# print("THE SMALLEST VALUE IS:",current_smallest_value)

smallest_so_far = None
for num in [10,20,3000,40,3000,355,3444,5,3,444,55,66,2,1]:
    if smallest_so_far is None:    #None is a FLAG VALUE
        smallest_so_far=num
    elif num<smallest_so_far:
        smallest_so_far=num
    print(num,smallest_so_far)
print("smallest number is:",smallest_so_far)