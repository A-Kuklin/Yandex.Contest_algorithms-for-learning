"""
D. Хаотичность погоды
Ограничение времени	0.2 секунды
Ограничение памяти	64Mb

Метеорологическая служба вашего города решила исследовать погоду новым
способом. Под температурой воздуха в конкретный день будем понимать
максимальную температуру в этот день. Назовём хаотичностью погоды за n дней
количество дней, в которые температура строго больше, чем в день до (если
такой существует) и в день после текущего (если такой существует). Например,
если за 5 дней максимальная температура воздуха составляла [1, 2, 5, 4,
8] градусов, то хаотичность за этот период равна 2: в 3-й и 5-й дни
выполнялись описанные условия. Определите по ежедневным показаниям
температуры хаотичность погоды за этот период.

Формат ввода
В первой строке дано число n –— длина периода измерений в днях,
1 ≤ n≤ 105. Во второй строке даны n целых чисел –— значения температуры в
каждый из n дней. Значения температуры не превосходят 273 по модулю.

Формат вывода
Выведите единственное число — хаотичность за данный период.

"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s, %(message)s'))
logger.addHandler(handler)


def run():
    with open('input.txt') as file:
        days = 0
        daily_forecast = []
        for line in file:
            if days == 0:
                days = int(line)
                continue
            line = line.replace('\n', '')
            daily_forecast = list(map(int, line.split()))
        weather_chaos(days, daily_forecast)


def weather_chaos(days, daily_forecast):
    logger.debug(f'Проверка входных данных: {daily_forecast}')
    temp_chaos = 0

    if days == 1:
        temp_chaos = 1
    else:
        for i, temp in enumerate(daily_forecast):
            if i == 0:
                if temp > daily_forecast[1]:
                    temp_chaos += 1
                continue
            if i + 1 == len(daily_forecast):
                if temp > daily_forecast[-2]:
                    temp_chaos += 1
                continue
            if temp > daily_forecast[i-1] and temp > daily_forecast[i+1]:
                temp_chaos += 1
    logger.debug(f'Ответ: {temp_chaos}')
    # print(temp_chaos)


if __name__ == '__main__':
    run()
