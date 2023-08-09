def numeros_pares(lista):
    return [numero for numero in lista if numero % 2 == 0]

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares_lista = numeros_pares(lista_numeros)
print(numeros_pares_lista)