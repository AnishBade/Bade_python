'''Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers. You will extract
all the numbers in the file and compute the sum of the numbers.
'''
import re
total=0
num_list=[]
file_name=input("Enter a file name: ")
file=open(file_name)
for lines in file:
    list=re.findall('\d+',lines)

    if list != []:
        for i in range(len(list)):
            num_list.append(list[i])
for i in range(len(num_list)):
    total+=int(num_list[i])

print("Total=",total)