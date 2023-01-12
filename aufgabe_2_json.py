import json

with open('tsjson/accounts.json', 'r') as f:
    data = json.load(f)
    print (json.dumps(data, indent =2))