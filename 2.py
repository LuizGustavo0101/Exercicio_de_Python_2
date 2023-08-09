def media(lista):
    if not lista:
        return 0
    
    soma = sum(lista)
    media = soma / len(lista)
    return media

listaNumeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]
resultado = media(listaNumeros)
print("A média dos valores é:", resultado)