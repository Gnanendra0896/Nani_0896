import requests
import jsonpath
import json

url = 'https://reqres.in/api/users'

file = open('C:\\Users\\Gnanendra\\Desktop\\creatingUser.json','r')
json_input = file.read()
request_json = json.loads(json_input)
#print(request_json)
response = requests.post(url,request_json)
print(response.content)
assert response.status_code == 201
print(response.headers)
# parse response to json format
response_json = json.loads(response.text)
#fetching name Json path
name = jsonpath.jsonpath(response_json,'job')
print(name[0])
# validating the job
#assert name[1] == 'lead engineer'
assert name[0] == 'leader'
