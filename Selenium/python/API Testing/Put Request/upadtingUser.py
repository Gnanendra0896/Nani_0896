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

#parse response to json
json_response = json.loads(response.text)

# fetching the updating data
updating_list = jsonpath.jsonpath(json_response,'name')
print(updating_list[0])
# Validating names
assert updating_list[0] == 'Gnanendra12 updated'
# validating response code
assert response.status_code == 201



