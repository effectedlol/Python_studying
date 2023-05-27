import random
word_list = ['СТОЛБ', 'МАШИНА', 'ДЕРЕВО', 'КОШКА', 'ЭЛЕКТРОСТАНЦИЯ', 'МАГНИТ']

def get_word():
    x = random.choice(word_list)
    return x


def display_hangman(tries):
    stages = [
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / \
        |
        |  Всего доброго!

        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / 
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |     |
        |     |
        |     
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    
        |     
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     
        |    
        |       
        |  
        '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print("Let's play Hangman!")
    print(display_hangman(tries))

    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    word_real = list(word_completion)

    print("Let's play Hangman!")
    print(word_real)

    while guessed == False or tries > 0:
        the_word = input()
        if the_word.isalpha() == False:
            print('Нормально вводи!')
            continue
        elif the_word.upper() in guessed_letters or the_word.upper() in guessed_words:
            print('Ты эту уже пробовал. Давай другую.')
            continue
        elif the_word.upper() not in word:
            print('Такой буквы нет, давай другую')
            guessed_letters.append(the_word.upper())
            tries -= 1
            print(display_hangman(tries))
        elif the_word.upper() == word:
            print('Да, это верное слово. Моя умница!')
            print('Сыграешь еще?')
            n = input()
            if n == 'да':
                play(get_word())
            else:
                print('Ок, ну как хочешь')
                break
        elif the_word.upper() in word:
            word_real[word.index(the_word.upper())] = the_word.upper()
            print('Одну угадали)')
            print(word_real)
            guessed_letters.append(the_word.upper())
            print(display_hangman(tries))
            if '_' not in word_real:
                print('Вы выиграли!')
                print('Еще сыграешь?')
                question = input()
                if question == 'да':
                    play(get_word())
                else:
                    print('Ясно. Давай тогда, счастливо')
                break
    if tries == 0:
        print('Сыграешь еще?')
        x = input()
        if x == 'да':
            play(get_word())
        else:
            print('Счастливо!')
play(get_word())