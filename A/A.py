"""
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

"""


import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s, %(message)s'))
logger.addHandler(handler)


def run():
    with open('input.txt') as file:
        for line in file:
            a, x, b, c = line.split()
            a = int(a)
            x = int(x)
            b = int(b)
            c = int(c)
            quadratic_equation(a, x, b, c)


def quadratic_equation(a, x, b, c):
    logger.debug(f'Проверка входных данных: {a}, {x}, {b}, {c}')
    y = a*x*x + b*x + c
    logger.debug(f'Ответ: {y}')
    # print(y)


if __name__ == '__main__':
    run()
