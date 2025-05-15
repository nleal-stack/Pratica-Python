import math

lista_d = []
while True:
    valor_d = int(input("Digite um valor desejado para D: "))
    lista_d.append(valor_d)

    continuar = input("Deseja adicionar mais valores para D na lista? [s/n]: ")
    if continuar != 's':
        break

for D in lista_d:
    Q = ((10 * D) / 3)
    resultados = math.sqrt(Q)
    print(f"Quando D = {D}, Q = {resultados}")