import os
import argparse
from collections import defaultdict


def creation_of_the_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path')
    return parser


def check_of_a_directory(directory_for_check):
    while not os.path.isdir(directory_for_check):
        directory_for_check = input("Указанной вами директории не существует. Пожалуйста, введите корректный путь:\n")
    return directory_for_check


def creation_of_the_register(directory_for_check):  
    register_of_files = defaultdict(list)

    for root_directory, directorys, files in os.walk(directory_for_check):
        for file_name in files:
            path_to_file = os.path.join(root_directory,file_name)
            size_file = os.path.getsize(path_to_file)
            register_of_files[(file_name, size_file)].append(path_to_file)

    return register_of_files


def search_doubles(register_of_files):  
    list_of_doubles = {(key[0], key[1]): register_of_files[key] for key in register_of_files if len(register_of_files[key]) > 1}
    return list_of_doubles


def print_doubles(list_of_doubles):
    if list_of_doubles:
        print("Найдены следующие дублированные файлы:")
        for num, element in enumerate(list_of_doubles.keys(), start =1):
            print("\nДублированный файл номер %s\nИмя файла: %s\nРазмер файла: %s\nВсе местоположения файла:"\
                % (num, element[0], element[1]))
            for path_to_file in list_of_doubles[element]:
                print(path_to_file)
    else:
        print("Дублированные файлы в директории не найдены.")


if __name__ == '__main__':

    parser = creation_of_the_parser()
    arguments_of_script = parser.parse_args()

    directory_for_check = check_of_a_directory(arguments_of_script.path)
    register_of_files = creation_of_the_register(directory_for_check)

    list_of_doubles = search_doubles(register_of_files)
    print_doubles(list_of_doubles)

    print("\nПрограмма завершена.")
