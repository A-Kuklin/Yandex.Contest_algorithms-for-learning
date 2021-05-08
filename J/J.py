"""
J. Факторизация
Язык	Ограничение времени	Ограничение памяти
Python 3.7.3	0.1 секунда	64Mb

Тимофей готовит доклад ко дню открытых дверей кафедры Теории чисел. Он
собирается рассказать про Основную теорему арифметики. В соответствии с этой
теоремой, любое число раскладывается на произведение простых множителей
единственным образом –— с точностью до их перестановки.
Например, число 8 можно представить как 2 × 2 × 2.
Число 50 –— как 2 × 5 × 5 (или 5 × 5 × 2, или 5 × 2 × 5). Три варианта
отличаются лишь порядком следования множителей.
Разложение числа на простые множители называется факторизацией числа.
Факторизацию в уме делать сложно, поэтому помогите Тимофею написать для
этого программу.

Формат ввода
В единственной строке дано число n (2 ≤ n ≤ 109), которое нужно факторизовать.

Формат вывода
Выведите в порядке неубывания простые множители, на которые раскладывается
число n.

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

                div = 2
                result = []
                while div ** 2 <= test:
                    if test % div == 0:
                        result.append(div)
                        test //= div
                    else:
                        div += 1
                if test > 1:
                    result.append(test)
        # logger.debug(result)
        # result = ' '.join(map(str, result))
        # print(result)
            else:
                answer = line.split()
                answer = [int(item) for item in answer]
                logger.debug(f'{digit} = {answer}')
                logger.debug(f'Ответ: {result}')
                assert answer == result, f'{answer} != {result}'


if __name__ == '__main__':
    run()
