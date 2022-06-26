import math

def side_full_square_cylinder(radius, height):
    side = (2 * math.pi) * radius * height
    full = side + 2 * (math.pi * radius ** 2)

    return side, full

radius = float(input('Введите радиус: '))
height = float(input('Введите высоту: '))

side, full = side_full_square_cylinder(radius, height)

print(side)
print(full)