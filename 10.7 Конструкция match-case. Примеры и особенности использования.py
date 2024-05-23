# request = {'server': '127.0.0.10', 'login': 'root', 'password': '1234', 'port': 24}
#
#
# def connect_db(connect: dict) -> str:
#     match connect:
#         case {'server': host, 'login': login, 'password': psw, 'port': port}:
#             pass
#         case {'server': host, 'login': login, 'password': psw}:
#             port = 22
#         case _:
#             return "error connection"
#
#     return f"connection: {host}@{login}.{psw}:{port}"
#
# result = connect_db(request)
# print(result)