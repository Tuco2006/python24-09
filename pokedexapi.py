import requests
def pokemon(pok):
    url = f'https://pokeapi.co/api/v2/pokemon/{pok}'
    r = requests.get(url)
    info = r.json()
    return f'ID:{info['id']} \n tipo:{info['type'][0]['type']['name']}'

opcao = input('Digite o nome do pokemon: ')
print(pokemon(opcao))

