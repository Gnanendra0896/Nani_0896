import requests
import json
import jsonpath

# API utl
url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

print(response)

# parse response to json forat
json_response = json.loads(response.text)
print(json_response)
# fetching values from jsonpath
pages = jsonpath.jsonpath(json_response, 'data')
# print(pages)
# assert pages[0] == 9

