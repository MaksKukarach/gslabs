def count_words(text):
    words = text.split()
    return len(words)

if __name__ == "__main__": # Типа по крутому сделал
    text = input("Введите текст: ")
    print(f"Количество слов в тексте: {count_words(text)}")
