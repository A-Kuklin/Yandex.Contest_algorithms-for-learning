"""
K. Списочная форма
Ограничение времени	1 секунда
Ограничение памяти	64Mb

Вася просил Аллу помочь решить задачу. На этот раз по информатике.
Для неотрицательного целого числа X списочная форма –— это массив его цифр
слева направо. К примеру, для 1231 списочная форма будет [1,2,3,1]. На вход
подается количество цифр числа Х, списочная форма неотрицательного числа Х и
неотрицательное число K. Числа К и Х не превосходят 10000.
Нужно вернуть списочную форму числа X + K.

Формат ввода
В первой строке — длина списочной формы числа X. На следующей строке — сама
списочная форма с цифрами записанными через пробел.
В последней строке записано число K.

Формат вывода
Выведите списочную форму числа X+K.

"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s, %(message)s'))
logger.addHandler(handler)


def run():
    with open('input.txt') as file:
        n = 1
        for line in file:
            while n < 5:
                if n == 1:
                    length = int(line)
                    n += 1
                    break
                elif n == 2:
                    digit1 = line.replace('\n', '')
                    n += 1
                    break
                elif n == 3:
                    digit2 = int(line)
                    n += 1
                    break
                elif n == 4:
                    answer = line.replace('\n', '')
                    logger.debug(f'{length} | {digit1} + {digit2} = {answer}')

                    digit1 = int(digit1.replace(' ', ''))
                    res = digit1 + digit2
                    res = str(res)
                    logger.debug(res)
                    res = [''.join(f'{item}') for item in res]
                    logger.debug(res)
                    res = ' '.join(map(str, res))
                    logger.debug(f'Ответ: {res}')

                    assert answer == res, f'{answer} != {res}'
                    # print(res)

                    n = 1
                    break


if __name__ == '__main__':
    run()
