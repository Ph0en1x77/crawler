import requests

def crawler(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36'
        }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None
