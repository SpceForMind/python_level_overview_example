'''
1. Данный файл является точкой, где создается парсер аргументов для каждого отедльного .py сценария
2. Сюда импортируются функции main из .py файлов, которые исполняют их функционал как CLI
3. Для каждой такой функции main_file_name создается парсер аргументов, затем он и вызывает срабатываение данной
main_file_name с передачей туда аргументов в переменной args

Read more: https://docs.python.org/3/library/argparse.html

'''
import argparse

from uploader.docx_uploader import main as docx_uploader_main


def parse_args():
    '''
    Создаем аргументы парсеров

    :return:
    '''
    # Общий парсер
    parser = argparse.ArgumentParser(description='File Uploaders')

    # Подпарсеры - через эту переменную мы будем добавлять отдельные парсеры для соответствующих .py сценариев
    # то есть описывать аргументы для переменной args каждой main_script_name (docx_uploader_main - пример)
    # После описания аргументов делается 'bind' функции и все готово!
    subparsers = parser.add_subparsers()

    devices_monitor_parser = subparsers.add_parser('docx_uploader',
                                                   help='Upload file [docx]')
    # Добавляем опц. аргумент 'file'
    devices_monitor_parser.add_argument('--file',
                                        type=str,
                                        required=True,
                                        help='path to docx file'
                                        )
    # Делаем bind парсера к docx_uploader_main, важно указывать без скобок, ведь функция тут передается как object
    # а не вызывается [ docx_uploader_main() - это вызов ], а без скобок это объект класса <function>
    devices_monitor_parser.set_defaults(func=docx_uploader_main)

    # Метод обработки входящих аргументов, возвращает объект args
    return parser.parse_args()


def main():
    '''
    Вызываем срабатываение нужной функции main_script_name
    Note: можно просто скопировать нижние 2 строчки и саму функцию, самое главное не ошибиться в функции
    parse_args()

    :return:
    '''
    args = parse_args()
    args.func(args)


# Данная конструкция работает, когда мы вызываем файл напрямую из интерпретатора
# Some theory - командой python -m uploader ... мы вызовем срабатывание этой конструкции
if __name__ == '__main__':
    main()

