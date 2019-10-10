# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import os
import sys
#import easy.py



#print(sys.path)


print ("Вы находитесь - ",os.getcwd())
#print(os.getcwd())
url_folder = os.getcwd()

def func_list():

    print("cd <path_to_folder> - для перехода в папку")
    print("list - для просмотра содержимого текущей папки")
    print("del_f <folder_name> - для удаления папки")
    print("mkdir <dir_name> - для создания папки")



#print(os.getcwd())



def cd_to_folder():
    if dir_name:
        url_folder = dir_name
        print("Вы перешли в ", url_folder)
    else:
        print("Вы не ввели неправильный путь к папке")

def list_folder():

    dir_arr = os.listdir(url_folder)
    print(dir_arr)
    #easy.export_list_folder(url_folder)


def del_folder():
    dir_path1_rem = os.path.join(url_folder, dir_name)
    print(dir_path1_rem)
    try:
        os.rmdir(dir_path1_rem)
        print("Удалено")
    except:
        print("Такой папки нет")
def make_folder():

    dir_path1 = os.path.join(url_folder,dir_name)
    try:
        os.mkdir(dir_path1)
        print("Создано")
    except FileExistsError:
        print("Такая папака уже существует")

do = {
    "help": func_list,
    "cd": cd_to_folder,
    "list": list_folder,
    "del_f": del_folder,
    "mkdir": make_folder
}

try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None


if key:
    print("Key =", key)
    print(do[key])
    if do.get(key):
        do[key]()
    else:
        print("Неверный параметр")
# print(sys.argv)
# print(sys.argv[0])




