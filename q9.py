arquivo = "exemplo.txt"

with open(arquivo, 'r') as file:
    conteudo = file.read()
    qntd_palavras = len(conteudo.split())
    print(conteudo)
    print(f"A quantidade de palavras é: {qntd_palavras}")