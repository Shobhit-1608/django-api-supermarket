import requests
import json
from requests.api import get

def get_queuelength():
    url = 'http://localhost:8000/customer/' 
    r = requests.get(url)
    print(r)
    members = r.json()
    print(members)
    members_number = len(members)
    print(members_number)
    return members_number

x = get_queuelength()