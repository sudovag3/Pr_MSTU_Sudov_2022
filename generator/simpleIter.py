import math
from timeit import default_timer as timer

import sympy

logs = []

def check_e(x_list, result, step, E):
    """Проверка рузультата на достижение точности E(кси)"""
    if abs(result - x_list[step]) < E:
        # print('Точность перешла порог E (кси)')
        # print('По формуле: |Xn+1 - Xn|')
        # print('|{next} - {prev}| = {result} <= {E}'.
        #     format(next=result, prev=x_list[step], result=abs(result - x_list[step]), E=E)
        # )
        return True


def show_step(step, current_x, result, function):
    """Показать информацию о текущем шаге"""
    logs.append(f'Шаг №{step} при X{step} = {current_x} По формуле '
          f'{function("x")} = {result} \n')
    # print(f'Шаг №{step} при X{step} = {current_x} По формуле '
    #       f'{function("x")} = {result}')


def simple_iteration(function, E, x0):
    """
    Цикл вычислений и проверок
    """
    start = timer()
    # Получаем данные от пользователя
    x_list = [x0]
    max_step = 100
    global logs

    for step in range(max_step):
        current_x = x_list[step]
        result = function(current_x)
        show_step(step, current_x, result, function)
        x_list.append(result)
        if len(x_list) > 1 and check_e(x_list=x_list, result=result, step=step, E=E):
            end = timer()
            result = {
                'result': x_list[-1],
                'method': 'Метод простой итерации',
                'accuracy': E,
                'time': end - start,
                'logs': logs
            }
            logs = []
            return result
    else:
        print('Метод простой итерации не сошелся')

def function(x):
    """Функция для вычислений"""
    return math.sin(x) + x**2

if __name__ == '__main__':

    simple_iteration(function)