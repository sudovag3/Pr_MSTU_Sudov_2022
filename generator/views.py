from django.shortcuts import render
from django.http import HttpResponse
from .services import generate_password
import generator.SolvingNonlinearEquations as sne
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')

def chord_method_calculator(request):
    return render(request, 'generator/chord_method_calculator.html')

def newton_method_calculator(request):
    return render(request, 'generator/newton_method_calculator.html')

def simple_iteration_method_calculator(request):
    return render(request, 'generator/simple_iteration_method_calculator.html')

def bisection_method_calculator(request):
    return render(request, 'generator/bisection_method_calculator.html')

def check_currency(request):
    return render(request, 'generator/currency.html')

def bisection_method_calculator_result(request):
    validateFields = validate(request.POST.get('eval'), request.POST.get('e'), request.POST.get('a'), request.POST.get('b'))
    if validateFields:
        eval = request.POST.get('eval')
        mode = 1
        e = float(request.POST.get('e'))
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))

        print(validateFields)

        result =  eq_par({'mode':1, 'evalx': eval, 'eps': e, 'a': a, 'b': b})
        print(result)
        return render(request, 'generator/bisection_method_calculator.html', result)
    else:
        return render(request, 'generator/bisection_method_calculator.html', {'error': 'Заполните все поля!'})


def chord_method_calculator_result(request):
    validateFields = validate(request.POST.get('eval'), request.POST.get('e'), request.POST.get('a'), request.POST.get('b'))
    if validateFields:
        eval = request.POST.get('eval')
        mode = 2
        e = float(request.POST.get('e'))
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        validateFields = validate(eval, e, a, b)
        print(validateFields)

        result =  eq_par({'mode':2, 'evalx': eval, 'eps': e, 'a': a, 'b': b})
        print(result)
        return render(request, 'generator/chord_method_calculator.html', result)
    else:
        return render(request, 'generator/bisection_method_calculator.html', {'error': 'Заполните все поля!'})

def newton_method_calculator_result(request):
    validateFields = validate(request.POST.get('eval'), request.POST.get('e'), request.POST.get('a'), request.POST.get('b'))
    if validateFields:
        eval = request.POST.get('eval')
        mode = 3
        e = float(request.POST.get('e'))
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        validateFields = validate(eval, e, a, b)
        print(validateFields)
        result =  eq_par({'mode':3, 'evalx': eval, 'eps': e, 'a': a, 'b': b})
        print(result)
        return render(request, 'generator/newton_method_calculator.html', result)
    else:
        return render(request, 'generator/bisection_method_calculator.html', {'error': 'Заполните все поля!'})

def simple_iteration_method_calculator_result(request):
    validateFields = validate(request.POST.get('eval'), request.POST.get('e'), request.POST.get('x0'))
    if validateFields:
        eval = request.POST.get('eval')
        mode = 4
        e = float(request.POST.get('e'))
        x0 = float(request.POST.get('x0'))
        validateFields = validate(eval, x0)
        print(validateFields)
        result =  eq_par({'mode':4, 'evalx': eval, 'eps': e, 'x0': x0})
        print(result)
        return render(request, 'generator/simple_iteration_method_calculator.html', result)
    else:
        return render(request, 'generator/bisection_method_calculator.html', {'error': 'Заполните все поля!'})

def password(request):

    length = int(request.GET.get('length', 10))
    numbers = request.GET.get('numbers', '')
    uppercase = request.GET.get('uppercase', '')
    special = request.GET.get('special', '')

    gen_password = generate_password(length=length, numbers=numbers, uppercase=uppercase, special=special)
    return render(request, 'generator/password.html', {'password':gen_password})

def eq_par(params):
    result = {}
    if params['mode'] == 1:
        result = sne.BisectionMethod(params['a'], params['b'], params['evalx'], params['eps'])
    elif params['mode'] == 2:
        result = sne.ChordMethod(params['a'], params['b'], params['evalx'], params['eps'])
    elif params['mode'] == 3:
        result = sne.NewtonsMethod(params['a'], params['b'], params['evalx'], params['eps'])
    elif params['mode'] == 4:
        result = sne.SimpleIterationMethod(params['evalx'], params['eps'], params['x0'])
    else:
        result['error'] = 'Метод вычисления указан неправильно указан неправильно'

    return result

def validate(*args):
    for element in args:
        if element == '':
            return False
        return True
