#7.1 Write a program that prompts for a file name, then opens that
#file and reads through the file, and print the contents of the file in upper
#case. Use the file words.txt to produce the output below.
file_name=input("enter a file name:")
file=open(file_name)
for files in file:
    files=files.upper().rstrip()
    print(files)