from textwrap import indent
from urllib import response
import requests
import json


apiUrl="https://www.boredapi.com/api/activity"

response = requests.get(apiUrl)

responseBody= response.json()

responseBodyTxt = str(responseBody).replace("\'", "\"") # Double quote was getting converted to single quote

jsonObj = json.loads(str(responseBodyTxt))

jsonFormattedTxt = json.dumps(jsonObj, indent=2)

print(jsonFormattedTxt)

# Sample output
#{
#  "activity": "Invite some friends over for a game night",
#  "type": "social",
#  "participants": 4,
#  "price": 0,
#  "link": "",
#  "key": "6613428",
#  "accessibility": 0.2
#}
