import requests

url = "http://127.0.0.1:8000"

resposta = requests.get(url)

print(resposta.json())