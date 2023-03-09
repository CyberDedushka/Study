import os.path
from abc import ABC, abstractmethod
from exceptions import *


def sort_by_alphabet(input_str: str) -> str:
    return input_str[0]


class FileManager(ABC):
    def __init__(self, path: str):
        self.path = path

    def read(self) -> list:
        if os.path.exists(self.path):
            with open(self.path, 'r+') as f:
                return f.readlines()
        else:
            raise ClearFileException('File not exist')

    def write(self, data: list) -> None:
        with open(self.path, 'w+') as f:
            f.writelines(data)

    @staticmethod
    def remove_symbols(symbol: str, content: list) -> None:
        while symbol in set(content):
            content.remove(symbol)

    @abstractmethod
    def parse(self):
        pass


class Notes(FileManager):
    def parse(self) -> tuple:
        info = self.read()
        # return_list: list = []  # Для задротов можно везде указать типы
        return_names_list = []
        return_all_list = []
        note_template = ['name', 'surname', 'mark']
        if not info:
            raise ClearFileException('File is clear!')
        for item in info:
            split_list = item.split(' ')
            self.remove_symbols('', split_list)
            if len(split_list) != 3:
                raise BadStringException('File with bad string')
            split_list[-1] = float(split_list[-1])
            tmp = dict(zip(note_template, split_list))
            return_all_list.append(tmp)
            tmp = tmp.get('name') + ' ' + tmp.get('surname')
            if tmp not in return_names_list:
                return_names_list.append(tmp)
        return return_all_list, return_names_list

    def make_otchet(self) -> list:
        info_all, info_students = self.parse()
        info_students.sort(key=sort_by_alphabet)
        clear_list = []
        for student in info_students:
            mark = 0
            for obj in info_all:
                if (obj.get('name') + ' ' + obj.get('surname')) == student:
                    mark += obj.get('mark')
            clear_list.append({'name': student.split()[0], 'surname': student.split()[-1], 'mark': round(mark, 1)})
        return clear_list

    def print_otchet(self) -> None:
        otchet_list = self.make_otchet()
        for otchet_obj in otchet_list:
            print(
                str(otchet_obj.get('name')) + ' ' + str(otchet_obj.get('surname')) + ' ' + str(otchet_obj.get('mark')))


professor_notes = Notes(input('Введите путь к заметкам: '))
professor_notes.print_otchet()
