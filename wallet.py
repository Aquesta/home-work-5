# программа личный счет

balance = 100
history = {}


def input_amount(re_fill=True):
    # TODO: после урока по try/catch отловить что вводят не цифры
    if re_fill:
        return int(input("Введите сумму для пополнения баланса: "))
    else:
        return int(input("Введите сумму покупки: "))


def refill(summ, current_balance):
    new_balance = current_balance + summ
    print(f'Баланс пополнен на {summ}, текущий баланс: {new_balance}. Возврат в меню.')
    return new_balance


def check_balance(summ, current_balance):
    if summ > current_balance:
        return False
    else:
        return True


def purchase(summ, current_balance):
    if check_balance(summ, current_balance):
        product = input('Введите название покупки: ')
        new_balance = current_balance - summ
        write_history(product, summ)
        return new_balance
    else:
        print(print('Недостаточно средств. Возврат в меню.'))
        return current_balance


def write_history(product_name, amount):
    print('Покупка совершена, возврат в меню.')
    history[product_name] = amount


def check_history():
    if not history:
        print('Нет покупок, возврат в меню.')
    else:
        for k, v in history.items():
            print(f'Товар: {k} --> {v}')
            print(f'Текущий баланс: {balance}')


def start_program():
    global balance
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            balance = refill(input_amount(), balance)
        elif choice == '2':
            balance = purchase(input_amount(re_fill=False), balance)
        elif choice == '3':
            check_history()
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
