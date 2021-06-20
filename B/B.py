"""
https://contest.yandex.ru/contest/23389/problems/B/
B. Чётные и нечётные числа
Ограничение времени	0.15 секунд
Ограничение памяти	64Mb

Алла придумала такую онлайн-игру: игрок нажимает на кнопку, и на экране
появляются три случайных числа. Если все три числа оказываются одной
чётности, игрок выигрывает.
Напишите программу, которая по трём числам определяет, выиграл игрок или нет.

Формат ввода
В первой строке записаны три случайных целых числа a, b и c.
Числа не превосходят 109 по модулю.

Формат вывода
Выведите «WIN», если игрок выиграл, и «FAIL» в противном случае.

Пример 1
Ввод
1 2 -3
Вывод
FAIL

Пример 2
Ввод
7 11 7
Вывод
WIN

Пример 3
Ввод
6 -2 0
Вывод
WIN

"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s, %(message)s'))
logger.addHandler(handler)


def even_uneven(a, b, c):
    logger.debug(f'Проверка входных данных: {a}, {b}, {c}')
    if ((a % 2, b % 2, c % 2) == (0, 0, 0)
            or (a % 2 != 0 and b % 2 != 0 and c % 2 != 0)):
        logger.debug('Ответ: WIN')
        return 'WIN'
    else:
        logger.debug('Ответ: FAIL')
        return 'FAIL'


if __name__ == '__main__':
    with open('input.txt') as file:
        for line in file:
            a, b, c = line.split()
            a = int(a)
            b = int(b)
            c = int(c)
            print(even_uneven(a, b, c))
