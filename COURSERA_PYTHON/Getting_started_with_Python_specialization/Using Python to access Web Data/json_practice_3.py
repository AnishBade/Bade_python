import json
data='''{
    "name": "jane doe",
    "salary": 9000,
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "JaneDoe@pynative.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}'''
print(data)
print(type(data))
parsed=json.loads(data)
print(parsed)
print(type(parsed))

dumped=json.dumps(parsed,sort_keys=True)
print(dumped)
print(type(dumped))
print(json.loads(dumped))
print(type(json.loads(dumped)))
parsed_again=json.loads(dumped)
print(parsed_again)