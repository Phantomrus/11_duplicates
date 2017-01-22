# Anti-Duplicator

Программа ищет дублированные файлы в указанной директории и всех её поддиректориях.
Файл сравнивается по имени и размеру.

Скрипт запускается с параметром `-p` или `--path` после которого указывается директория, в которой необходимо осуществить поиск дубликатов. 
####Пример запуска скрипта: 
`python3.5 duplicates.py --path /home/username/testdirectory`

Скрипт выведет информацию о том найдены ли дублированные файлы в директории и выведет их на экран.
####Пример вывода результатов работы скрипта:
```
Реестр дублированных файлов готов.

Введите 1, если хотите вывести список дублей на экран.
Введите 0, если хотите завершить программу.

1

Дублированный файл номер 1
Имя файла: 6757567
Размер файла: 0
Все местоположения файла:
/home/username/testdirectory/рр/6757567
/home/username/testdirectory/123/6757567

Дублированный файл номер 2
Имя файла: Hello doc
Размер файла: 0
Все местоположения файла:
/home/username/testdirectory/Hello doc
/home/username/testdirectory/dfgdfgdfg/Hello doc
/home/username/testdirectory/123/234/Hello doc

Программа завершена.
```

* Функция check_of_a_directory проверяет наличие указанной директории.
* Функция creation_of_the_register создает реестр всех файлов в указанной директории. Структура:

```
register_of_files {(Имя файла, размер): [расположение1, расположение2]}
```

* Функция search_doubles формирует список дублированных файлов. Структура:

```
list_of_doubles {(имя, размер): [расположение 1, расположение 2 ... расположение n]
                    (имя, размер): [расположение 1, расположение 2 ... расположение n]}
 ```
 
* Функция print_doubles выводит данные о дублированных файлах на экран.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
