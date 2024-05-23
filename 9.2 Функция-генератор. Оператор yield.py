# def get_list():
#     for x in [1,2,3,4]:
#         yield x
#
#
# a = get_list()
# for i in a:
#     print(i)

# def get_list():
#     for i in range(1, 10):
#         a = range(i, 11)
#         yield sum(a) / len(a)
#
#
# a = get_list()
# print(list(a))


"""На вход программе подается натуральное число N. Оно уже читается в программе командой:
N = int(input())
Объявите в программе функцию-генератор с именем get_sum с сигнатурой:
def get_sum(total): ...
которая бы возвращала текущую сумму чисел последовательности длины total = N в диапазоне целых чисел [1; N]
(включительно). То есть, при вызове get_sum в качестве аргумента передается переменная N.
В результате должны получить следующие результаты работы функции-генератора:
при первом вызове get_sum возвращает сумму 1;
при втором вызове get_sum возвращает сумму чисел 1+2 = 3;
при третьем вызове get_sum возвращает сумму чисел 1+2+3 = 6;
....
для N-го вызова get_sum возвращает сумму
1+2+...+(N−1)+N.
Реализовать функцию-генератор get_sum без использования коллекций. Вызывать ее не нужно, только объявить."""
# N = 5
#
# def get_sum(N):
#     my_sum = 0
#     for i in range(1, N+1):
#         my_sum += i
#         yield my_sum


"""Мы с вами в заданиях несколько раз генерировали последовательность чисел Фибоначчи, которая строится по правилу:
 каждое последующее число равно сумме двух предыдущих. Для разнообразия давайте будем генерировать каждое последующее
  как сумму трех предыдущих чисел. При этом первые три числа равны 1. Получаем такую последовательность:
1, 1, 1, 3, 5, 9, 17, 31, 57, ...
Не знаю, есть ли у нее название, поэтому, в рамках уроков, я скромно назову ее последовательностью Балакирева. 
Итак, на вход программе поступает натуральное число N (N > 5), которое необходимо прочитать и сохранить в переменной.
 Затем (или в начале программы), объявить функцию-генератор с сигнатурой:
def balak_seq(max_len): ...
которая бы возвращала max_len = N первых чисел последовательности Балакирева (включая первые три единицы).
Реализуйте эту функцию без использования коллекций (списков, кортежей, словарей и т.п.). Вызовите ее N раз для получения
 N чисел и выведите полученные числа на экран в одну строчку через пробел."""
# N = int(input())
#
# def balak_seq(max_len):
#     a = b = c = 1
#     for i in range(max_len):
#         yield a
#
#         a,b,c = b,c,a + b + c
#
#
# print(*balak_seq(N))

# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
# import random
# random.seed(1)
# N = int(input())
#
# def get_pswrd(N):
#     yield ''.join(random.choice(chars) for i in range(N))
#
#
# print(''.join(get_pswrd(N)))
# print(''.join(get_pswrd(N)))
# print(''.join(get_pswrd(N)))
# print(''.join(get_pswrd(N)))
# print(''.join(get_pswrd(N)))


# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase
# import random
# random.seed(1)
# indx = random.randint(0, len(chars)-1)
# N = int(input())
#
# def my_gen(max_size):
#     yield ''.join(random.choice(chars) for i in range(max_size)) + "@mail.ru"
#
# print(''.join(my_gen(N)))
# print(''.join(my_gen(N)))
# print(''.join(my_gen(N)))
# print(''.join(my_gen(N)))
# print(''.join(my_gen(N)))


"""Объявите функцию-генератор, которая бы возвращала простые числа. (Простое число - это натуральное число, 
которое делится только на себя и на 1). Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в
 одну строчку через пробел."""
# import sympy
# n = int(input())
# def prime_nums(n):
#     for i in range(2,n+1):
#         if sympy.isprime(i):
#             yield i
#
# a = list(prime_nums(n))
# print(*a[:20])



