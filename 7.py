def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

numero = int(input("Escreva um número inteiro positivo: "))
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")