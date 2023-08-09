palavra = input("Escreva uma palavra: ")

def verificador_de_palindromo():
    palavra_invertida = palavra[::-1]
    return palavra_invertida
    
palavra_invertida = verificador_de_palindromo()
if palavra == palavra_invertida:
    print("A palavra é um palindromo e se escreve ao contrario assim: ", palavra_invertida)
else:
    print("Não é um palindromo")