import json
#json.dumps() function converts a Python object into a json string.
#Using the json.load() and json.loads() method, you can turn JSON encoded/formatted data into
# Python Types this process is known as JSON decoding. P

data = '''{
    "name":"anish",
    "cars":["ferrari","volkswaegen","bmw"],
    "phones": ["iphone 8","iphone 9","iphone 10"]
}'''
with open("sample1.txt","r") as nth:
    parsed=json.load(nth)
    print(parsed)

dumped=json.dumps(parsed,sort_keys=True)
print(dumped)

parsed_again=json.loads(dumped)
print(parsed_again)