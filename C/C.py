"""
C. Соседи
Ограничение времени	1 секунда
Ограничение памяти	64Mb

Дана матрица. Нужно написать функцию, которая для элемента возвращает всех
его соседей. Соседним считается элемент, находящийся от текущего на одну
ячейку влево, вправо, вверх или вниз. Диагональные элементы соседними не
считаются.

Например, в матрице A:
   0 1 2
0| 1 2 3
1| 0 2 6
2| 7 4 1
3| 2 7 0
соседними элементами для (0, 0) будут 2 и 0. А для (2, 1) –— 1, 2, 7, 7.

Формат ввода
В первой строке задано n — количество строк матрицы. Во второй
— количество столбцов m. Числа m и n не превосходят 1000. В следующих n
строках задана матрица. Элементы матрицы — целые числа, по модулю не
превосходящие 1000. В последних двух строках записаны координаты элемента (
индексация начинается с нуля), соседей которого нужно найти.

Формат вывода
Напечатайте нужные числа в возрастающем порядке через пробел.

"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s, %(message)s'))
logger.addHandler(handler)


def run():
    n = 0
    m = 0
    y = 0
    x = 0
    counter = 0
    array = {}
    with open('input.txt') as file:
        for line in file:
            if n == 0:
                n = int(line)
                continue
            if n != 0 and m == 0:
                m = int(line)
                continue
            counter += 1
            if counter <= n:
                line = line.replace('\n', '')
                array[counter - 1] = list(map(int, line.split()))
                continue
            if y == 0 and counter == (n+1):
                line = line.replace('\n', '')
                y = int(line)
                continue
            line = line.replace('\n', '')
            x = int(line)
        neighbors(n, m, array, y, x)


def neighbors(n, m, array, y, x):
    logger.info(f'Проверка входных данных:\n'
                f'количество строк матрицы: {n},\n'
                f'количество столбцов матрицы: {m},\n'
                f'матрица: {array},\n'
                f'координаты элемента: {y}, {x}')
    neighbors_list = []
    if y > 0:
        neighbors_list.append(array[y - 1][x])
    if y + 1 < n:
        neighbors_list.append(array[y + 1][x])
    if x > 0:
        neighbors_list.append(array[y][x - 1])
    if x + 1 < m:
        neighbors_list.append(array[y][x + 1])
    neighbors_list = sorted(neighbors_list)
    logger.debug(neighbors_list)
    result = ' '.join(map(str, neighbors_list))
    # print(' '.join(map(str, neighbors_list)))
    logger.info(f'Ответ: {result}')


if __name__ == '__main__':
    run()
