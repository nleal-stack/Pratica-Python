#Programa que pede lista de numeros divisiveis por 7, porem estes nao podem ser divisiveis por 5 ao mesmo tempo.

lista_7 = []
for num in range (2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        lista_7.append(num)
print(lista_7)