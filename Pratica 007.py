lista = []
while True:
    palavra = input("Digite uma palavra desejada aqui: ")
    lista.append(palavra)

    continuar = input("Deseja adicionar mais alguma palavra na frase? [s/n]: ")
    if continuar != 's':
        break

palavras_ordenadas = sorted(lista, key=str.lower)
frase_ordenada = " ".join(palavras_ordenadas)

print(f"A frase escrita, agora ordenada, foi: {frase_ordenada}")