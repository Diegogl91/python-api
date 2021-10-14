import requests

def get_titles():
    titles = []
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    for i in range(0,len(response.json()['posts'])):
        titles.append(response.json()['posts'][i]['title'])
        
    # your code here
    return titles


print(get_titles())