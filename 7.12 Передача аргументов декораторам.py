# import math
from functools import wraps
#
# def df_decorator(dx=0.0001):
#     def func_decorator(func):
#         @wraps(func)
#         def wrapper(x, *args, **kwargs):
#             res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
#             return res
#         return wrapper
#     return func_decorator
#
# @df_decorator(dx=0.01)
# def sin_df(x):
#     return math.sin(x)
#
# sin_df = df_decorator(dx=0.001)(sin_df)
# df = sin_df(math.pi/3)
# print(df)


"""Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку в список чисел и
возвращает их сумму.
Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:
s = input()
Результат отобразите на экране."""
# def deco(start=0):
#     def func_deco(func):
#         def wrapper(*args, **kwargs):
#             return start + func(*args, **kwargs)
#         return wrapper
#     return func_deco
#
# @deco(start=5)
# def converse(s):
#     s = list(map(int, s.split()))
#     return sum(s)
#
#
# s = input()
# print(converse(s))

"""Объявите функцию, которая возвращает переданную ей строку в нижнем регистре (с малыми буквами). 
Определите декоратор для этой функции, который имеет один параметр tag, определяющий строку с названием тега и
начальным значением "h1". Этот декоратор должен заключать возвращенную функцией строку в тег tag и возвращать результат.
Пример заключения строки "python" в тег h1: <h1>python</h1>
Примените декоратор со значением tag="div" к функции и вызовите декорированную функцию для введенной строки s:
s = input()
Результат отобразите на экране."""
# def deco(tag='h1'):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             res = f"<{tag}>{func(*args, **kwargs)}</{tag}>"
#             return res
#         return wrapper
#     return decorator
#
#
# @deco(tag='div')
# def return_str(s):
#     return s.lower()
#
#
# s = input()
# print(return_str(s))

"""Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу, используя следующий словарь
 для замены русских букв на соответствующее латинское написание:
Функция должна возвращать преобразованную строку. 
Замены делать без учета регистра (исходную строку перевести в нижний регистр - малые буквы). 
Определите декоратор с параметром chars и начальным значением " !?", который данные символы преобразует в символ "-" и,
 кроме того, все подряд идущие дефисы (например, "--" или "---") приводит к одному дефису. 
 Полученный результат должен возвращаться в виде строки.
Примените декоратор с аргументом chars="?!:;,. " к функции и вызовите декорированную функцию для введенной строки s:
s = input()
Результат отобразите на экране."""
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
#
# def deco(chars="!?"):
#     def decorator(func):
#         def wrapper(s):
#             s = func(s)
#             for c in chars:
#                 s = s.replace(c, '-')
#             while '--' in s:
#                 s = s.replace('--', '-')
#             return s
#
#         return wrapper
#
#     return decorator
#
#
# @deco(chars='?!:;,. ')
# def swap_letters(string):
#     res = [t.get(i, i) for i in string.lower()]
#     return ''.join(res)
#
#
# s = input()
# x = swap_letters(s)
# print(x)

"""Объявите функцию с именем get_list и следующим описанием в теле функции:
'''Функция для формирования списка целых значений'''
Сама функция должна формировать и возвращать список целых чисел, который поступает на ее вход в виде строки из 
целых чисел, записанных через пробел.
Определите декоратор, который выполняет суммирование значений из списка этой функции и возвращает результат.
Внутри декоратора декорируйте переданную функцию get_list с помощью команды @wraps (не забудьте сделать импорт:
 from functools import wraps). Такое декорирование необходимо, чтобы исходная функция get_list сохраняла
  свои локальные свойства: __name__ и __doc__.
Примените декоратор к функции get_list, но не вызывайте ее."""
# def deco(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         s = sum(func(*args, **kwargs))
#         return s
#     return wrapper
#
#
# @deco
# def get_list(*args):
#     '''Функция для формирования списка целых значений'''
#     res = list(map(int, nums.split()))
#     return res
#
#
# nums = input()
# print(get_list(nums))
# print(get_list.__name__)
# print(get_list.__doc__)