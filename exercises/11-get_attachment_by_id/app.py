import requests

def get_attachment_by_id(attachment_id):
    attachment = None
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    for i in range(0,len(response.json()['posts'])):
        for n in range(0,len(response.json()['posts'][i]['attachments'])):
            if response.json()['posts'][i]['attachments'][n]['id']  == attachment_id:
                attachment = (response.json()['posts'][i]['attachments'])
    # your code here
    return attachment

print(get_attachment_by_id(137))