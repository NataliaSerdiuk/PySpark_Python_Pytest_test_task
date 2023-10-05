import math

class Figure:
    def __init__(self):
        pass
    def get_area(self):
        return area

class Circle(Figure):
    def __str__(self, radius):
        self.radius = radius

    def calc_cirсle_area(radius):
        return math.pi * (radius ** 2)

class Triangle(Figure):   #формула Герона
    def __str__(self, ftst_size, sec_size, thrd_size):
        self.x = ftst_size
        self.y = sec_size
        self.z =  thrd_size

        if not (x + y > z and x + z > y and y + z > x):
            raise ValueError('Данная фигура не является треугольником.')

    def calc_triangle_area(x, y, z):
        semi_perimeter = (x + y+ z) / 2
        triangle_area = math.sqrt(
            semi_perimeter * (semi_perimeter - x) * (semi_perimeter - y) * (semi_perimeter - z))
        return triangle_area

    def check_right_triangle(x,y,z):  # Проверка:прямоугольный треугольник, для проверки: 3,4,5 --> True, 3,5,5 -->False
        sides = sorted([x,y,z])
        if sides[0] > 0 and sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            return True
        else:
            return False

class Rectangle(Figure):
    def __str__(self, ftst_size, sec_size):
        self.x = ftst_size
        self.y = sec_size

    def calc_rectangle_area(x, y):
        return x*y


def calc_selection(name: str, *args: float):
    if name.lower() == 'круг':
        return Circle.calc_cirсle_area(*args)
    elif name.lower() == 'треугольник':
        return Triangle.calc_triangle_area(*args)
    elif name.lower() == 'прямоугольник':
        return Rectangle.calc_rectangle_area(*args)
    else:
        raise NotImplementedError('Расчет площади данной фигуры не реализован')

print(Triangle.check_right_triangle(3,4,5))