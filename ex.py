a = {"banana", "maça", "pera", "kiwi"}
b = {"maça", "abacaxi", "morango", "kiwi"}

opc = int(input('Digite um valor:'))
if opc == 1:
    c = a & b
    print(c)
elif opc == 2:
    d = a - b
    print(d)
elif opc == 3:
    e = b - a
    print(e)
elif opc == 4:
    f = a - b
    g = b - a
    h = f | g
    print(h)