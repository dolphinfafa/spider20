import requests

# 调度器
def search():
    params = input('enter the search keywords: ')
    url = f'https://www.vcg.com/creative-image/168909/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'Referer': 'https://www.vcg.com/'
    }
    res = requests.get(url=url, headers=headers)
    print(res)

search()