file = open("my_fyle.txt", encoding="utf-8")

# print(file.read(4)) # чтение определенных символов
# file.seek(0) # переход на файловую позицию
# print(file.read(4))
# pos = file.tell() # вывод файловой позиции
# print(pos)

# print(file.readline()) # \n - символ конца строки

# for line in file: # чтение построчно в цикле
#     print(line, end='')

print(file.readlines()) # читает в виде списка. Использовать аккуратно так как с большим файлом может не хватить памяти.

file.close() #освобождение памяти связанной с этим файлом, не будет потери данных.