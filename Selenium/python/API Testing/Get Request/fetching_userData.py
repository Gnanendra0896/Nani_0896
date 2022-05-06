import requests
#API utl
url = "https://reqres.in/api/users?page=2"

# send get request
response = requests.get(url)
print(response)    #getting response from server
print(response.content)
print(response.headers)
