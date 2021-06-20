"""
https://contest.yandex.ru/contest/23389/problems/G/
G. Работа из дома
Ограничение времени	1 секунда
Ограничение памяти	64Mb

Вася реализовал функцию, которая переводит целое число из десятичной системы
в двоичную. Но, кажется, она получилась не очень оптимальной.
Попробуйте написать более эффективную программу. Не используйте встроенные
средства языка по переводу чисел в бинарное представление.

Формат ввода
На вход подаётся целое число в диапазоне от 0 до 10000.

Формат вывода
Выведите двоичное представление этого числа.

Пример 1
Ввод
5
Вывод
101

Пример 2
Ввод
14
Вывод
1110

"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s, %(message)s'))
logger.addHandler(handler)


def run():
    with open('input.txt') as file:
        for i, line in enumerate(file):
            if not i % 2:
                digit = int(line)
                test = digit
                digit2 = ''
                while digit > 0:
                    digit2 = str(digit % 2) + digit2
                    digit = digit // 2
                logger.debug(f'Входные данные: {test}\n'
                             f'Проверка: {digit2}')
            else:
                answer = line.replace('\n', '')
                assert answer == digit2, f'{answer} != {digit2}'
                logger.debug(f'Ответ: {digit2}')
            # print(digit2)


if __name__ == '__main__':
    run()
