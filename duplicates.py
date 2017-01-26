import os
import argparse
from collections import defaultdict


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path')
    return parser


def create_register(directory_for_check):  
    register_of_files = defaultdict(list)

    for root_directory, directorys, files_in_directory in os.walk(directory_for_check):
        for file_name in files_in_directory:
            path_to_file = os.path.join(root_directory,file_name)
            size_of_file = os.path.getsize(path_to_file)
            register_of_files[(file_name, size_of_file)].append(path_to_file)

    return register_of_files


def search_for_doubles(register_of_files):  
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

    parser = create_parser()
    arguments_of_script = parser.parse_args()
    directory_for_check = arguments_of_script.path
    
    if os.path.isdir(directory_for_check):
        register_of_files = create_register(directory_for_check)
        list_of_doubles = search_for_doubles(register_of_files)
        print_doubles(list_of_doubles)
    else:
        print("Указанной вами директории не существует.\n")
        
    print("\nПрограмма завершена.")
