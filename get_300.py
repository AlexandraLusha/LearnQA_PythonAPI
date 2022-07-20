import requests

response = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
print(response.status_code)