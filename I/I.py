"""
I. Степень четырёх
Ограничение времени	1 секунда
Ограничение памяти	64Mb

Вася на уроке математики изучил степени. Теперь он хочет написать программу,
которая определяет, будет ли положительное целое число степенью четвёрки.

Формат ввода
На вход подаётся целое число в диапазоне от 1 до 10000.

Формат вывода
Выведите «True», если число является степенью четырёх, «False» –— в обратном
случае.

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
                boo = ''
                digit = int(line)
                test = digit
                while test != 1:
                    if (test % 4) != 0:
                        boo = 'False'
                        break
                    test = test // 4
                if boo != 'False':
                    boo = 'True'
                logger.debug(f'{digit} | {boo}')
            else:
                answer = line.replace('\n', '')
                assert answer == boo, f'{answer} != {boo}'
            # print(boo)


if __name__ == '__main__':
    run()
