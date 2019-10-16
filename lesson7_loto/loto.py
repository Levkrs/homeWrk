import random

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
number = random.randint(1,90)
print(number)


line1 = []
line2 = []
line3 = []

line1_cmp = []
line2_cmp = []
line3_cmp = []
# space_p = set()

rangeInt = list(range(1,90))
# print(rangeInt)
# print(len(rangeInt))

def gen_line(line):   # генератор строки
    space_p = set()
    if (len(line) == 0):
        while len(line) <= 8:
            x = random.randint(0,(len(rangeInt)-1))
            replay = False
            for i in line:
                if (i == x):
                    replay = True
            if (replay != True):
                line.append(rangeInt[x])
                #print("Удален элемент =", rangeInt[x])
                rangeInt.remove(rangeInt[x])
                #print(rangeInt)
        while len(space_p) <= 3:
                space_p.add(random.randint(0,7))

        #print("Line1 =", line)
        #print("Space count = ", space_p)
        line.sort()
        #print(line)
        list_space = list(space_p)
        #print(list_space)
        for i, val in enumerate(list_space):
            #print(val)
            line[val] = " "
        # print(line)
        return line

# n1 = 2


def number_map(full_l, n):
    # print("Массив - ", full_l)

    print("Выпал № - ", n)
    # print(full.index(number))
    in_answer = input("Зачеркнуть цифру? y/n ")
    if (in_answer == "y"):
        try: full_l[full_l.index(n)] = "-"
        except Exception:
            print("Такой цифры у вас нет, вы проиграли")
            return False
    elif (in_answer == "n"):
        try:
            if (full_l.index(n)):
                print("Вы проиграли")
                return False
        except Exception:
            print("Продолжаем")

    # print(full_l)
    return  full_l


line_test = [1,2,3,4,5,6]
line_test1 = ["f",2,"s","as"]


# print(number_map(line_test))

def all_int(list):
    empty_list = False
    for i in list:
        try:
            int(i)
            empty_list = True
            break
        except Exception:
            empty_list = False
    return empty_list


# print(all_int(line_test))




def start_game():
    line_user = gen_line(line1) + gen_line(line2) + gen_line(line3)
    line_computer = gen_line(line1_cmp) + gen_line(line2_cmp) + gen_line(line3_cmp)
    # print("Line_user - ",line_user)
    # print("Comp line - ", line_computer)
    # print(gen_line(line1))
    # print(gen_line(line2))
    # print(gen_line(line3))

    winer = False

    while winer == False :
        n1 = random.randint(1,90)
        # number_map(line_user, n1)
        print("--------- Ход игрока ---------")
        # print("Line_user - ",line_user)
        print(line_user[0:9])
        print(line_user[9:18])
        print(line_user[18:27])

        false_user = number_map(line_user,n1)
        # print("user - ",number_map(line_user,n1))
        print("--------- Ход компьютера --------")
        # print("Comp line - ", line_computer)
        print(line_computer[0:9])
        print(line_computer[9:18])
        print(line_computer[18:27])
        # print("cmp -", number_map(line_computer,n1))
        false_comp = number_map(line_computer,n1)
        if (false_user == False):
            print("Компьютер выиграл")
            winer = True
        elif (false_comp == False):
            print("Выиграл игрок")
            winer = True

        if (all_int(line_user) == False):
            print("Компьютер выиграл")
            winer = True
        elif(all_int(line_computer) == False):
            print("Выиграл игрок")
            winer = True


    # print(all_int(line_user))
    # print(all_int(line_computer))



start_game()