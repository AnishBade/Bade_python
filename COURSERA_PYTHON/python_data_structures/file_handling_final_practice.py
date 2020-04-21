#7.2 Write a program that prompts for a file name, then opens that file and
#reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from
#each of the lines and compute the average of those values and produce an
#output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
file_name=input("Enter the file name:")
file=open(file_name)
num_lines=0

total=0
for files in file:
    if ('X-DSPAM-Confidence:') in files:
        num_lines+=1
        finds=files.find(":")
        value=float(files[finds+1:].strip())
        total+=value
average=total/num_lines
print(average)