import requests
import json

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
hour = response.json()['hours']
minutes = response.json()['minutes']
seconds = response.json()['seconds']


print("Current time: "+hour+" hrs "+minutes+" min and "+seconds+" sec") 