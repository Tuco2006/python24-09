def add_tupla(tupla, elemento):
    return tupla + (elemento,)

mytupla = (1, 2, 3, 4, 5)
mytupla = add_tupla(mytupla, 6)
print(mytupla)