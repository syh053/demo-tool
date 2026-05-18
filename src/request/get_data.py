import requests

res = requests.get('https://www.cnn.com/')

print(res.status_code)