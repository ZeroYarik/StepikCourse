""" На вход программе поступает строка с наименованиями рек, записанных через пробел.
Необходимо их прочитать и отсортировать названия рек в порядке убывания их длин строк (названий).
 Результат вывести в одну строчку через пробел."""
# rivers = list(map(str, input().split()))
# rivers.sort(key=len, reverse=True)
# print(*rivers)

"""На вход программе поступают строки в формате:
предмет_1=вес_1
предмет_N=вес_N
Веса предметов заданы целыми числами. В программе уже реализовано их считывание в список lst_in:
lst_in = list(map(str.strip, sys.stdin.readlines()))
Необходимо на основе этих данных сформировать словарь (ключи - названия предметов, значения - вес предметов) и, затем, 
на основе этого словаря сформировать список предметов по убыванию их веса. 
(В списке должны находиться только наименования предметов без их весов).
Отобразить полученный список в виде строки с названиями через пробел."""
# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# d = {s.split('=')[0]: int(s.split('=')[1]) for s in lst_in}
#
# s = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
# print(*s.keys())

"""Известно, что порядок нот следующий: до, ре, ми, фа, соль, ля, си. На вход программе поступает строка с набором
 этих нот, записанных в произвольном порядке через пробел. Необходимо прочитать ноты и сформировать список (с нотами), 
 отсортированными в порядке: до, ре, ми, фа, соль, ля, си.
  Результирующий список нот вывести в одну строчку через пробел."""
# notes = map(str, input().split())
# example = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
# res = sorted(notes, key=lambda x: example.index(x))
# print(*res)

"""Имеется таблица с данными, представленная в формате:
Номер;Имя;Оценка;Зачет
1;Иванов;3;Да
2;Петров;2;Нет
N;Балакирев;4;Да
 В программе уже реализовано их считывание в список lst_in:
lst_in = list(map(str.strip, sys.stdin.readlines()))
Данные этого списка необходимо разбить по разделителю ";" и представить в виде двумерного (вложенного) кортежа в 
формате:
( ('Номер', 'Имя', 'Оценка', 'Зачет'), (1, 'Иванов', 3, 'Да'), (2, 'Петров', 2, 'Нет'), ... )
При этом все числа должны быть представлены как целые числа. Затем, отсортировать этот кортеж так, чтобы столбцы шли
 в порядке:
Имя;Зачет;Оценка;Номер
Реализовать эту операцию с помощью сортировки. Результат должен быть представлен также в виде двумерного кортежа и 
присвоен переменной с именем t_sorted.
Программа ничего не должна выводить на экран, только формировать двумерный кортеж с переменной t_sorted."""
# import sys
#
# # считывание списка из входного потока (не меняйте переменную lst_in в программе)
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# def get_m(lst_in):
#     x = lst_in.split(';')
#
#     if x[0].isdigit():
#         return x[1], x[3], int(x[2]), int(x[0])
#     else:
#         return x[1], x[3], x[2], x[0]
#
#
# t_sorted = tuple([tuple(get_m(i)) for i in lst_in])

"""Известно, что звания военнослужащих имеют следующий порядок (по возрастанию):
рядовой, сержант, старшина, прапорщик, лейтенант, капитан, майор, подполковник, полковник
На вход программе поступают данные о военнослужащих в формате:
имя_1=звание_1
имя_N=звание_N
 В программе уже реализовано их считывание в список lst_in:
lst_in = list(map(str.strip, sys.stdin.readlines()))
Необходимо данные списка lst_in представить в виде вложенного списка вида:
[['имя_1', 'звание_1'], ['имя_2', 'звание_2'], ..., ['имя_N', 'звание_N']]
Этот список присвоить переменной с именем lst. Затем, отсортировать его по возрастанию званий.
Выводить на экран ничего не нужно, только сформировать список и указать на него переменную lst."""
# import sys
#
# # считывание списка из входного потока (переменную lst_in не менять)
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список строк lst_in)
# example = ['рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант', 'капитан', 'майор', 'подполковник', 'полковник']
# lst = [x.split('=') for x in lst_in]
# lst.sort(key=lambda rank: example.index(rank[1]))
# print(lst)