import math


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# При условии что A - C основание


"""

class Triangle:
    def __init__(self, a1,b1,c1):
        self.ax = a1[0]
        self.ay = a1[1]
        self.bx = b1[0]
        self.by = b1[1]
        self.cx = c1[0]
        self.cy = c1[1]


    def print_coords(self):
        print("ax = ", self.ax, "ay ", self.ay, "bx = ", self.bx, "by ", self.by,"cx = ", self.cx, "cy ", self.cy, )




    def s_size(self):

        self.ab = round(abs(math.sqrt((self.bx - self.ax)**2 + (self.by - self.ay)**2)))
        self.ac = round(abs(math.sqrt((self.cx - self.ax) ** 2 + (self.cy - self.ay) ** 2)))
        self.bc = round(abs(math.sqrt((self.cx - self.bx) ** 2 + (self.cy - self.by) ** 2)))
        self.s = round(1/2*(self.ab + self.ac + self.bc))

        print("ab = ", self.ab, "ac = ", self.ac, "bc = ", self.bc)
        print("Площадь = ", self.s)
        return self.s

    def pr_size(self):
        self.ab = round(abs(math.sqrt((self.bx - self.ax) ** 2 + (self.by - self.ay) ** 2)))
        self.ac = round(abs(math.sqrt((self.cx - self.ax) ** 2 + (self.cy - self.ay) ** 2)))
        self.bc = round(abs(math.sqrt((self.cx - self.bx) ** 2 + (self.cy - self.by) ** 2)))

        self.pr = self.ab + self.bc + self.bc

        print("Периметр = ", self.pr)

    def h_size(self):

        self.h = (2 * self.s_size()) / 2
        print("h = ", self.h)









a1 = [3,2]
b1 = [4,4]
c1 = [5, 2]

tr = Triangle(a1,b1,c1)


tr.s_size()
tr.pr_size()
tr.h_size()

"""

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezoid:
    def __init__(self, a,b,c,d):
        self.ax = a[0]
        self.ay = a[1]
        self.bx = b[0]
        self.by = b[1]
        self.cx = c[0]
        self.cy = c[1]
        self.dx = d[0]
        self.dy = d[1]

    def print_coords(self):
        print("ax = ", self.ax, "ay ", self.ay, "bx = ", self.bx, "by ", self.by, "cx = ", self.cx, "cy ", self.cy, "dx = ", self.dx, "dy ", self.dy )


    def trapez_true(self):
        self.diagAC = round(abs(math.sqrt(((self.cx - self.ax) ** 2) + ((self.cy - self.ay) ** 2))))
        self.diagBD = round(abs(math.sqrt(((self.dx - self.bx) ** 2) + ((self.dy - self.by) ** 2))))
        print("AC = {} BD = {}".format(self.diagAC, self.diagBD))

        if (self.diagAC == self.diagBD):
            return "Трапеция равносторонняя"
        else:
            return "Трапеция не равносторонняя"

    def len_side(self):
        self.lenAB = round(abs(math.sqrt(((self.bx - self.ax) ** 2) + ((self.by - self.ay) ** 2))))
        self.lenBC = round(abs(math.sqrt(((self.cx - self.bx) ** 2) + ((self.cy - self.by) ** 2))))
        self.lenCD = round(abs(math.sqrt(((self.dx - self.cx) ** 2) + ((self.dy - self.cy) ** 2))))
        self.lenDA = round(abs(math.sqrt(((self.dx - self.ax) ** 2) + ((self.dy - self.ay) ** 2))))

        print("Длинна АВ = {}, ВС = {}, СВ = {}, DA = {}".format(self.lenAB, self.lenBC, self.lenCD,  self.lenDA))
        return self.lenAB, self.lenBC, self.lenCD, self.lenDA

    def per_size(self):
        self.per = sum(self.len_side())
        print("Периметр = {}".format(self.per))

    def s_size(self):
        self.s = ((self.len_side()[3] + self.len_side()[1])/2) * math.sqrt( (self.len_side()[0]**2) - ( ((self.len_side()[3] - self.len_side()[1])**2) / 4))
        print("S = {}".format(self.s))

a = [2,2]
b = [4,5]
c = [6,5]
d = [7,3]

tr = Trapezoid(a,b,c,d)

tr.print_coords()

print(tr.trapez_true())

print(tr.len_side())
tr.per_size()
tr.s_size()