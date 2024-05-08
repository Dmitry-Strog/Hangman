import random

filename = "Word.txt"


def get_random_word_from_text(text):
    """Выбор случайного слова из списка"""
    with open(text, "r", encoding="UTF-8") as file:
        f = file.read()
        word = f.split()
    if word:
        return random.choice(word)


def start_game():
    """ Функция определяет Старт игры """

    start_word = get_random_word_from_text(filename)
    transform_letters = transform_letters_to_symbols(start_word)

    x = input("Нажмите Y для началы игры, либо Q для выхода из игры = ")
    if x == 'Y':
        print("Вам загадали слово =", transform_letters, start_word)
        while start_word != transform_letters:
            sim = input("Введите букву = ")
            if sim in start_word:
                decrypt = reveal_letter(start_word, sim)
                transform_letters = decrypt_word(transform_letters, decrypt)
                print(transform_letters)
        else:
            return """
            ******************
            Поздравляю вы отгадали слово!
            ******************
            """
    else:
        return "Возвращайтесь"


def transform_letters_to_symbols(name):
    """ Шифрует слово в символ * """
    hush_word = ''
    for _ in name:
        hush_word += '*'
    return hush_word


def decrypt_word(transform_letters, word):
    """ Разшифрует слово из символа * в угаданное слово """
    combined_word = []
    for char1, char2 in zip(transform_letters, word):
        if char1 == '*':
            combined_word.append(char2)
        else:
            combined_word.append(char1)

    return ''.join(combined_word)


def reveal_letter(word, sim):
    """ Раскрытие определенной буквы в слове"""

    new_word = []
    for i in word:
        if i == sim:
            new_word.append(sim)
        else:
            new_word.append("*")
    return ''.join(new_word)


print(start_game())
