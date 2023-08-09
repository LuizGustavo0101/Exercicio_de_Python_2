def soma_numeros_de_1_a_100():
    soma = 0
    for numero in range(1, 101):
        soma += numero
    return soma

resultado = soma_numeros_de_1_a_100()
print("A soma dos números de 1 a 100 é:", resultado)