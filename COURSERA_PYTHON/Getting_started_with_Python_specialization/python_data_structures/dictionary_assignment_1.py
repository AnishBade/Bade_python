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
most_email_sender=None
most_count=None
for lines in file:
    if lines.startswith('From '):
        lines=lines.rstrip()
        words=lines.split()
        counts[words[1]]=counts.get(words[1],0)+1
        for sender,count in counts.items():
            if most_count is None:
                most_email_sender=sender
                most_count=count
            elif count>most_count:
                most_count=count
                most_email_sender=sender
print("Most email sender: ",most_email_sender)
print("Number of times email sent by {}: ".format(most_email_sender),most_count)
