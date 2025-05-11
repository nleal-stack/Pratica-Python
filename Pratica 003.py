lista = []
while True:
    n = int(input("Digite um numero: "))
    lista.append(n)

    continuar = input("Deseja adicionar mais algum numero? [s/n] ")
    if continuar != 's':
        break

tupla = tuple(lista)
print(lista, tupla)