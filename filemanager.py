import os
from shutil import copy, copytree
import platform


def create_folder():
    print('Текущая дериктория: ', os.getcwd())
    folder_name = input('Введите название папки: ')
    if os.path.isdir(folder_name):
        print('Такая папка уже есть.')
    else:
        os.mkdir(folder_name)
        print('Создана папка ', os.getcwd() + '/' + folder_name)


def delete_folder_files():
    show_dir(False)
    name = input('Введите наименование папки/файла для удаления: ')
    full_path = os.path.join(os.getcwd(), name)
    if os.path.isdir(full_path):
        os.removedirs(name)
        print(f'Папка {name} удалена.')
        input('Что бы продолжить нажмите любую клавишу...')
    elif os.path.isfile(full_path):
        os.remove(full_path)
        print(f'Файл {name} удален.')
        input('Что бы продолжить нажмите любую клавишу...')
    else:
        print('Такого файла/папки не существует')
        input('Что бы продолжить нажмите любую клавишу...')


def show_dir(show=True):
    path = os.getcwd()
    results = sorted(os.listdir(path))
    for n, item in enumerate(results):
        print(n + 1, item)
    if show:
        input('Что бы продолжить нажмите любую клавишу...')


def copy_items():
    show_dir(False)
    old_name = input('Введите имя файла/папки для копирования: ')
    dst_name = input('Введите имя нового файла/папки: ')
    if os.path.isdir(old_name):
        copytree(old_name, dst_name)
    else:
        copy(old_name, dst_name)


def show_items(look_dir=True) -> list:
    path = os.getcwd()
    items = os.listdir(path)
    dirs = []
    files = []
    for n in items:
        if look_dir:
            if os.path.isdir(n):
                print(n)
                dirs.append(n)
        else:
            if os.path.isfile(n):
                print(n)
                files.append(n)
    return dirs if look_dir else files


def save_items_to_file():
    with open('listdir.txt', 'w') as f:
        dir_for_save = show_items()
        files_for_save = show_items(look_dir=False)
        f.write(f'dir: {", ".join(dir_for_save)} \n')
        f.write(f'files: {", ".join(files_for_save)}')


def show_info():
    n = 0
    for i in platform.uname():
        n += 1
        print(n, i)
    input('Что бы продолжить нажмите любую клавишу...')


def show_user_info():
    print('Создатель программы: ', os.environ['LOGNAME'])
    input('Что бы продолжить нажмите любую клавишу...')


def change_dir():
    path = os.getcwd()
    print('Текущая дериктория: ', path)
    new_dir = input('Введите путь к новой директории: ')
    os.chdir(new_dir)
    print('Текущая дериктория: ', os.getcwd())
    input('Что бы продолжить нажмите любую клавишу...')
