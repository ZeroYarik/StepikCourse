# import time
#
#
# def get_nod(a, b):
#     """Вычисляется НОД для натуральных чисел a, b по алгоритму Евклида.
#     :param a: первое натуральное число
#     :param b: второе натуральное число
#     :return: НОД
#     """
#
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#
#     return a
#
#
# def test_nod(func):
#     # --- тест №1 ---
#     a = 28
#     b = 35
#     res = func(a, b)
#     if res == 7:
#         print("TEST1 - OK")
#     else:
#         print("TEST1 - FAILED")
#
#     # --- тест №2 ---
#     a = 100
#     b = 1
#     res = func(a,b)
#     if res == 1:
#         print("TEST2 - OK")
#     else:
#         print("TEST2 - FAILED")
#
#     # --- тест №3 ---
#     a = 2
#     b = 100000000
#     st = time.time()
#     res = func(a, b)
#     et = time.time()
#     dt = et - st
#     if res == 2 and dt < 1:
#         print("TEST3 - OK")
#     else:
#         print("TEST3 - FAILED")
#
#
# res = get_nod(18, 24)
# print(res)
# help(get_nod)
#
# test_nod(get_nod)
#
#
def get_nod(a, b):
    """Вычисляется НОД для натуральных чисел a, b по алгоритму Евклида.
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

a, b = tuple(map(int, input().split()))
res = (get_nod(a, b))
print(res)