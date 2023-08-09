lista = ["UM", "dois", "tres", "QUATRO", "CINCO", "Seis"]
maiusculo = []
minusculo = []

if lista.isupper():
    maiusculo.append(lista)
elif lista.islower():
    minusculo.append(lista)

print(f"Palavra em maiusculo: {maiusculo} \nPalavra em minusculo: {minusculo}")