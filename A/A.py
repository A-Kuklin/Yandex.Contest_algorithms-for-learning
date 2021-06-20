"""
https://contest.yandex.ru/contest/23389/problems/
A. Значения функции
Ограничение времени	0.2 секунды
Ограничение памяти	64Mb

Вася делает тест по математике: вычисляет значение функций в различных
точках. Стоит отличная погода, и друзья зовут Васю гулять. Но мальчик решил
сначала закончить тест и только после этого идти к друзьям. К сожалению,
Вася пока не умеет программировать. Зато вы умеете. Помогите Васе написать
код функции, вычисляющей y = ax2 + bx + c. Напишите программу, которая будет
по коэффициентам a, b, c и числу x выводить значение функции в точке x.

Формат ввода
На вход через пробел подаются числа a, x, b, c.

Формат вывода
Выведите одно число — значение функции в точке x.

Пример 1
Ввод
-8 -5 -2 7
Вывод
-183

Пример 2
Ввод
8 2 9 -10
Вывод
40

"""


import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s, %(message)s'))
logger.addHandler(handler)


def quadratic_equation(a, x, b, c):
    logger.debug(f'Проверка входных данных: {a}, {x}, {b}, {c}')
    y = a*x*x + b*x + c
    logger.debug(f'Ответ: {y}')
    return y


if __name__ == '__main__':
    with open('input.txt') as file:
        for line in file:
            a, x, b, c = line.split()
            a = int(a)
            x = int(x)
            b = int(b)
            c = int(c)
            print(quadratic_equation(a, x, b, c))
