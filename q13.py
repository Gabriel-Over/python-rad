def fibonacci(n_termo: int):
    comeco = 0
    soma = 1
    resultado = 0

    print(soma)
    for i in range (n-1):
        resultado = comeco + soma
        comeco = soma
        soma = resultado
        print(resultado)


n = int(input("Digite o n-ésimo termo da sequencia de Fibonacci: "))
fibonacci(n)
