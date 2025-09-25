a = ('maça', 'banana', 'pera')
print(a)
remove = input('Digite o item que deseja remover:')

lista = list(a)
if remove in lista:
    lista.remove(remove)
    print(lista)
else:
    print(f"{remove} não está na tupla!")

a = tuple(lista)
print(f"A tupla tem: {a}")
