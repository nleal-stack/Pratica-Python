import math

#Definindo o A:
while True:
    try:
        a = float(input("Digite o valor do primeiro numero: "))
        break
    except ValueError:
        print("Valor invalido, apenas numeros!!")
resultado = 0

def input_op():
    while True:
        operacao = input("Digite a operacao desejada: [+, -, *, /, **, √, !, %, apagar]: ")
        if operacao.lower() == 'apagar':
            return None
        if operacao in ['+', '-', '*', '/', '**', '√', '!', '%']:
            return operacao
        else:
            return "Operacao invalida. Tente novamente ou digite 'apagar'."
        

#Funcao pra adicionar a operacao:
def op(a):
    
    operacao = input_op()
    if operacao is None:
        return "apagar"

    if operacao in ['+', '-', '*', '/', '%', '**']:
        while True:
            try:
                b = input("Digite o valor do segundo numero: ")

                if b == 'apagar':
                    return 'apagar'
                b = float(b)
                break
            except ValueError:
                print("Valor invalido, apenas numeros!!")

    match operacao:
        case '+':
            resultado = a + b

        case '-':
            resultado = a - b

        case '*':
            resultado = a * b

        case '/':
            if b == 0:
                if a == 0:
                    return "Indeterminado: ∞−∞"
                else:
                    return "Impossivel dividir por 0"
            else:
                resultado = a / b
        
        case '%':
            resultado = (a / 100) * b
        
        case '**':
            resultado = a ** b
        
        case '√':
            if a < 0:
                return "Raiz nao real"
            else:
                resultado = math.sqrt(a)
        case '!':
            if a >= 0:
                resultado = math.factorial(int(a))
            else:
                return "Fatorial n eh possivel com numeros negativos"
        
        case _:
            return "Operacao invalida"

    return resultado

while True:
    resultado = op(a)
    if isinstance (resultado, str):
        print(resultado)
        #Pedir novo valor pra A, agora funcional pra calculadora
        a = float(input("Digite o valor do primeiro numero: "))
        continue

    print(f"Resultado: {resultado}\n")
    a = resultado

    continuar = input("Deseja fazer mais alguma operacao? [s/n]: ")
    if continuar.lower() != 's':
        print("Encerrando calculadora\n")
        break