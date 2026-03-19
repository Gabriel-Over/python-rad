def ordenar(lista: list[int]):
    tamanho = len(lista)
    for i in range(tamanho - 1):
        for j in range(tamanho - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

    print(*lista)


lista = [4, 1, 6, 3, 0, 7, 9, 8]
print("Lista desordenada:")
print(*lista)

print("Lista ordenada:")
ordenar(lista)
