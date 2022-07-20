import requests

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"params" : "value1"})
print(response.status_code)
print(response.text)