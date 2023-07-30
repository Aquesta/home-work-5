import json

balance = 0
history = {}


def save_state(current_balance: int, current_history: dict):
    current_state = {}
    current_state.update({'balance': current_balance, 'history': current_history})

    with open('balance.json', 'w') as f:
        json.dump(current_state, f)


def load_state():
    global balance
    global history
    with open('balance.json', 'r') as f:
        saved_state = json.load(f)
        balance = saved_state['balance']
        history = saved_state['history']


def input_amount(choice):
    # TODO: после урока по try/catch отловить что вводят не цифры
    if choice == '1':
        return int(input("Введите сумму для пополнения баланса: "))
    elif choice == '2':
        return int(input("Введите сумму покупки: "))
    elif choice == '3':
        return input('Введите название покупки: ')


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
        new_balance = current_balance - summ
        return new_balance
    else:
        print(print('Недостаточно средств. Возврат в меню.'))
        return current_balance


def write_history(product_name, amount, dictionary):
    """
    :param product_name: str
    :param amount: int
    :type dictionary: dict
    """
    print('Покупка совершена, возврат в меню.')
    dictionary.update({product_name: amount})


def check_history():
    if not history:
        print('Нет покупок, возврат в меню.')
    else:
        for k, v in history.items():
            print(f'Товар: {k} --> {v}')
            print(f'Текущий баланс: {balance}')


def start_program():
    global balance
    load_state()
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            balance = refill(input_amount('1'), balance)
        elif choice == '2':
            summ = input_amount('2')
            balance = purchase(summ, balance)
            write_history(input_amount('3'), summ, history)
        elif choice == '3':
            check_history()
        elif choice == '4':
            save_state(balance, history)
            break
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    start_program()
