lista = []
while True:
    palavra = str(input("Escreva qualquer palavra que voce desejar aqui: "))
    lista.append(palavra)

    continuar = input("Deseja adicionar mais palavras a lista? [s/n]: ")
    if continuar != 's':
        break

palavras_ordenadas = sorted(lista)
lista_ordenada = []
lista_ordenada.append(palavras_ordenadas)

for nome in lista_ordenada:
    print(lista, nome)