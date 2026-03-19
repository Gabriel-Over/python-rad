try:
    num1 = float(input("Digite um numero: "))
    num2 = float(input("Digite um numero: "))
except ZeroDivisionError:
    print("Erro!, você fez uma divisão por zero.")
    
divisao = num1 / num2
print(f"Resultado da divisão é: {divisao}")