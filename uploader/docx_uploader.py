# В заголовке файла сперва импортите системные пакеты python, либо установленные с помощью Pip
import docx

# С отступом в 1 строчку импортим свои кастомные пакеты
from uploader.base_uploader import BaseUploader


class DocxUploader(BaseUploader):
    def _upload(self, file):
        '''
        Используя docx, Либо иную библиотеку по работе с форматом, обрабатываете файл, сохраняете куда нужно
        (диск, БД и т.д.)

        :param file:
        :return:
        '''
        # Предобработка (пример из пальца)
        processed_file = self.__preprocess_file(file=file)

        # Для примера сохраним в переменную __file (private) предобработанный файл
        self.__file = docx.Document(processed_file)

        # do something else...

    def __preprocess_file(self, file):
        '''
        Метод предобработки файла, например, он приходит в формате, требующим предобработки для передачи его
        в docx.Document

        1. Метод можно было определить в базовом классе и делать override protected метода
        2. Рассмотрим путь, когда не каждый файл нуждается в предобработке, тогда очевидный выбор - private реализация
        в конкретном классе-обработчике файла

        :param file:
        :return: processed file
        '''

        # Искусственный пример чего-то деланья с файлом (предобработки) в качестве return-value
        return bytes(file)

    def upload_from_cli(self, file):
        '''
        1. Для публичного использования во внешнем коде создадим публичный метод для вызова protected метода
        2. Суть объявления метода protected была показана как часть пример идеалогии ООП
        3. Если метод нужно вызывать из внешних точек в коде, он должен быть public, то есть не иметь черточек
        перед именованием

        :param file:
        :return:
        '''
        # Just call protected method
        self._upload(file=file)


def main(args):
    '''
    1. Данная функция используется для import-в __main__.py
    2. Из парсера аргументов к данному .py сценарию мы передаем сюда аргумент args и вызываем срабатывание этой функции
    (main)
    3. Т.е. код ниже будет исполнен, а данные будут взяты из args

    :param args:
    :return:
    '''
    file = args.file
    uploader = DocxUploader()
    uploader.upload_from_cli(file=file)