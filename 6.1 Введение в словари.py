# d = {"house": "дом", "car": "машина",
#      "tree": "дерево", "road": "дорога",
#      "river": "река"}
#
#
# if "house" in d and "car" in d and "road" in d:
#     print("YES")
# else:
#     print("NO")

#
# my_dict = dict(one=1, two=2, three='3',four='4', five=5)
# print(my_dict)
#
# lst = [[2, "неуд"], [3, "удовл"], [4, "хорошо"], [5, "отлично"]]
# print(lst)

# d = {}
# d[True] = "Истина"
# print(d)
# d[False] = "Ложь"
# print(d)
# d = {True: 1, False: "Ложь", 'list': [1, 2, 3], 5: 5} # ключами могут быть только неизменяемые типы данных
# print(d)
# print(len(d))
# del d[True]
# print(d)
# print("abc" in d) # проверка проверяет ключи но не значения
# print(False in d)
# print("abc" not in d) # обратная проверка
# d = dict([[1,'one'], [2,'two']], five5='five', '8'='eight')
# print(d)
# house = "house"
# d = {house:'дом'}
# print(d)

# Вводятся данные в формате ключ=значение в одну строчку через пробел. Значениями здесь являются целые числа
# (см. пример ниже). Необходимо на их основе создать словарь d с помощью функции dict() и вывести его на экран командой:
# nums = input().split()
# lst = [nums[x].split('=') for x in range(len(nums))]
# d = dict(lst)
# for key in d:
#     d[key] = int(d[key])
#
# print(*sorted(d.items()))

# На вход программы поступают данные в виде набора строк в формате:
# ключ1=значение1
# ключ2=значение2
# ключN=значениеN
# Ключами здесь выступают целые числа (см. пример ниже). Необходимо их преобразовать в словарь d
# (без использования функции dict()) и вывести его на экран командой:
# print(*sorted(d.items()))
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
# d = {}
# for i in lst_in:
#     row = i.split('=')
#     d[int(row[0])] = row[1]
#
# print(*sorted(d.items()))

# Вводятся данные в формате ключ=значение в одну строчку через пробел. Необходимо на их основе создать словарь,
# затем проверить, существуют ли в нем ключи со значениями: 'house', 'True' и '5' (все ключи - строки).
# Если все они существуют, то вывести на экран ДА, иначе - НЕТ.
# nums = input().split()
# lst = [nums[x].split('=') for x in range(len(nums))]
# d = dict(lst)
#
# print(d)
# if 'house' in d and "True" in d and '5' in d:
#     print("ДА")
# else:
#     print("НЕТ")

# Вводятся данные в формате ключ=значение в одну строчку через пробел.
# Необходимо на их основе создать словарь d, затем удалить из этого словаря ключи 'False' и '3', если они существуют.
# Ключами и значениями словаря являются строки. Вывести полученный словарь на экран командой:
# print(*sorted(d.items()))
# l = input().split()
# lst = [l[x].split('=') for x in range(len(l))]
# dict_my = dict(lst)

# if 'False' in dict_my:
#     del dict_my['False']
# if '3' in dict_my:
#     del dict_my['3']
# print(*sorted(dict_my.items()))

# Вводятся номера телефонов в одну строчку через пробел с разными кодами стран: +7, +6, +2, +4 и т.д.
# Необходимо составить словарь d, где ключи - это коды +7, +6, +2 и т.п., а значения - список номеров
# (следующих в том же порядке, что и во входной строке) с соответствующими кодами. Полученный словарь вывести командой:
# print(*sorted(d.items()))
# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
# nums = input().split()
# lst = nums
#
# d = {}
# for i in lst:
#     kod = i[:2]
#     if kod not in d:
#         d[kod] = []
#     if kod in d:
#         d[kod].append(i)
#
# print(*sorted(d.items()))

# Вводятся номера телефонов в формате:
# номер_1 имя_1
# номер_2 имя_2
# номер_N имя_N
# Необходимо создать словарь d, где ключами будут имена, а значениями - список номеров телефонов для этого имени.
# Обратите внимание, что одному имени может принадлежать несколько разных номеров. Полученный словарь вывести командой:
# print(*sorted(d.items()))
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# +71234567890 Сергей
# +71234567810 Сергей
# +51234567890 Михаил
# +72134567890 Николай

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# d = {}
#
# for i, j in enumerate(lst_in):
#     name = j[13:]
#     number = j[:12]
#     if name not in d:
#         d[name] = []
#     if name in d:
#         d[name].append(number)
# print(*sorted(d.items()))

# Пользователь вводит в цикле целые положительные числа, пока не введет число 0. Д
# ля каждого числа вычисляется квадратный корень (с точностью до сотых) и значение выводится на экран (в столбик).
# С помощью словаря выполните кэширование данных так, чтобы при повторном вводе того же самого числа результат
# не вычислялся, а бралось ранее вычисленное значение из словаря. При этом на экране должно выводиться:
# значение из кэша: <число>
# import math
# d = {}
#
# while True:
#     my_num = int(input())
#     if my_num == 0:
#         break
#     if my_num not in d:
#
#         d[my_num] = round(math.sqrt(my_num), 2)
#
#         print(f'{d[my_num]}')
#
#     else:
#         print(f"значение из кэша: {d[my_num]}")

#  Тестовый веб-сервер возвращает HTML-страницы по URL-адресам (строкам). На вход программы поступают различные
#  URL-адреса. Если адрес пришел впервые, то на экране отобразить строку (без кавычек):
# "HTML-страница для адреса <URL-адрес>"
# Если адрес приходит повторно, то следует взять строку "HTML-страница для адреса <URL-адрес>" из словаря и вывести
# на экран сообщение (без кавычек):
# "Взято из кэша: HTML-страница для адреса <URL-адрес>"
# Сообщения выводить каждое с новой строки.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# import sys
#
# # считывание списка из входного потока
# my_url = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
# d = {}
#
# for i in my_url:
#     if i not in d:
#         d[i] = [i]
#         print('HTML-страница для адреса', *d[i])
#     else:
#         print('Взято из кэша: HTML-страница для адреса', *d[i])

