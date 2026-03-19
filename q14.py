#Módulo necessario pra poder remover a pontuação
import string

pal = input("Digite uma frase: ")

pal = pal.lower()
pal = pal.translate(str.maketrans('', '', string.punctuation))

inverso = pal[::-1]

if inverso == pal:
    print("Essa frase é um palíndromo.")
else:
    print("Essa frase não é um palíndromo.")
