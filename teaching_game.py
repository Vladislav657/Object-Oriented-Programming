import random

dicts_of_questions = [{
    "q": "How many days do we have in a week?",
    "d": "1",
    "a": "7"
}, {
    "q": "How many letters are there in the English alphabet?",
    "d": "3",
    "a": "26"
}, {
    "q": "How many sides are there in a triangle?",
    "d": "2",
    "a": "3"
}, {
    "q": "How many years are there in one Millennium?",
    "d": "2",
    "a": "1000"
}, {
    "q": "How many sides does hexagon have?",
    "d": "4",
    "a": "6"
}, {
    "q": "Which planet is known as the Red Planet?",
    "d": "2",
    "a": "mars"
}, {
    "q": "How many years are there in a century?",
    "d": "1",
    "a": "100"
}, {
    "q": "How many strings does a violin have?",
    "d": "3",
    "a": "4"
}, {
    "q": "What do people often call American flag?",
    "d": "4",
    "a": "stars and stripes"
}]


class Question:
    def __init__(self, question, difficulty, correct_answer):
        self.question = question
        self.difficulty = difficulty
        self.correct_answer = correct_answer

        self.asked = False
        self.answer = None
        self.points = int(difficulty) * 10

    def get_points(self):
        return self.points

    def is_correct(self):
        return self.answer == self.correct_answer

    def build_question(self):
        return f'\nВопрос: {self.question}\nСложность {self.difficulty}/5'

    def build_feedback(self):
        if self.is_correct():
            return f'Ответ верный, получено {self.points} баллов'
        else:
            return f'Ответ неверный, верный ответ - {self.correct_answer.capitalize()}'


def end_of_noun(num):
    if num % 100 not in [12, 13, 14] and num % 10 in [2, 3, 4]:
        return 'а'
    elif num % 100 != 11 and num % 10 == 1:
        return ''
    else:
        return 'ов'


questions = [Question(i['q'], i['d'], i['a']) for i in dicts_of_questions]
random.shuffle(questions)

score = 0
correct = 0

print('Игра начинается!')

for quest in questions:
    print(quest.build_question())
    ans = input().lower()
    quest.answer = ans
    print(quest.build_feedback())
    if quest.is_correct():
        score += quest.points
        correct += 1

print(f'\nВот и всё!\nОтвечено {correct} вопрос{end_of_noun(correct)} из {len(questions)}\nНабрано баллов: {score}')
