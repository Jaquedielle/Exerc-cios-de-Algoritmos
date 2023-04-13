termo = int(input('digite o numero do termo da serie fibonacci:'
))
ultimo = 1
penultimo = 0
for _ in range(termo):
    print(ultimo)
    aux = ultimo
    ultimo += penultimo
    penultimo = aux
