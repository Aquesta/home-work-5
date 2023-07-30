import random

peoples = {'Пушкин': ['06.06.1799', 'шестое июня 1799'],
           'Ленин': ['22.04.1870', 'двадцать второе апреля 1870'],
           'Сталин': ['18.12.1878', 'восемьнадцатое декабря 1878'],
           'Ельцин': ['01.02.1931', 'первое фераля 1931'],
           'Путин': ['07.10.1952', 'седьмое октября 1952']}


def print_result(count_correct_answers, number_questions):
    print("--------- RESULTS----------", end='\n')
    print(f"Количество верных ответов: {count_correct_answers}")
    print(f"Количество не верных ответов: {number_questions - count_correct_answers}")
    print(f"Процент правильных ответов: {count_correct_answers / number_questions * 100} %")
    print(f"Процент не правильных ответов: {(number_questions - count_correct_answers) / number_questions * 100} %")


def sample_from_dict(dictionary, sample=2):
    keys = random.sample(list(dictionary), sample)
    values = [dictionary[k] for k in keys]
    return dict(zip(keys, values))


def check_answer(dictionary: dict, answer: str, name: str) -> bool:
    for _ in dictionary.keys():
        if answer == dictionary[name][0]:
            print('Правильный ответ')
            return True
        else:
            print(f'Неправильно, верный ответ {dictionary[name][1]}')
            return False


def get_names(dictionary):
    names = []
    for n in dictionary.keys():
        names.append(n)
    return names

def game(dictionary):
    count_correct = 0
    count_try = int(input(f'Введите количество попыток (мин 1, макс 5): '))
    dictionary_random = sample_from_dict(dictionary, count_try)
    names = get_names(dictionary_random)
    while count_try != 0:
        answer = input(f'Введите дату рождения в формате "dd.mm.yyyy" {names[count_try-1]}: ')
        if check_answer(dictionary_random, answer, names[count_try-1]):
            count_correct += 1
        count_try -= 1
    print_result(count_correct, len(dictionary_random))


def victory_start_game():
    game(peoples)
    start_again = int(input('Хотите продолжить игру? (1 - да, 0 - нет: '))
    while start_again == 1:
        game(peoples)
        start_again = int(input('Хотите продолжить игру? (1 - да, 0 - нет: '))
