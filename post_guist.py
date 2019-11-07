import requests
import json

user = 'nestoralonsovina'
github_api = "https://api.github.com"
token = 'token'

def create_gist(params, payload):
    """
    creates a new guist with one or more files"
    """
    request = requests.post(f"{github_api}/gists", auth=(user, token), params=params, data=json.dumps(payload))

    if request.status_code == 201:
        return request.json()
    else:
        raise Exception(f"Query faild to run by returning code of {request.status_code} {request.text}")

params = {'scope': 'gist'}
payload = {
    'description': "GIST created with python",
    'public': True,
    "files": {
        "python request module": {
            "content": "hello les amigos"
        }
    }
}

#make the request
r = create_gist(params, payload)

print(r)



