# request = {'url': 'https://stepik.ru/', 'method': 'GET', 'timeout': 1000}
#
# match request:
#     case{'url': url, 'method': method}:
#         print(f"Запрос: url: {url}, method: {method}")
#     case _:
#         print("Неверный запрос")

"""Имеется следующий фрагмент программы с функцией parse_json и словарем json_data:
С помощью оператора match/case в функцию parse_json добавьте в самое начало шаблон для выделения значения ключа access
 с проверкой на тип bool и для выделения даты (первое значение списка) из поля data с проверкой,
 что data является списком. Возвратите выделенные два значения в виде кортежа в формате (access, date).
P. S. В программе нужно только дописать шаблон. Вызывать функцию не нужно."""
# def parse_json(data):
#     match data:
#         case {'access': bool() as access, 'data': list([date, *_])}:
#             return access, date
#         case {'id': ids, 'data': [_, {'login': login}, _, _]}:
#             return ids, login
#
#
#     return None
#
# json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}

"""Имеется следующий фрагмент программы с функцией parse_json и словарем json_data:
С помощью оператора match/case в функцию parse_json добавьте в самое начало шаблон для выделения значений ключей login
 и email с проверкой, что они являются строками и при условии, что поле access принимает значение True. 
 Возвратите выделенные два значения в виде кортежа в формате (login, email).
P. S. В программе нужно только дописать шаблон. Вызывать функцию не нужно."""
# def parse_json(data):
#     match data:
#         case {'access': access, 'data': [_, {'login': str(login), 'email': str(email)}, *_]} if access == True:
#             return login, email
#         case {'id': ids, 'data': [_, {'login': login}, _, _]}:
#             return ids, login
#
#     return None
#
# json_data = {'id': 2, 'access': True, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}