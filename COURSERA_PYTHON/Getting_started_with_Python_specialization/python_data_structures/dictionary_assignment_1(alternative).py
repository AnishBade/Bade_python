'''9.4 Write a program to read through the mbox-short.txt and figure out who has
sent the greatest number of mail messages. The program looks for 'From ' lines and
    takes the second word of those lines as the person who sent the mail. The program
    creates a Python dictionary that maps the sender's mail address to a count of the numbe' \
 of times they appear in the file. After ' \'the dictionary is produced, ' \
'the program reads through the dictionary using a maximum loop '  'to find the most prolific committer.
'''
file_name=input("Enter a file name:")
if len(file_name)<1: file_name="mbox-short.txt"
file=open(file_name)
counts=dict()
list=[]
final_list=[]
for lines in file:
    if lines.startswith('From '):
        lines=lines.rstrip()
        words=lines.split()
        counts[words[1]]=counts.get(words[1],0)+1
for name,count in counts.items():
    newtuple=(count,name)
    list.append((newtuple))
list=sorted(list,reverse=True)
for v,k in list:
     final_list.append((k,v))
for i in range(10):
    print(final_list[i])

most_email_sender=final_list[0][0]
most_count=final_list[0][1]
print("The highest number of email is sent by %s,i.e %s times"%(most_email_sender,most_count))


