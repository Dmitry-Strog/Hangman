import random

filename = "Word.txt"


def get_random_word_from_text(text):
    with open(text, "r", encoding="UTF-8") as file:
        f = file.read()
        word = f.split()
    if word:
        return random.choice(word)


start_word = get_random_word_from_text(filename)



def start_game():
    """ Функция определят Старт игры"""

    x = input("Нажмите Y для началы игры, либо Q для выхода из игры = ")
    transform_letters = transform_letters_to_symbols()
    if x == 'Y':
        print("Вам загадали слово =", transform_letters)
        while start_word != transform_letters:
            input("Введите букву = ").upper()
    else:
        return "Возвращайтесь"


def transform_letters_to_symbols():
    word = start_word
    hush_word = ''
    for _ in word:
        hush_word += '*'

    return hush_word


print(start_game())