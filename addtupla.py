a = (1, 2, 3, 4, 5)
print(f"tupla: {a}")
add = input('Digite um número que deseja adicionar à tupla:')

lista = list(a)
lista.append(add)
a = tuple(lista)
print(lista)
