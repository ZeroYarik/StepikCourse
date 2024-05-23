try:
    with open("out.txt", "a+") as file:
        file.seek(0)
        file.write("hello4")            # открывая тот или иной файл на запись мы удаляем все его прежнее содержимое
        s = file.readlines()            # открывая через "a" мы добавляем в файл
                                        # открывая файл на запись/дозапись мы не можем его читать
        print(s)
        file.write("hello4")
except:
    print("Ошибка прии работе с файлом")