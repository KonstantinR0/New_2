import string


def analyze_text(text):
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()

    words = text.split()

    word_count = len(words)

    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    vowels = "аеёиоуыэюя"
    vowel_count = sum(1 for char in text if char in vowels)

    print(f"Количество слов: {word_count}")
    print(f"Самое длинное слово: '{longest_word}'")
    print(f"Количество гласных: {vowel_count}")
    print("Частота слов:")
    for word, count in word_frequency.items():
        print(f"{word}: {count}")

user_input = input("Введите текст: ")
analyze_text(user_input)