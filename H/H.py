"""
H. Двоичная система
Ограничение времени	0.07 секунд
Ограничение памяти	39Mb

Тимофей спросил у Гоши, умеет ли тот работать с числами в двоичной системе
счисления. Он ответил, что проходил это на одной из первых лекций по
информатике. Тимофей предложил Гоше решить задачку. Два числа записаны в
двоичной системе счисления. Нужно вывести их сумму, также в двоичной
системе. Встроенную в язык программирования возможность сложения двоичных
чисел применять нельзя.
Решение должно работать за O(N), где N –— количество разрядов максимального
числа на входе.

Формат ввода
Два числа в двоичной системе счисления, каждое на отдельной строке. Длина
каждого числа не превосходит 10 000 символов.

Формат вывода
Одно число в двоичной системе счисления.

"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s, %(message)s'))
logger.addHandler(handler)


def run():
    with open('input.txt') as file:
        digit1 = ''
        digit2 = ''
        n = 1
        for line in file:
            while n < 4:
                if n == 1:
                    digit1 = line.replace('\n', '')
                    n += 1
                    break
                elif n == 2:
                    digit2 = line.replace('\n', '')
                    n += 1
                    break
                elif n == 3:
                    answer = line.replace('\n', '')
                    logger.debug(f'{digit1} + {digit2} = {answer}')

                    digit1 = digit1[::-1]
                    digit2 = digit2[::-1]
                    digit1 = [*map(int, digit1)]
                    logger.debug(digit1)
                    digit2 = [*map(int, digit2)]
                    size = max(len(digit1), len(digit2))
                    digit1 += [0] * (size - len(digit1))
                    digit2 += [0] * (size - len(digit2))
                    overflow = 0
                    res = []
                    for obj in zip(digit1, digit2):
                        value = obj[0] + obj[1] + overflow
                        overflow = value // 2
                        res.append(value % 2)
                    if overflow == 1:
                        res.append(1)
                    res = res[::-1]
                    res = ''.join(map(str, res))
                    logger.debug(f'Ответ: {res}')
                    assert answer == res, f'{answer} != {res}'
                    # print(res)

                    n = 1
                    break


if __name__ == '__main__':
    run()
