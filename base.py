import random

filename = "Word.txt"


def get_random_word_from_text(text):
    """Выбор случайного слова из списка"""
    with open(text, "r", encoding="UTF-8") as file:
        f = file.read()
        word = f.split()
    if word:
        return random.choice(word).lower()


def start_game():
    """ Запуск игры """
    if start_message():
        round_game()


def start_message():
    """ Вывод сообщения для игрока в начале игры"""
    try:
        input_player = int(input("""
            Нажмите 
            1 - Начать играть
            0 - Выйти из игры
            """))
        if input_player == 1:
            return True
        elif input_player == 0:
            print("""
        Возвращайся! =)
        """)
            return False
        else:
            print(f"Пожалуйста введите только цифру {1} или {0}")
            start_game()
    except ValueError:
        print(f"Пожалуйста введите только цифру {1} или {0}")
        start_game()


def round_message(word):
    print(f"""
    Угадай слово {word}
    """)


def round_game():
    """ Функция определяет Старт игры """

    start_word = get_random_word_from_text(filename)  # Загадываем слово
    transform_letters = transform_letters_to_symbols(start_word)  # Шифруем слово для игрока
    player_life = 6  # Счетчик жизней игрока

    round_message(transform_letters)  # Выводит текст Угадай слово
    while start_word != transform_letters:
        sim = input("Введите букву = ").lower()
        if sim in start_word:
            decrypt = reveal_letter(start_word, sim)  # Запоминаем раскрытые буквы в слове
            transform_letters = decrypt_word(transform_letters,
                                             decrypt)  # Применяем раскрытую букву в зашифрованом слове
            print(transform_letters)
            draw_noose(player_life)
            get_player_life(player_life)
        else:
            player_life -= 1
            if player_life != 0:
                print(transform_letters)
                draw_noose(player_life)
                get_player_life(player_life)
            else:
                print("Ты проиграл!")
                start_game()
                break
    else:
        print('Ты выйграл!')


def transform_letters_to_symbols(name):
    """ Шифрует слово в символ * """
    hush_word = ''
    for _ in name:
        hush_word += '*'
    return hush_word


def decrypt_word(transform_letters, word):
    """ Разшифрует слово из символа * в угаданную букву """
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


def get_player_life(count):
    """ Вывод в консоль количетсво попыток """

    print(f"У вас осталось {count} жизней!")


def draw_noose(count):
    """ Вывод изображения виселицы """

    if count == 6:
        print("""  
        ------
        |   |
        |   
        |
        |
        |
        ======
        """)
    if count == 5:
        print(""" 
        ------
        |   |
        |   O
        |
        |
        |
        ======
        """)
    if count == 4:
        print("""  
        ------
        |   |
        |   O
        |  /|
        |
        |
        ======
        """)
    if count == 3:
        print("""  
        ------
        |   |
        |   O
        |  /|\\
        | 
        |
        =====
        """)
    if count == 2:
        print("""  
        ------
        |   |
        |   O
        |  /|\\
        |   |
        | 
        =====
        """)
    if count == 1:
        print("""  
        ------
        |   |
        |   O
        |  /|\\
        |   |
        |  /
        =====
        """)
    if count == 0:
        print("""  
        ------
        |   |
        |   O
        |  /|\\
        |   |
        |  / \\
        =====
        """)


start_game()
