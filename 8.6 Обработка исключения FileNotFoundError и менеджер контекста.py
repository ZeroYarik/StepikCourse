try:
#    file = open("my_fyle.txt", encoding="utf-8")
    with open("my_fyle.txt", encoding="utf-8") as file:
        s = file.readlines()
        print(s)
    # try:
    #     s = file.readlines()
    #     int(s)
    #     print(s)
    # finally:
    #     file.close()
except FileNotFoundError:
    print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлом")