"""
https://contest.yandex.ru/contest/23389/problems/L/
L. Лишняя буква
Ограничение времени	1 секунда
Ограничение памяти	64Mb

Васе очень нравятся задачи про строки, поэтому он придумал свою. Есть 2
строки s и t, состоящие только из строчных букв. Строка t получена
перемешиванием букв строки s и добавлением 1 буквы в случайную позицию.
Нужно найти добавленную букву.

Формат ввода
На вход подаются строки s и t, разделенные переносом строки. Длины строк не
превосходят 1000 символов. Строки не бывают пустыми.

Формат вывода
Выведите лишнюю букву.

Пример 1
Ввод
abcd
abcde
Вывод
e

Пример 2
Ввод
go
ogg
Вывод
g

Пример 3
Ввод
xtkpx
xkctpx
Вывод
c

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
            while n < 4:
                if n == 1:
                    line1 = line.replace('\n', '')
                    n += 1
                    break
                elif n == 2:
                    line2 = line.replace('\n', '')
                    n += 1
                    break
                elif n == 3:
                    answer = line.replace('\n', '')
                    logger.debug(f'{line1} | {line2} = {answer}')

                    line1 = {f'{item}': line1.count(item) for item in line1}
                    logger.debug(line1)
                    line2 = {f'{item}': line2.count(item) for item in line2}
                    logger.debug(line2)

                    set1 = set(line1.keys())
                    set2 = set(line2.keys())
                    uncommon_keys = set2 - set1
                    logger.debug(uncommon_keys)
                    res = list(uncommon_keys)
                    if not uncommon_keys:
                        common_keys = set1.intersection(set2)
                        result = {k: line2[k] - line1[k] for k in common_keys
                                  if (line2[k] - line1[k]) != 0}
                        logger.debug(result)
                        res = list(result.keys())[0]
                        logger.debug(f'Ответ: {res}')
                        # print(res)
                        assert answer == res, f'{answer} != {res}'
                    else:
                        logger.debug(f'Ответ: {res[0]}')
                        # print(res[0])
                        assert answer == res[0], f'{answer} != {res[0]}'

                    n = 1
                    break


if __name__ == '__main__':
    run()
