import random

def guess_the_number():

    secret_number = random.randint(1, 100)
    attempts = 0

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        try:
            user_guess = int(input("Digite seu palpite: "))
            
            attempts += 1

            if user_guess < secret_number:
                print("Tente um número maior.")
            elif user_guess > secret_number:
                print("Tente um número menor.")
            else:
                print(f"Parabéns! Você adivinhou o número {secret_number} em {attempts} tentativas.")
                break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

if __name__ == "__main__":
    guess_the_number()