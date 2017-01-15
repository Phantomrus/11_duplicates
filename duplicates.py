import os
from collections import defaultdict

def register_creation(directory):
    # os.walk возвращает генератор кортежей из трех элементов. 
    # 1. Абсолютный адрес очередного каталога (строка).
    # 2. Имена (без адреса) подкаталогов первого уровня для текущего каталога (список).
    # 3. Имена (без адреса) файлов данного каталога.
    
    register = defaultdict(list) # defaults to list
    # Словарь {(Имя файла, размер): [расположение1, расположение2]}

    for root, dirs, files in os.walk(directory):
        for file_name in files:
            path = os.path.join(root,file_name) # формирование адреса
            size_file = os.path.getsize(path)
            register[(file_name, size_file)].append(path)

    return register

def search_doubles(register):
    # doubles [[имя, размер, [расположение 1, расположение 2 ... расположение n]
    #           [имя, размер, [расположение 1, расположение 2 ... расположение n]]]
    doubles = []
    for key in register:
        if len(register[key]) > 1:
            doubles.append([key[0], key[1], register[key]])
    return doubles


def print_doubles(doubles):
    for num, element in enumerate(doubles, start =1):
        print("\nДублированный файл номер %s\nИмя файла: %s\nРазмер файла: %s\nВсе местоположения файла:\n%s\n" % (num, element[0], element[1], element[2])) # сделать выравнивание, логичнее сделать вывод без привязки к количеству элементов. Ещё один цикл for и отредактировать окончание print.     

if __name__ == '__main__':

    directory = input("Введите папку для поиска дубликатов:\n")
    while not os.path.isdir(directory):
        directory = input("Такой директории не существует. Пожалуйста, введите корректный путь:\n")

    register = register_creation(directory)

    doubles = search_doubles(register)
    if doubles:
        print("Реестр дублированных файлов готов.")
        while True:
            choice = input("Введите 1, если хотите вывести список дублей на экран.\nВведите 0, если хотите завершить программу.\n")
            if choice == "1":
                print_doubles(doubles)
            elif choice == "0":
                break
            else:
                print("\nВведено неверное значение.\n")

    print("\nПрограмма завершена.")