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

student_list = []
teacherlist = []


classList = {}



class Student:
    def __init__(self, name, classN, f_parents, m_parents):
        self.nameSt = name
        self.classSt = classN
        self.f_parentsSt = f_parents
        self.m_parentsSt = m_parents
        if (classList.get(classN) == None):
            classList[classN] = classN
            print("Create Class N")
        else: pass
        st = [self.nameSt, self.classSt, self.f_parentsSt, self.m_parentsSt]
        student_list.append(st)






class Teacher:
    def __init__(self, name, classT, subj):
        self.name = name
        self.classT = classT
        self.subj = subj
        th = [self.name, self.classT, self.subj]
        





st1 = Student("Костиков Виктор Викторович", "6A", "Костиков Виктор Петрович", "Костикова Дарья Юрьевна")
st2 = Student("Жучара М. И.", "6Б", "Жучара Иван Мизайлович ", "Жучара Регина Михайловна")

print(classList)
print(student_list)


def print_class_n():
    list_class = list(classList)
    print(list_class)

def print_parent():
    pass

# print_class_n()
#
# th1 = Teacher("Татьяна Владимировна Мурашкина", "9A", "Английский")
# th2 = Teacher("Вера Ильинишна Цыбулька", "5В", "Русский")
# th3 = Teacher("Галина Добрый Вечер", "5А", "Русский")
# th4 = Teacher("Виктор Срегеевич Копай", "5В", "Математика")
# print(teacher_arr[0])




