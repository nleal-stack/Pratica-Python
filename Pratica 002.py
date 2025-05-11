#Programa que pede numeros e que eh pra imprimir esse dado numero e seu fatorial ao lado. Ex: [8, 40320]

while True:
    lista = []
    lista2 = []

    num = int(input("Digite um numero desejado: "))
    lista.append(num)

    fatorial = 1
    for i in range (1, num + 1):
         fatorial *= i
    lista2.append(fatorial)

    for a, b in zip(lista, lista2):
        print(f"{a}, {b}")
    
    continuar = input("Deseja continuar? [s/n] ").lower()
    if continuar != 's':
        break
