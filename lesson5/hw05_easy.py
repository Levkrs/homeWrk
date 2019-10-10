import os
import sys

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

#print(sys.path)
#print(sys.path[0])


def mk_dir():
     dir_path1 = os.path.join(os.getcwd(), "dir_1")
     dir_path2 = os.path.join(os.getcwd(), "dir_2")
     try:
         os.mkdir(dir_path1)
     except FileExistsError:
         print("Такая папака уже существует")
     try:
         os.mkdir(dir_path2)
     except FileExistsError:
         print("Такая папака уже существует")
#mk_dir()

def del_dir():
    dir_path1_rem = os.path.join(os.getcwd(), "dir_1")
    dir_path2_rem = os.path.join(os.getcwd(),"dir_2")
    try:
        os.rmdir(dir_path1_rem)
    except:
        print("Такой папки нет")
    try:
        os.rmdir(dir_path2_rem)
    except:
        print("Такой папки нет")
#del_dir()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def dir_show():
    dir_arr = os.listdir()
    #path_os = os.path.join(os.getcwd())
    for i in dir_arr:

        path_os = os.path.join(os.getcwd(), i)

        if(os.path.isdir(path_os)):
            print(i, "Директория")
        else:
            pass
            #print(i, " Не директория")

#dir_show()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():

    name_script = str(os.path.basename(__file__))
    new_name_file = "Copy_" + name_script

    print(new_name_file)
    with open(new_name_file, 'w') as f:
        f.write("")

#copy_file()




