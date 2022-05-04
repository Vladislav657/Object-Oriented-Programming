from wordsgame import *
from utils import *

print('Введите имя игрока')
user_name = input()
player = Player(user_name)
word = load_random_word(get_words())
i = 0

print(f'\nПривет, {user_name}!\nСоставьте {word.subwords_count()} слов из слова {word.basic_word}')
print('Слова должны быть не короче 3 букв\nПоехали, ваше первое слово?\n')

answer = input().lower()
if answer in ['стоп', 'stop']:
    print(f'игра завершена!\nвы угадали {player.used_words_count()} слов**')
    exit()
elif word.is_right(answer):
    print('верно\n')
    player.add_word(answer)
else:
    print('неверно\n')

while i != word.subwords_count():
    i += 1
    answer = input().lower()
    if answer in ['стоп', 'stop']:
        print(f'игра завершена!\nвы угадали {player.used_words_count()} слов**')
        exit()
    elif player.is_used(answer):
        print('Это слово уже было\n')
        i -= 1
    elif word.is_right(answer):
        print('верно\n')
        player.add_word(answer)
    else:
        print('неверно\n')
        i -= 1

print(f'слова закончились, игра завершена!\nвы угадали {player.used_words_count()} слов**')
