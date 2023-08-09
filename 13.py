def count_word_occurrences(text):
    word_count = {}
    words = text.split()

    for word in words:
        # Remove pontuações para contar palavras corretamente
        word = word.strip(".,!?;:'\"()[]{}")
        word = word.lower()  # Considera palavras em minúsculas
        
        if word:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count

def main():
    input_text = input("Digite o texto: ")
    word_occurrences = count_word_occurrences(input_text)
    
    print("\nContagem de ocorrências de palavras:")
    for word, count in word_occurrences.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
