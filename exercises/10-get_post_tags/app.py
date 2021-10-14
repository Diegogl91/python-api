import requests

def get_post_tags(post_id):
    tags = None
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    for i in range(0,len(response.json()['posts'])):
        if response.json()['posts'][i]['id'] == post_id:
            tags = (response.json()['posts'][i]['tags'])
    # your code here
    return tags


print(get_post_tags(146))