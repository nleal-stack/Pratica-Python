lista = []
while True:
    n = [x for x in input("Digite algum numero binario que preferir aqui: ").split(',')]
    for i in n:
        decimal = int(i, 2)
        if decimal % 5 == 0:
            lista.append(i)
    
    continuar = input("Deseja adicionar mais algum numero binario aqui? [s/n]: ")
    if continuar != 's':
        break

print(','.join(lista))