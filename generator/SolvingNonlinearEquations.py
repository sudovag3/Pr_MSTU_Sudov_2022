from timeit import default_timer as timer
from generator.simpleIter import simple_iteration
from math import *
import sympy
from sympy import Symbol, diff

EVALX = ''


def cot(x):
    return cos(x) / sin(x)


def function(x, evalx):
    if x == 'x':
        from sympy import sin, cos, log, tan, cot
        x = sympy.symbols('x')
        eq = eval(evalx)
        return eq
    return eval(evalx)


# Метод биссекции
def BisectionMethod(a, b, evalx, eps):
    print("Метод биссекции:")
    start = timer()
    ya = function(a, evalx)
    yb = function(b, evalx)

    while True:
        x0 = (a + b) / 2  # начальное приближение x0
        y = function(x0, evalx)
        if ya * y < 0:  # Выбираем нужный отрезок
            b = x0
            yb = y
        if y * yb < 0:
            a = x0
            ya = y
        if abs(y) < eps:  # условие выхода из цикла |y(x0)| < e
            break
    end = timer()
    result = {
        'result': x0,
        'eq': function('x', evalx),
        'method': 'Метод Биссекции',
        'accuracy': eps,
        'time': end - start
    }
    return result
    print('Приближенное значение корня: x0 = ', x0, ';   |y(x0)| < e: ', y)


# Метод хорд
def ChordMethod(a, b, evalx, eps):
    print("Метод хорд:")
    x = Symbol('x')
    start = timer()
    ddy = diff(diff(function('x', evalx)))  # берем вторую производную по заданной функции

    if (function(a, evalx) * ddy.subs(x, a)) > 0:  # проверяем неподвижность точки a
        x0 = b
        while True:
            x0 = x0 - (function(x0, evalx) * (a - x0)) / (
                        function(a, evalx) - function(x0, evalx))  # вычисляем начальное приближение по заданной формуле
            y = function(x0, evalx)  # значение функции в данной точке
            if abs(y) < eps:  # условие выхода из цикла |y(x0)| < e
                break

    else:  # если точка b неподвижна, то двигается точка a
        x0 = a
        while True:
            x0 = x0 - (function(x0, evalx) * (b - x0)) / (
                        function(b, evalx) - function(x0, evalx))  # вычисляем начальное приближение по заданной формуле
            y = function(x0, evalx)  # значение функции в данной точке
            if abs(y) < eps:  # условие выхода из цикла |y(x0)| < e
                break
    end = timer()
    result = {
        'result': x0,
        'eq': function('x', evalx),
        'method': 'Метод Хорд',
        'accuracy': eps,
        'time': end - start
    }
    return result
    print('Приближенное значение корня: x0 = ', x0, ';   |y(x0)| < e: ', "%f" % abs(y))


# Метод Ньютона
def NewtonsMethod(a, b, evalx, eps):
    print("Метод Ньютона:")
    start = timer()
    x = Symbol('x')
    dy = diff(function('x', evalx))  # берем производную по y
    ddy = diff(diff(function('x', evalx)))  # берем вторую производную по заданной функции
    if (function(a, evalx) * ddy.subs(x, a)) > 0:  # проверяем неподвижность точки a
        x0 = a
        while True:
            x0 = x0 - function(x0, evalx) / eval(
                str(dy.subs(x, x0)))  # вычисляем начальное приближение по заданной формуле
            y = function(x0, evalx)  # значение функции в данной точке
            if abs(y) < eps:  # условие выхода из цикла |y(x0)| < e
                break

    else:  # проверяем неподвижность точки b
        x0 = b
        while True:
            x0 = x0 - function(x0, evalx) / dy.subs(x, x0)  # вычисляем начальное приближение по заданной формуле
            y = function(x0, evalx)  # значение функции в данной точке
            if abs(y) < eps:  # условие выхода из цикла |y(x0)| < e
                break
    end = timer()
    result = {
        'result': x0,
        'eq': function('x', evalx),
        'method': 'Метод Ньютона',
        'accuracy': eps,
        'time': end - start
    }
    return result
    print('Приближенное значение корня: x0 = ', x0, ';   |y(x0)| < e: ', '%0.15f' % y)


# Метод простой итерации
def SimpleIterationMethod(evalx, eps, x0):
    EVALX = evalx

    def function(x, fi=False):
        if fi == True:
            return eval(EVALX + "+ x")
        if x == 'x':
            from sympy import sin, cos, log, tan, cot
            x = sympy.symbols('x')
            return eval(EVALX)
        return eval(EVALX)

    print('Метод простой итерации:')
    res = simple_iteration(function, eps, x0)
    res['evalx'] = EVALX
    EVALX = ''
    return res
