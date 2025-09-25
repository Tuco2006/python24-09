import requests
url ='https://viacep.com.br/ws/03442110/json/'
r = requests.get(url)
info = r.json()
print(info)
