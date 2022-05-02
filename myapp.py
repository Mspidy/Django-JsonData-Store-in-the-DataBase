#3rd Party Application
import requests
import json
URL="http://127.0.0.1:8000/studcreate/"
data={
    'name':'Somnath',
    'roll':101,
    'city':'Ranchi'
}

#convert python to json ----->use dumps method
json_data = json.dumps(data)
r= requests.post(url=URL, data=json_data)
data = r.json()
print(data)
