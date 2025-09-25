def del_tupla(t, e):
    l = list(t)
    for i, j in enumerate(l):
        if j == e:
            l.pop(i)
    return tuple(l)
a = (1, 2, 3)
b = del_tupla(a, 2)
print(b)