import json

#print(type(data))
#print(data)

#parsed = json.loads(data)
#print(type(parsed))
#print(parsed)

#dumped=json.dumps(data,sort_keys=True)
#print(type(dumped))
#print(dumped)

#print(type(data))
#print(data)

#file_parsed=json.load(sample1.txt)
#print(file_parsed)
with open("sample1.json","r") as f:
    file_parsed = json.load(f)
    print("Decoded JSON Data From File")
    for key, value in file_parsed.items():
        print(key, ":", value)
    print("Done reading json file")
