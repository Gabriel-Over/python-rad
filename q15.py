import string

frase = input("Digite uma frase: ")
frase_cortada = frase.strip()
frase_cortada = frase_cortada.translate(str.maketrans('', '', string.punctuation))

num_palavras = len(frase_cortada.split())

print(f"Há {num_palavras} palavra(s)")
