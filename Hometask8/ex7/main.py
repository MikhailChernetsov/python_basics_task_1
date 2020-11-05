'''
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и
умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.

'''
class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im > 0:
            return f'{self.re} + {self.im}i'
        else:
            return f'{self.re} - {abs(self.im)}i'

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)


num1 = ComplexNumber(2, 4)
print(num1)

num2 = ComplexNumber(1, -8)
print(num2)

print(f'Сумма чисел ({num1}) и ({num2}) равна ({num1 + num2})')
print(f'Произведение чисел ({num1}) и ({num2}) равно ({num1 * num2})')


