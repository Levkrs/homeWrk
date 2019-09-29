# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y


equation = 'y = -12x + 100.2121'
x = 2.5

y= 0

arr = equation.split(" ")

print(arr)
k_string = ""

len_val = len(arr[2])
print(len_val)

find_index_neg = arr[2].find("-")
find_index_x = arr[2].find("x")

temp = str(arr[2])
print(temp.index("x"))
pos_x = int(temp.index("x"))

k_string = temp.replace("x", "")
k1_string = k_string.replace("-","")
k1_int = int(k1_string)
b_int = float(arr[4])

print(k1_int, "k")
print(b_int, "B")

if (find_index_neg < 0):
    y = (k1_int*x) + int(b_int)
else:
    y = ((k1_int*-1)*x) + int(b_int)
print("y = ", y)







# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты


date = '01.01.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'



lst_month = {"01": 31, "02":28, "03":31, "04":30,"05":31,"06":30, "07":31,"08":31,"09":30,"10":31,"11":30,"12":31}


cur_date = date.split(".")

date_val = cur_date[0]
month_val = cur_date[1]
year_val = cur_date[2]

if (year_val.find(".") == -1 and year_val.find("-") == -1 and len(year_val) == 4 and int(year_val) <= 9999 and int(year_val)>=1):
    if (month_val.find(".") == -1 and len(month_val) == 2 and int(month_val) <= 12 and int(month_val)>=1):
        if(date_val.find(".") == -1 and len(date_val) == 2 and date_val.find("-") == -1 and int(date_val) >= 1 and
                int(date_val) <= int(lst_month[month_val])):
            print("Введенная корректная дата")
        else:
            print("Некорректна введено число ")
        print("Месяц подходит")
    else:
        print("Месяц не подходит")
    print("Год подходит")
else:
    print("Год не подходит")
print(cur_date)



# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#    27 28 29 30
#    23 24 25 26
#    19 20 21 22
#    15 16 17 18
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

n = int(input("Введите колличество элементов: "))

#n = 45
arr = [1]
count=1

for i in range(2,n+1):
    arr.append(i)


arr_plus = []
arr_res = []

count_while = 0
while count< len(arr):
    start_index = 0
    stop_index = count*count
    x = arr[start_index:stop_index]
    arr_res.append(x)
    del arr[start_index:stop_index]
    count+=1
print(arr_res)
print(len(arr_res))



arr_res_flour = []
count_flour = 1
for i in arr_res:
    z = len(i)
    if ((len(i) / count_flour) == count_flour):
        count_while = 1
        while count_while <=count_flour:
            arr_res_flour.append(i[0:count_flour])
            del i[0:count_flour]
            count_while+=1
        count_flour+=1
    elif(int(len(i) / count_flour) > 0 ):
        res_element = int(len(i) / count_flour)
        count_while_el = 1
        while count_while_el <= res_element+1:
            arr_res_flour.append(i[0:count_flour])
            del i[0:count_flour]
            count_while_el+=1



print(arr_res_flour)


y = int(input("Введите элемент для поиска: "))
#y = 21


flour = 1

for i in arr_res_flour:
    count_left = 1
    for g in i:
        if(g == y):
            print("Вход: ", y)
            print("Выход: ", flour, count_left)
            #print("Этаж ", flour)
            #print("Номер слева ", count_left)
        count_left+=1


    flour+=1





