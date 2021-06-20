"""
https://contest.yandex.ru/contest/23389/problems/F/
F. Палиндром
Ограничение времени	1 секунда
Ограничение памяти	64Mb

Помогите Васе понять, будет ли фраза палиндромом. Учитываются только буквы
и цифры, заглавные и строчные буквы считаются одинаковыми.
Решение должно работать за O(N), где N — длина строки на входе.

Формат ввода
В единственной строке записана фраза или слово. Буквы могут быть только
латинские.

Формат вывода
Выведите «True», если фраза является палиндромом, и «False», если не является.

Пример 1
Ввод
A man, a plan, a canal: Panama
Вывод
True

Пример 2
Ввод
zo
Вывод
False

"""

import logging
import re

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s, %(message)s'))
logger.addHandler(handler)


def run():
    with open('input.txt') as file:
        for i, line in enumerate(file):
            if not i % 2:
                benchmark = line.replace('\n', '').lower()
                benchmark = re.sub(r'\W', '', benchmark)
                test = benchmark[::-1]
                logger.debug(f'Проверка: {benchmark} | {test}')
                if benchmark == test:
                    boo = 'True'
                    # print('True')
                else:
                    boo = 'False'
                    # print('False')
                logger.debug(f'Ответ: {boo}')
            else:
                answer = line.replace('\n', '')
                assert answer == boo, f'{answer} != {boo}'


if __name__ == '__main__':
    run()
