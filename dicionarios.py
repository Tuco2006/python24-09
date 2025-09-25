def valor(d, c):
    if c in d:
        return d[c]
    return None

pessoa = {
    'nome': 'Mateus',
    'idade': 25,
    'sexo': 'M'
}

print(pessoa.get('cc'))
pessoa['sobrenome'] = 'Saavedra'
print(pessoa.get('sobrenome'))



