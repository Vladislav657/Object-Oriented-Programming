import json


def load_questions():
    with open('questions.json', encoding='UTF-8') as json_file:
        return json.load(json_file)


def show_field():
    for key in questions.keys():
        print(key, end='\t')
        for i in questions[key].keys():
            if questions[key][i]['asked']:
                print(' ', end='\t')
            else:
                print(i, end='\t')
        print()


def parse_input():
    global inp
    return inp.split()


def show_question():
    global categ
    global num
    print(f'\nСлово {questions[categ.capitalize()][num]["question"]} в переводе означает:')


def show_stats():
    global points
    global correct
    global incorrect
    print(f'Ваш счет: {points}\nВерных ответов: {correct}\nНеверных ответов: {incorrect}')


def save_results_to_file():
    with open('results.json', 'w', encoding='UTF-8') as outfile:
        json.dump(dict({'points': points, 'correct': correct, 'incorrect': incorrect}), outfile)


questions = load_questions()
points, correct, incorrect = 0, 0, 0
count = 9

while count != 0:
    show_field()
    print('\nВыберете вопрос:')
    inp = input()
    categ, num = parse_input()
    if categ.capitalize() not in questions.keys() or categ.capitalize() in questions.keys() \
            and num not in questions[categ.capitalize()].keys():
        print('\nТакого вопроса нет, попробуйте еще раз!\n')
        count += 1
    elif not questions[categ.capitalize()][num]['asked']:
        questions[categ.capitalize()][num]['asked'] = True
        show_question()
        answer = input()
        if answer.lower() == questions[categ.capitalize()][num]['answer'] or \
                questions[categ.capitalize()][num]['answer'] == 'самолет' and answer.lower() == 'самолёт':
            points += int(num)
            correct += 1
            print(f'\nВерно, +{num}. Ваш счет = {points}\n')
        else:
            incorrect += 1
            points -= int(num)
            print(f'\nНеверно, на самом деле – {questions[categ.capitalize()][num]["answer"].capitalize()}.'
                  f' –{num}. Ваш счет = {points}\n')
    else:
        print('\nТакой вопрос уже был, попробуйте еще раз!\n')
        count += 1
    count -= 1

print('У нас закончились вопросы!\n')
show_stats()
save_results_to_file()
