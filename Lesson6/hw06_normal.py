# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.


# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

student_list_arr = []
teacher_list_arr = []
class_list_arr = []


classList = {}



class Student:
    def __init__(self, name,f_parents, m_parents):
        self.nameSt = name
        self.f_parentsSt = f_parents
        self.m_parentsSt = m_parents
        st = [self.nameSt, self.f_parentsSt, self.m_parentsSt]
        student_list_arr.append(st)



class Class_list():
    def __init__(self,name,student_list,teacher_list):
        self.name = name
        self.student_list = student_list
        self.teacher_list = teacher_list
        classList[self.name] = [self.student_list, self.teacher_list]


class Teacher:
    def __init__(self, name, subj):
        self.name = name
        self.subj = subj
        ther = [self.name,self.subj]
        teacher_list_arr.append(ther)









st1 = Student("Костиков Виктор Викторович", "Костиков Виктор Петрович", "Костикова Дарья Юрьевна")
st2 = Student("Жучара М. И.", "Жучара Иван Мизайлович ", "Жучара Регина Михайловна")
th1 = Teacher("Татьяна Владимировна Мурашкина","Английский")

class9a = Class_list("9A", student_list_arr, teacher_list_arr)

stud = class9a
# print(stud.student_list)
print(classList)
print("9A - ", classList.get("9A"))

users = classList.get("9A")
print(users[1])


# print(classList)
# print(student_list)



# print_class_n()
#
# th1 = Teacher("Татьяна Владимировна Мурашкина", "9A", "Английский")
# th2 = Teacher("Вера Ильинишна Цыбулька", "5В", "Русский")
# th3 = Teacher("Галина Добрый Вечер", "5А", "Русский")
# th4 = Teacher("Виктор Срегеевич Копай", "5В", "Математика")
# print(teacher_arr[0])




