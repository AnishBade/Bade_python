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
parsed=json.loads(data)
print(parsed)

dumped=json.dumps(parsed,sort_keys=True)
print(json.loads(dumped))

parsed_again=json.loads(dumped)
print(parsed_again)