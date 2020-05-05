list1=[]
list2=[]
lowest=None
second_lowest=None
for i in range(int(input("Enter number of students:"))):
    name = input("Enter the name of student:")
    score = float(input("Enter the score of {}".format(name)))
    list1.append(name)
    list1.append(score)
    list2.append(list1)
for outer_list in list1:
    for inner_list in outer_list:
         if lowest is not None:
                lowest=inner_list[-1]
         elif int(inner_list[-1])<int(lowest):
                lowest=inner_list[-1]

for outer_list in list1:
    for inner_list in outer_list:
        if second_lowest is not None:
            second_lowest = inner_list[-1]
        elif int(second_lowest)<int(inner_list[-1]) < int(lowest):
            second_lowest = inner_list[-1]
print(second_lowest)
