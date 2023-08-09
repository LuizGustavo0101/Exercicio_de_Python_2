def main():
    try:

        input_sequence = input("Digite uma sequência de números separados por espaços: ")

        numbers = input_sequence.split()

        numbers = [int(num) for num in numbers]

        if len(numbers) == 0:
            print("Nenhum número foi inserido.")
            return

        max_number = max(numbers)
        min_number = min(numbers)
        
        print("Maior número:", max_number)
        print("Menor número:", min_number)

    except ValueError:
        print("Entrada inválida. Certifique-se de inserir apenas números separados por espaços.")

if __name__ == "__main__":
    main()
