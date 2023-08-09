def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Conversor de Temperatura")
    print("Escolha uma opção:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")

    choice = int(input("Digite o número da opção desejada: "))

    if choice == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius equivalem a {fahrenheit:.2f} Fahrenheit.")
    elif choice == 2:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit equivalem a {celsius:.2f} Celsius.")
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()
