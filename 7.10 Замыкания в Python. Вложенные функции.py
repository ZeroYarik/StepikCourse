# def say_name(name):
#     def say_goodbye():
#         print("Dont say me goodbye " + name + "!")
#
#     return say_goodbye
#
#
# f = say_name("yaroslav")
# f()


# def counter(start=0):
#     def step():
#         nonlocal start
#         start += 1
#         return start
#
#     return step
#
# c1 = counter(10)
# c2 = counter()
# print(c1(), c2())
# print(c1(), c2())
# print(c1(), c2())


# def strip_string(strip_chars=" "):
#     def do_strip(string):
#         return string.strip(strip_chars)
#
#     return do_strip
#
#
# strip1 = strip_string()
#
# print(strip1(" Hello     "))


# Используя замыкания функций, определите вложенную функцию, которая бы увеличивала значение переданного параметра на 5
# и возвращала бы вычисленный результат. При этом внешняя функция должна иметь следующую сигнатуру:
# def counter_add(): ...
# Вызовите функцию counter_add и результат ее работы присвойте переменной с именем cnt. Вызовите внутреннюю функцию
# через переменную cnt со значением k, введенным с клавиатуры:
# k = int(input())
# Выведите результат на экран.
# def counter_add(k):
#     def add_five():
#         global k
#         k += 5
#         return k
#
#     return add_five
#
#
# k = int(input())
#
# cnt = counter_add(k)
#
# print(cnt())


# Используя замыкания функций, объявите внутреннюю функцию, которая увеличивает значение своего аргумента на некоторую
# величину n - параметр внешней функции с сигнатурой:
# def counter_add(n): ...
# Вызовите внешнюю функцию counter_add со значением аргумента 2 и результат присвойте переменной cnt.
# Вызовите внутреннюю функцию через переменную cnt со значением k, введенным с клавиатуры:
# k = int(input())
# Выведите результат на экран.
# def counter_add(n):
#     def add_smth(k):
#         k += n
#         return k
#     return add_smth
#
# k = int(input())
#
# cnt = counter_add(2)
# print(cnt(k))


#  Используя замыкания функций, объявите внутреннюю функцию, которая заключает в тег h1 строку s
#  (s - строка, параметр внутренней функции). Далее, на вход программы поступает строка и ее нужно поместить в тег
#  h1 с помощью реализованного замыкания. Результат выведите на экран.
# P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
# def add_tag(t1, t2):
#     def do_tag(s):
#         return t1 + s + t2
#     return do_tag
#
# s = "y"
#
# c = add_tag("</h1>", "<h>")
# print(c(s))

# Используя замыкания функций, объявите внутреннюю функцию, которая заключает строку s
# (s - строка, параметр внутренней функции) в произвольный тег, содержащийся в переменной tag - параметре внешней функции.
# Далее, на вход программы поступают две строки: первая с тегом, вторая с некоторым содержимым.
# Вторую строку нужно поместить в тег из первой строки с помощью реализованного замыкания. Результат выведите на экран.
# P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
# def add_tag(t):
#     def do_tag(s):
#         return f"<{t}>{s}</{t}>"
#
#     return do_tag
#
#
# t = input()
# s = input()
#
# c = add_tag(t)
# print(c(s))


# Используя замыкания функций, объявите внутреннюю функцию, которая преобразует строку из списка целых чисел,
# записанных через пробел, либо в список, либо в кортеж. Тип коллекции определяется параметром tp внешней функции.
# Если tp = 'list', то используется список, иначе (при другом значении) - кортеж.
# Далее, на вход программы поступают две строки: первая - это значение для параметра tp; вторая - список целых чисел,
# записанных через пробел. С помощью реализованного замыкания преобразовать эти данные в соответствующую коллекцию.
# Результат вывести на экран командой (lst - ссылка на коллекцию):
# print(lst)
# def transform():
#     def do_it(tp):
#         if tp == 'list':
#             return list(nums)
#         else:
#             return tuple(nums)
#
#     return do_it
#
#
# tp = input()
# nums = map(int, input().split())
#
# lst = transform()
#
# print(lst(tp))
