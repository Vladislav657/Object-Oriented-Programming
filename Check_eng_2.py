words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}
words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}
words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}
levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}
difficulty = {'легкий': words_easy, 'средний': words_medium, 'сложный': words_hard}
answers = {}

print('Выберите уровень сложности.\nЛегкий, средний, сложный.')
words = difficulty[input().lower()]
print()

for key in words.keys():
    print(f'{key}, {len(key)} букв, начинается на {words[key][0]}...')
    answer = input().lower()
    if answer == words[key]:
        print(f'Верно. {key.capitalize()} — это {words[key]}.')
    else:
        print(f'Неверно. {key.capitalize()} — это {words[key]}.')
    answers[key] = answer == words[key]
    print()

print('Правильно отвечены слова:')
print(*[key for key in answers.keys() if answers[key]], sep='\n')
print()
print('Неправильно отвечены слова:')
print(*[key for key in answers.keys() if not answers[key]], sep='\n')
print()
print(f'Ваш ранг:\n{levels[len([key for key in answers.keys() if answers[key]])]}')
