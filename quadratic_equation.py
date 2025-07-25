import math

a = 10
b = 20
c = 30

quadratic_equation = f'{a}x^2 + {b}x + {c}'
print(f'quadratic_equation is {quadratic_equation}')

print('solution of quadratic equation is: ')

discriminant = b**2 - 4 * a * c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant))/ 2 * a
    root2 = (-b - math.sqrt(discriminant)) / 2 * a
    print(f'Root 1 : {root1}')
    print(f'Root 2 : {root2}')
elif discriminant == 0:
    root1 = -b / 2 * a
    print(f'Root is ; {root1}')
else:
    real_part = -b / 2 * a
    imaginary_part = math.sqrt(abs(discriminant)) / 2 * a
    print(f'Root 1 : {real_part} + {imaginary_part}i')
    print(f'Root 2: {real_part} - {imaginary_part}i')
