# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

#number = 5.28567654
#ndigits = 5



def my_round(number, ndigits):


    resault = 0

    number_string = str(number)

    number_string = number_string.split(".")
    after_point = number_string[1]
    string_after_point = str(after_point)
    x = len(string_after_point)
    index_if = ndigits + 1

    if (len(string_after_point) >ndigits):
        if (int(string_after_point[ndigits]) >= 6):

            # print(string_after_point[ndigits])
            summ_num = "0."
            summ_count = ndigits - 1
            count = 1
            while (count <= summ_count):
                summ_num += "0"
                count += 1
            summ_num += "1"
            summ_num = float(summ_num)
            resault = number + summ_num
            # print(resault)
        else:
            resault = number

        split_resault = str(resault)
        split_resault = split_resault.split(".")
        split_element = split_resault[1]
        str_split_element = split_element[0:ndigits]
        resault_float = float(split_resault[0] + "." + str(str_split_element))

    # print(split_resault)
    # print(split_element)
    # print("Результируюее ", str_split_element)
    # print("Итог ==", resault_float)

        return resault_float
    else:
        return "Запрашиваемое колличество знаков превышает число"

print(my_round(5.28567654, 3))




# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):

    str_ticket_number = str(ticket_number)
    if (len(str_ticket_number) == 6):
        str_ticket_number1 = str_ticket_number[0:3]
        str_ticket_number2 = str_ticket_number[3:6]

        count1 = 0
        resault1 = 0
        while (count1 <= (len(str_ticket_number1) - 1)):
            resault1 += int(str_ticket_number1[count1])
            count1 += 1
        # print("Результат 1=", resault1)

        count2 = 0
        resault2 = 0
        while (count2 <= (len(str_ticket_number2) - 1)):
            resault2 += int(str_ticket_number2[count2])
            count2 += 1
        # print("Результат 2 =", resault2)

        if (resault1 == resault2):
            return ("Билет счастливый")
        else:
            return ("Билет обычный")
    else:
        return ("Билет не из 6 цифр")


print(lucky_ticket(534234))


