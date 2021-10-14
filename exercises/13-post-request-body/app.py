import requests

myjson = { "id":2323,"title": "Very big project"}
resp = requests.post("https://assets.breatheco.de/apis/fake/sample/save-project-json.php", json=myjson, headers={'Content-Type': 'application/json'})
print(resp.text)