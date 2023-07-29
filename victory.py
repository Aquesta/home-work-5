import random

peoples = {'Пушкин': ['06.06.1799', 'шестое июня 1799'],
           'Ленин': ['22.04.1870', 'двадцать второе апреля 1870'],
           'Сталин': ['18.12.1878', 'восемьнадцатое декабря 1878'],
           'Ельцин': ['01.02.1931', 'первое фераля 1931'],
           'Путин': ['07.10.1952', 'седьмое октября 1952']}


def print_result(count_correct_answers, count_error_answers, number_questions):
    print("--------- RESULTS----------", end='\n')
    print(f"Количество верных ответов: {count_correct_answers}")
    print(f"Количество не верных ответов: {count_error_answers}")
    print(f"Процент правильных ответов: {count_correct_answers / number_questions * 100} %")
    print(f"Процент не правильных ответов: {count_error_answers / number_questions * 100} %")


def sample_from_dict(dictionary, sample=2):
    keys = random.sample(list(dictionary), sample)
    values = [dictionary[k] for k in keys]
    return dict(zip(keys, values))


def game(dictionary):
    count_errors = 0
    count_correct = 0
    dictionary_random = sample_from_dict(dictionary)
    for key in dictionary_random.keys():
        answer = input(f'Введите дату рождения в формате "dd.mm.yyyy" {key}: ')
        if answer == dictionary[key][0]:
            print('Правильный вариант')
            count_correct += 1
        else:
            print(f'Неправильно, верный ответ {dictionary_random[key][1]}')
            count_errors += 1
    print_result(count_correct, count_errors, len(dictionary_random))


def victory_start_game():
    game(peoples)
    start_again = int(input('Хотите продолжить игру? (1 - да, 0 - нет: '))
    while start_again == 1:
        game(peoples)
        start_again = int(input('Хотите продолжить игру? (1 - да, 0 - нет: '))
