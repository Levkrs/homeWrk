import re
import random

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# Способ 1 (через re)
p = list(filter(None,re.split(r'[A-Z]', line)))
print(p)


#Способ 2 (без re);


index = len(line)

arr_line = list(line)
string = ""
for i, val in enumerate(arr_line):
       if (ord(val) <= 132 and ord(val) >= 101):
              string += val
       else:
              string += "?"
resault = list(filter(None,string.split("?")))
print(resault)

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'



# нужно получить список строк: ['AY', 'NOGI', 'P']


#Решение через re


found = re.findall(r"[a-z]{2}([A-Z]+)[A-Z]{2}", line_2)

print(found)



#Решение без re



def char_lower(int_val):
       if (ord(int_val) >= 97 and ord(int_val) <= 122):
              return True
       else:
              return False

def char_uper(int_val):
       if (ord(int_val) >= 65 and ord(int_val) <= 90):
              return True
       else:
              return False

count = 0

arr_x = []

while count <= (len(line_2) - 3):
       if (char_lower(line_2[count]) == True and char_lower(line_2[count + 1]) == True and char_uper(line_2[count+2]) == True):
              #print("Index = ", count+2)
              x = count+2
              arr_x.append(x)

       count+=1

arr_y = []
count1 = 0
while count1 <= (len(line_2) - 3):
       if (char_uper(line_2[count1]) == True and char_uper(line_2[count1 + 1]) == True and char_lower(line_2[count1+2]) == True):
              #print("Index 2 = ", count1)
              y = count1
              arr_y.append(y)

       count1+=1

res_arr = []
for i, val_x in enumerate(arr_x):
       for j, val_y in enumerate(arr_y):
              if (line_2[val_x:val_y].isupper() == True):
                     #print("x = ", val_x, "y = ", val_y)
                     #print(line_2[val_x:val_y])
                     res_arr.append(line_2[val_x:val_y])
print(res_arr)

#line_2 = "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"





# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

def write_file(str_to_file):
       name_file = input("Введите имя файла ")
       with open(name_file, "w", encoding="utf-8") as f:
              f.write(str_to_file)
       string = str_to_file

       count_while = 0

       arr_res = []

       while count_while <= 9:
              #print("Длинна строки - ", len(string))
              count_int = 0
              max_count = 0
              for val in string:
                     if (int(val) == count_while):
                            count_int += 1
                            if (max_count < count_int):
                                   max_count = count_int
                     else:

                            count_int = 0
              count_while += 1
              arr_res.append(max_count)

       return ("Максимальная последовательность одинаковых цифр у -", arr_res.index(max(arr_res)), " равная =",
             max(arr_res), "повторений")


res_x = ""
count = 1
while count <= 2499:
       x = random.randint(0,9)
       res_x += str(x)
       count+=1


#write_file(res_x)  #Запись сгенерированной строки в файл


print(write_file(res_x))

