print("Enter a line: ")
line=input("")
words=line.split()
counts=dict()
for word in words:
    counts[word]=counts.get(word,0)+1
print(words)
print(counts)
