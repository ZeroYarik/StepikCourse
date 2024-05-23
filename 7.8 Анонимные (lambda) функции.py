# x = lambda a, b: a + b
#
# # внутри лямбда функций нельщя использовать оператор присваивания
# # должны быть записаны в одну строчку
# # можно использовать только одну операцию внутри
#
# print(x(2,5))


# Объявите анонимную (лямбда) функцию с одним параметром для возведения числа в квадрат.
# Присвойте эту функцию переменной get_sq.
# Вызывать функцию не нужно, только задать.
# n = int(input())
# get_sq = lambda n: n * n
# print(get_sq(n))

# Объявите анонимную (лямбда) функцию с двумя параметрами для деления одного целого числа на другое.
# Если происходит деление на ноль, то функция должна возвращать значение None, иначе - результат деления.
# Присвойте эту функцию переменной get_div. Вызывать функцию не нужно, только задать.
# x = int(input())
# y = int(input())
# get_div = lambda x, y: None if x == 0 or y == 0 else x / y
# print(get_div(x, y))

# Объявите анонимную (лямбда) функцию для вычисления модуля числа
# (то есть, отрицательные числа нужно делать положительными). Вызовите эту функцию для введенного числа x:
# x = float(input())
# Отобразите результат работы функции на экране.
# x = float(input())
# get_abs = lambda x: abs(x)
# print(get_abs(x))

# Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "ra".
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.
# Вызовите эту функцию для введенной строки s:
# s = input()
# Отобразите результат работы функции на экране.
# s = input()
# get_frag = lambda s: True if 'ra' in s else False
# print(get_frag(s))

# В программе задана функция filter_lst (см. программу ниже), которая отбирает элементы,
# переданного ей итерируемого объекта и возвращает сформированный кортеж значений.
# На вход программы поступает список целых чисел, записанных в одну строчку через пробел.
# Вызовите функцию filter_lst для формирования:
# - кортежа из всех значений входного списка (передается в параметр it);
# - кортежа только из отрицательных чисел;
# - кортежа только из неотрицательных чисел (то есть, включая и 0);
# - кортежа из чисел в диапазоне [3; 5]
# Каждый результат работы функции следует отображать с новой строки командой:
# print(*lst)
# где lst - список на возвращенный функцией filter_lst. Для отбора нужных значений формальному параметру key следует
# передавать соответствующие определения анонимной функции.
# def filter_lst(it, key=None):
#     if key is None:
#         return tuple(it)
#
#     res = ()
#     for x in it:
#         if key(x):
#             res += (x,)
#
#     return res
#
# it = list(map(int, input().split()))
# print(*filter_lst(it))
# print(*filter_lst(it, lambda x: x < 0))
# print(*filter_lst(it, lambda x: x >= 0))
# print(*filter_lst(it, lambda x: 3 <= x <= 5))

