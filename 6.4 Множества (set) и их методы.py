# s = {1, 2, 3, "hello", (1,2,3),}
#
# x = set([1,2,3,4,5,1])
# print(x)
# y = set("abrakadabra")
# print(y)
# z = set(range(7))
# print(z)
#
# cities = ["Калуга", "Краснодар", "Тюмень", "Ульяновск", "Москва", "Тюмень", "Калуга", "Ульяновск"]
# q = set(cities)
# print(len(q))
# print("Москва" in q)
#
# q.add(7)
# print(q)
# q.update(["a","b",(1,2)]) # можно указывать любой итерируемый объект
# print(q)
# q.discard(7) # не возвращает ошибок для не существующих элементов
# print(q)
# q.remove('b') # возвращает
# print(q)
# q.pop() # удаляет произвольный элемент
# print(q)
# q.clear() # очищение множества
# print(q)

# Вводятся вещественные числа в одну строчку через пробел. Необходимо на их основе сформировать множество s.
# Подсказка: множество можно создать по аналогии со списком:
# list(map(float, <список из строк чисел>))
# Вывести на экран значения множества s в порядке возрастания в одну строчку через пробел, используя команду:
# print(*sorted(s))
# P. S. О функции sorted мы еще будем говорить, а также об операторе *.
# Пока просто запомните такую возможность сортировки и вывода произвольных коллекций на экран.
# nums = set(map(float, input().split()))
# print(*sorted(nums))

# Вводится текст в одну строку, слова разделены пробелом. Необходимо подсчитать число уникальных слов
# (без учета регистра) в этом тексте. Результат (число уникальных слов) вывести на экран.
# text = set(input().lower().split())
# print(len(text))

# Вводится строка, содержащая латинские символы, пробелы и цифры. Необходимо выделить из нее все неповторяющиеся цифры
# (символы от 0 до 9) и вывести на экран в одну строку через пробел их в порядке возрастания значений.
# Если цифры отсутствуют, то вывести слово НЕТ.
# text = list(input())
#
# x = []
# for i in text:
#     if i.isdigit():
#         x.append(i)
#
# if len(x) == 0:
#     print("НЕТ")
#
# x = set(x)
# print(*sorted(x))

# В ночном клубе фиксируется список гостей. Причем гости могут выходить из помещения, а затем, снова заходить.
# Тогда их имена фиксируются повторно. На вход программы поступает такой список (каждое имя записано с новой строки).
# Требуется подсчитать общее число гостей, которые посетили ночной клуб. Полагается, что гости имеют уникальные имена.
# На экран вывести общее число гостей клуба.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# x = set(lst_in)
# print(len(x))

# В аккаунте youtube Сергея прокомментировали очередное видео. Некоторые посетители оставляли несколько комментариев.
# Требуется по списку комментариев определить уникальное число комментаторов.
# Комментарии поступают на вход программы в формате:
# имя 1: комментарий 1
# имя 2: комментарий 2
# имя N: комментарий N
# Также полагается, что имена у разных комментаторов не совпадают. Вывести на экран общее число уникальных комментаторов.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# import sys

# считывание списка из входного потока
# lst_in = ['EvgeniyK: спасибо большое!',
# 'LinaTroshka: лайк и подписка!',
# 'Sergey Karandeev: крутое видео!',
# 'Евгений Соснин: обожаю',
# 'EvgeniyK: это повтор?',
# 'Sergey Karandeev: нет, это новое видео']
#
# print(len(set([i.split(':')[0] for i in lst_in])))

# Пользователь с клавиатуры вводит названия городов, пока не введет букву q. Определить общее уникальное число городов,
# которые вводил пользователь. На экран вывести это число. Из коллекций при реализации программы использовать
# только множества.

# cities2 = set()
# city = input()
#
# while city != "q":
#     cities2.add(city)
#     city = input()
# print(len(cities2))
