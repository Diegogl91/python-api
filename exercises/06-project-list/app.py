import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
name = response.json()[1]

print(name['name'])
# your code here