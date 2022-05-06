import pytest
import requests
import jsonpath
import json

url = 'https://reqres.in/api/users'


def test_creatingUSer():
    file = open('C:\\Users\\Gnanendra\\Desktop\\creatingUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    print(response.content)
    assert response.status_code == 201
    print(response.headers)
    response_json = json.loads(response.text)
    name = jsonpath.jsonpath(response_json, 'name')
    print(name[0])
    assert name[0] == 'Gnanendra12 updated'
    # assert name[0] == 'leader'


def test_Updating_newUser():
    file = open('C:\\Users\\Gnanendra\\Desktop\\creatingUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    print(response.content)
    assert response.status_code == 201
    print(response.headers)
    json_response = json.loads(response.text)
    updating_list = jsonpath.jsonpath(json_response, 'name')
    print(updating_list[0])
    assert updating_list[0] == 'Gnanendra12 updated'
    # validating response code
    assert response.status_code == 201
