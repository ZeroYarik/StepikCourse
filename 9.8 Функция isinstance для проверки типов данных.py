"""Объявите в программе функцию с именем get_add следующей сигнатуры:
def get_add(a, b): ...
Функция должна складывать или два числа или две строки (но не число со строкой) и возвращать полученный результат.
 Если сложение не может быть выполнено, то функция возвращает значение None.
Вызывать функцию не нужно, только объявить. Также ничего не нужно выводить на экран.
Подсказка: не забудьте про необходимость различения булевых значений (False, True) от целочисленных."""
# def get_add(a, b):
#     if type(a) in (int, float) and type(b) in (int, float):
#         return a + b
#     elif isinstance(a, str) and isinstance(b, str):
#         return a + b
#     else:
#         return None

"""Объявите в программе функцию с именем get_sum следующей сигнатуры:
def get_sum(it): ...
Функция принимает на входе итерируемый объект (список, строку, кортеж, словарь, множество) и вычисляет сумму только 
целых чисел, взятых из элементов итерируемого объекта. Вычисленная сумма возвращается функцией. 
Если целых чисел нет, то возвращается 0.
Вызывать функцию не нужно, только объявить. Также ничего не нужно выводить на экран.
Примеры входного аргумента функции:
get_sum([1,2,3, "a", True, [4, 5], "c", (4, 5)])
get_sum({5, 6, 7, '8', 5, '4'})
get_sum((10, "f", '33', True, 12))
get_sum(['1', True, False, (1, 23)])
Подсказка: не забудьте про необходимость различения булевых значений (False, True) от целочисленных."""
# def get_sum(it):
#     return sum(x if type(x) == int else 0 for x in it)

"""Объявите в программе функцию с именем get_even_sum следующей сигнатуры:
def get_even_sum(it): ...
Функция принимает на входе итерируемый объект (список, строку, кортеж, словарь, множество) и вычисляет сумму 
только целых четных чисел, взятых из элементов итерируемого объекта. Результат возвращается функцией. 
Если целых чисел нет, то возвращается 0.
Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.
Подсказка: не забудьте про необходимость различения булевых значений (False, True) от целочисленных."""
# def get_even_sum(it):
#     return sum(x if type(x) == int and x % 2 == 0 else 0 for x in it)

""" Объявите в программе функцию с именем get_list_digследующей сигнатуры:
def get_list_dig(lst): ...
Функция должна возвращать список только из числовых значений переданной ей коллекции (список или кортеж).
Вызывать функцию не нужно, только объявить. Также ничего не нужно выводить на экран.
Подсказка: не забудьте про необходимость различения булевых значений (False, True) от целочисленных."""
# def get_list_dig(lst):
#     return [x for x in lst if type(x) in (int, float)]
