'''10.2 Write a program to read through the mbox-short.txt and figure out the distribution
by hour of the day for each of the messages. You can pull the hour out from the 'From ' line
by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 Once you have accumulated the
ounts for each hour, print out the counts, sorted by hour as shown below.
'''
file_name=input("Enter the file name: ")
file=open(file_name)
init_dictionary=dict()
first_list=[]
for line in file:
    line=line.rstrip()
    if line.startswith("From "):
        first_split=line.split(':')
        second=first_split[0]
        hour=second[-2:]
        init_dictionary[hour]=init_dictionary.get(hour,0)+1
for k,v in init_dictionary.items():
    first_list.append((k,v))
first_list=sorted(first_list)
print(first_list)
for k,v in first_list:
    print(k,v)


