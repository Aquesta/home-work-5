from victory import victory_start_game as victory
from wallet import start_program as wallet


while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории (*необязательный пункт)')
    print('12. выход (или любая другая клавиша')

    choice = input('Выберите пункт меню: ')

    if choice == '1':
        pass
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6':
        pass
    elif choice == '7':
        pass
    elif choice == '8':
        pass
    elif choice == '9':
        victory()
    elif choice == '10':
        wallet()
    elif choice == '11':
        pass
    else:
        print('Выход..')
        break

