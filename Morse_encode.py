import random

words = ['code', 'bit', 'list', 'soul', 'next', 'snake', 'tiny', 'well played', 'little', 'lead']
answers = []
morse_code = {
    ' ': '/',
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}


def morse_encode(word):
    morse = ''
    for j in word:
        morse += morse_code[j] + ' '
    return morse[:-1]


def get_word():
    global words
    return random.choice(words)


def print_statistics(the_answers):
    print(f'Всего задачек: {len(the_answers)}\nОтвечено верно: {the_answers.count(True)}'
          f'\nОтвечено неверно: {the_answers.count(False)}')


print('Сегодня мы потренируемся расшифровывать азбуку Морзе')
input('Нажмите Enter и начнем')
print()

for i in range(10):
    new_word = get_word()
    encode = morse_encode(new_word)
    print(f'Слово {i + 1}: {encode}')
    answer = input()
    if answer[0].lower() + answer[1:] == new_word:
        print(f'Верно, {new_word.capitalize()}!')
    else:
        print(f'Неверно, {new_word.capitalize()}!')
    words.remove(new_word)
    answers.append(answer[0].lower() + answer[1:] == new_word)
    print()

print_statistics(answers)
