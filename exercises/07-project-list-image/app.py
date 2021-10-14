import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
project = response.json()[2]
img = project["images"]
print(img[2])
# your code here