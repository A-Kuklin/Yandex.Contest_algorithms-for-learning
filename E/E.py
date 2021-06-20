"""
https://contest.yandex.ru/contest/23389/problems/E/
E. Самое длинное слово
Ограничение времени	1 секунда
Ограничение памяти	64Mb

Чтобы подготовиться к семинару, Гоше надо прочитать статью по эффективному
менеджменту. Так как Гоша хочет спланировать день заранее, ему необходимо
оценить сложность статьи.
Он придумал такой метод оценки: берётся случайное предложение из текста и в
нём ищется самое длинное слово. Его длина и будет условной сложностью статьи.
Помогите Гоше справиться с этой задачей.

Формат ввода
В первой строке дана длина текста L (L ≤ 105).
В единственной строке записан текст, состоящий из строчных латинских букв и
пробелов. Слово —– последовательность букв, не разделённых пробелами.
Пробелы могут стоять в самом начале строки и в самом её конце.

Формат вывода
В первой строке выведите самое длинное слово. Во второй строке
выведите его длину. Если подходящих слов несколько, выведите то, которое
встречается раньше.

Пример 1
Ввод
19
i love segment tree
Вывод
segment
7

Пример 2
Ввод
21
frog jumps from river
Вывод
jumps
5

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
        words = 0
        for i, line in enumerate(file):
            if words == 0:
                words = int(line)
                continue
            if not i % 4:
                if words == 0:
                    words = int(line)
                    continue
            elif re.findall('>>', line):
                line = line.replace('\n', '')
                answer_word = line.replace('>> ', '')
            elif re.findall('<<', line):
                line = line.replace('\n', '')
                line = line.replace('<< ', '')
                answer_number = int(line)
                sophistication(answer_word, answer_number, text, words)
                words = 0
            else:
                text = line.replace('\n', '')


# def sophistication(text, words):
def sophistication(answer_word, answer_number, text, words):
    logger.debug(f'Проверка входных данных: <_{text}_>\n'
                 f'слово: {answer_word},\n'
                 f'его длина: {answer_number}')
    dict_text = [(x, len(x)) for x in text.split()]
    dict_text = dict(dict_text)
    logger.debug(dict_text)
    if words == 0:
        number = 0
        word = ''
    else:
        number = max(dict_text.values())
        word = list(dict_text.keys())[list(dict_text.values()).index(number)]
    assert answer_word == word, f'{answer_word} != {word}'
    assert answer_number == number, f'{answer_number} != {number}'
    logger.debug(f'Ответ: {word}, {number}\n')
    # print(word)
    # print(number)


if __name__ == '__main__':
    run()
