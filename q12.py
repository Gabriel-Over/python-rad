while True:
    try:
        escolha = input("Você quer escrever a temperatura celsius (C) ou fahrenheit (F)? ")
        if escolha.upper() == 'C':
            temperatura = float(input("Digite a temperatura em ºC: "))
            conversao = temperatura * 1.8 + 32
            
            print(f"A temperatura em Fahrenheit é: {conversao}ºF")
            
            break
        elif escolha.upper() == 'F':
            temperatura = float(input("Digite a temperatura em ºF: "))
            conversao = (temperatura-32)/1.8
            
            print(f"A temperatura em Celsius é: {conversao}ºC")
            break
        else:
            print("Valor invalido")
    except ValueError:
        print("Erro")