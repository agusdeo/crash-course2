import requests

url = "https://detik.com"
requests.get(url)
print(f'content {requests.get(url).text}')
