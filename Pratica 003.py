#Programa que pede para o usuario digitar um numero e logo apos vai expressar esse(s) numero(s) em formato de lista e em formato de tupla

lista = []
while True:
    n = int(input("Digite um numero: "))
    lista.append(n)

    continuar = input("Deseja adicionar mais algum numero? [s/n] ")
    if continuar != 's':
        break

tupla = tuple(lista)
print(lista, tupla)
