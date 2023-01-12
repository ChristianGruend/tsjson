import json
#
with open('tsjson/accounts.json', 'r') as f:
    data = json.load(f)
#
frage = input("Sie koennen 'alter' oder 'konto' suchen:")

if frage == "alter":
        for account in data:
            if account["age"] > 25:
                print(account["name"],"ist",account["age"],"Jahre alt")
   
#
elif frage == "konto":

    balance = []

    for i in data:
        balance.append(i["balance"])

    highest = "0"
    for number in balance: 
        if number > highest:
            highest = number
    print("Der hoechste Kontostand betraegt:", highest)