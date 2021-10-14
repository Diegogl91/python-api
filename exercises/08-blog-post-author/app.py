import requests
url="https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
response = requests.get(url)
print(response.json()['posts'][0]['author']['name'])
# your code here