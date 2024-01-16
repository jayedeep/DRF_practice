import requests

base_url = 'http://127.0.0.1:8000'

def get_token(username,password,url=base_url):
    response = requests.post(url+'/gettoken',{'username':username, 'password':password})
    json_data = response.json()
    print('json_data',json_data)
    return json_data


get_token(username = 'admin',password='admin')