"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна:')
        if self.b + other.b < 0:
            return f'{self.a + other.a} - {0 - self.b + other.b} * i'
        else:
            return f'{self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно:')
        if self.b * other.a > 0:
            return f'{self.a * other.a - self.b * other.b} - {self.b * other.a} * i'
        else:
            return f'{self.a * other.a - self.b * other.b} + {0 - self.b * other.a} * i'

    def __str__(self):
        return f'{self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(f'z_1 = {z_1}\nz_2 = {z_2}')
print(z_1 + z_2)
print(z_1 * z_2)
