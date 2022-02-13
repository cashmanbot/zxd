import requests
import json
import webbrowser
import time


print("STW DUPER MADE BY ADAMO_")
print("Opening URL...")
get_url= webbrowser.open('https://www.epicgames.com/id/api/redirect?clientId=ec684b8c687f479fadea3cb2ad83f5c6&responseType=code')

device_auth = input("Enter your device auth:")
print("Logging in...")
body = {'grant_type' : 'authorization_code', 'code' : device_auth}
r = requests.post('https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token', auth=('ec684b8c687f479fadea3cb2ad83f5c6', 'e1f31c211f28413186262d37a13fc84d'), data=body)

if r.status_code != 200:
    print("Invalid token")
    time.sleep(5)
    exit()
else:
    BEARER = r.json()["access_token"]
    Acc_id = r.json()["account_id"]
    print("Successfully logged in")

print("----->  Make sure to have enough space in your storage and mak sure to have quartz in your inventory")
print("----->  Once this is done, launch into your friend's homebase")
Ready=""
while Ready.lower() != "ready":
    Ready = input("Type ready if you're ready : ")
print("User ready")
headers = {'Authorization': 'Bearer ' + BEARER}
print("Getting profile...")
r=requests.post('https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/' + Acc_id + '/client/QueryProfile?rvn=-1&profileId=theater0', headers=headers, json={})
a = json.loads(r.text)
for k, v in a["profileChanges"][0]["profile"]["items"].items():
    if v['templateId'] == "Ingredient:ingredient_crystal_quartz":
        break
if v['templateId'] != "Ingredient:ingredient_crystal_quartz":
    print("You don't have quartz!")
    time.sleep(5)
    exit()
body={"transferOperations": [{"itemId": k,"quantity": 1,"toStorage": True,"newItemIdHint": "molleja"}]}
r=requests.post('https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/' + Acc_id + '/client/StorageTransfer?profileId=theater0&rvn=-1', headers=headers, json=body)
print("loading...")
numbers=[5,10,15,20,25]
count=0
while r.status_code != 200:
    print("Dupe failed, next attempt in 30 seconds")
    count += 1
    if count in numbers:
        print("----->  Make sure to have quartz in your inventory and enough room in your storage!")
        time.sleep(30)
        r
    else:
        time.sleep(30)
        r

r=requests.post('https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/' + Acc_id + '/client/QueryProfile?rvn=-1&profileId=outpost0', headers=headers, json={})
a = json.loads(r.text)
for k, v in a["profileChanges"][0]["profile"]["items"].items():
    if v['templateId'] == "Ingredient:ingredient_crystal_quartz":
        break
body={"transferOperations": [{"itemId": k,"quantity": 1,"toStorage": False,"newItemIdHint": "molleja"}]}
r=requests.post('https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/' + Acc_id + '/client/StorageTransfer?profileId=theater0&rvn=-1', headers=headers, json=body)
print("Dupe successful!")
print("Anything change you make to your inventory will not be saved once you leave the homebase!")
time.sleep(15)
exit()
