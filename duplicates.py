import os
import argparse
from collections import defaultdict

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path')
    return parser


def check_path(directory):
    while not os.path.isdir(directory):
            directory = input("Указанной вами директории не существует. Пожалуйста, введите корректный путь:\n")
    return directory


def creation_of_the_register(directory):
    
    register = defaultdict(list)
    # Словарь {(Имя файла, размер): [расположение1, расположение2]}

    for root, dirs, files in os.walk(directory):
        for file_name in files:
            path = os.path.join(root,file_name)
            size_file = os.path.getsize(path)
            register[(file_name, size_file)].append(path)

    return register


def search_doubles(register):
    # list_of_doubles {(имя, размер): [расположение 1, расположение 2 ... расположение n]
    #           (имя, размер): [расположение 1, расположение 2 ... расположение n]]}

    list_of_doubles = {(key[0], key[1]): register[key] for key in register if len(register[key]) > 1}
    return list_of_doubles


def print_options(list_of_doubles):
    if list_of_doubles:
        print("Дублированные файлы найдены. Реестр дублированных файлов готов.")
        while True:
            choice = input("\nВведите 1, если хотите вывести список дублей на экран.\nВведите 0, если хотите завершить программу.\n")
            if choice == "1":
                print_doubles(list_of_doubles)
                break
            elif choice == "0":
                break
            else:
                print("\nВведено неверное значение.\n")
    else:
        print("Дублированные файлы в директории не найдены.")


def print_doubles(list_of_doubles):
    for num, element in enumerate(list_of_doubles.keys(), start =1):
        print("\nДублированный файл номер %s\nИмя файла: %s\nРазмер файла: %s\nВсе местоположения файла:"\
            % (num, element[0], element[1]))
        for path in list_of_doubles[element]:
            print(path)


if __name__ == '__main__':

    parser = createParser()
    namespace = parser.parse_args()
    directory = check_path(namespace.path)
    register = creation_of_the_register(directory)

    list_of_doubles = search_doubles(register)
    print_options(list_of_doubles)

    print("\nПрограмма завершена.")
