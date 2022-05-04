import random


def read_words():
    with open('words.txt') as file1:
        return list(map(lambda w: w.strip(), file1.readlines()))


def read_players():
    with open('history.txt') as file2:
        return list(map(lambda player: tuple(player.strip().split()), file2.readlines()))


def write_player(name, score):
    with open('history.txt', 'a') as file3:
        print(f'{name} {score}', file=file3)


print('Введите ваше имя')
user_name = input().capitalize()
words = read_words()
scores = 0

for word in words:
    list_word = list(word)
    random.shuffle(list_word)
    print(f'\n****Угадайте слово: {"".join(list_word)}')
    answer = input().lower()
    if answer == word:
        scores += 10
        print('Верно! Вы получаете 10 очков.')
    else:
        print(f'Неверно! Верный ответ – {word}.')

write_player(user_name, scores)
players = read_players()
print(f'\nВсего игр сыграно: {len(players)}\nМаксимальный рекорд: {max(players, key=lambda p: int(p[1]))[1]}')
