import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project1.php")
name = response.json()['name']
print(name)
# your code here