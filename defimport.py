import requests
def informacoes(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    r = requests.get(url)
    info = r.json()
    return info

cep = input('Digite o CEP: ')
print(informacoes(cep))