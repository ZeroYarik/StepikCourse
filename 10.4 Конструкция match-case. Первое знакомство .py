# cmd = 2.4
#
# match cmd:
#     case str() as command if len(command) < 10 and command[0] == 'c':
#         print(f"строковая команда: {command}")
#     case bool() as command:
#         print(f"булева команда: {command}")
#     case int() | float() as command if 0 <= command <= 9:
#         print(f"численная команда: {command}")
#     case _:
#         print(f"другая комaнда")

# print("проверки завершены")

"""Пользователь может ввести с клавиатуры следующие команды в виде строки:
top или Top или TOP
bottom или Bottom или BOTTOM
right или Right или RIGHT
left или Left или LEFT
cmd = input()
С помощью оператора match/case необходимо определить тип команды cmd и при совпадении вывести на экран сообщение в формате:
Команда <название команды малыми буквами>
Например, при вводе Top, должны на выходе получить:
Команда top
И так для всех четырех команд. Если тип команды не определен, то вывести строку:
Неверная команда"""

# cmd = input()
#
# match cmd:
#     case "top" | "Top" | "TOP" as command:
#         print(f"Команда top")
#     case "bottom" | "Bottom" | "BOTTOM" as command:
#         print(f"Команда bottom")
#     case "right" | "Right" | "RIGHT" as command:
#         print(f"Команда right")
#     case "left" | "Left" | "LEFT" as command:
#         print(f"Команда left")
#     case _:
#         print("Неверная команда")

"""В функцию get_data() передается параметр value:
def get_data(value):
    match value:
        # здесь продолжайте программу
    
    return None
Необходимо дописать оператор match/case в этой функции так, чтобы для каждого типа данных (int, float и str)
 формировалась переменная со значением value и возвращалась функцией (непосредственно из блока case).
P. S. Вызывать функцию не нужно, только дописать."""
# def get_data(value):
#     match value:
#         case int() as val:
#             return val
#         case float() as val:
#             return val
#         case str() as val:
#             return val
#
#
#     return value

""" В функцию get_data() передается параметр value:
def get_data(value):
    match value:
        # здесь продолжайте программу
    
    return None
Необходимо дописать оператор match/case со следующими шаблонами:
если переменная value имеет тип int и больше нуля, то вернуть значение переменной value;
если переменная value имеет тип float и находится в диапазоне [-100; 100], то вернуть значение переменной value;
если переменная value имеет тип str, то просто вернуть ее значение.
P. S. Вызывать функцию не нужно, только дописать шаблоны."""
# def get_data(value):
#     match value:
#         case int() as val if 0 < val:
#             return value
#         case float() as val if -100 <= val <= 100:
#             return value
#         case str() as val:
#             return value
#
#     return value
#
#
# print(get_data(99))