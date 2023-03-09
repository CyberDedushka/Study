from abc import ABC, abstractmethod
from random import randint


FIELDS = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]
CONDITIONS = {
    1: 0,
    2: 0,
    3: 0,
    4: 1,
    5: 1,
    6: 1,
    7: 2,
    8: 2,
    9: 2,
}
NUMBERS = [i for i in range(1, 10)]


def transpose(matrix: list):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


class Player(ABC):
    def __init__(self, marker):
        self.progress = []
        self.marker = marker

    @abstractmethod
    def move(self):
        pass

    def write_marker(self, field):
        row = CONDITIONS[field]
        column = FIELDS[row].index(str(field))
        FIELDS[row][column] = self.marker
        NUMBERS.remove(field)

    @staticmethod
    def is_winner():
        diagonal_left = [FIELDS[0][0], FIELDS[1][1], FIELDS[2][2]]
        diagonal_right = [FIELDS[0][2], FIELDS[1][1], FIELDS[2][0]]
        transpose_fields = transpose(FIELDS)
        check_sets = [set(diagonal_left), set(diagonal_right)]
        for field in FIELDS:
            check_sets.append(set(field))
        for field in transpose_fields:
            check_sets.append(set(field))
        for st in check_sets:
            if len(st) == 1 and 'O' in st:
                return 'You Won!'
            elif len(st) == 1 and 'X' in st:
                return 'You PC!'
        return ''


class Human(Player):
    marker = 'O'

    def __init__(self):
        super().__init__(self.marker)

    def move(self):
        field = 0
        while field not in NUMBERS:
            field = int(input('Выберите клетку из доступных: '))
        self.write_marker(field)
        self.progress.append(field)


class PC(Player):
    marker = 'X'

    def __init__(self):
        self._first_move = False
        super().__init__(self.marker)

    def move(self):
        is_first_move = self.__make_first_move()
        if is_first_move:
            field = 0
            while field not in NUMBERS:
                field = randint(1, 9)
            self.write_marker(field)

    @property
    def first_move(self):
        return self._first_move

    @first_move.setter
    def first_move(self, flag):
        self._first_move = flag

    def __make_first_move(self):
        if not self._first_move:
            FIELDS[1][1] = self.marker
            NUMBERS.remove(5)
            self._first_move = True
            return False
        return True


computer = PC()
people = Human()
while True:
    print(NUMBERS)
    computer.move()
    for line in FIELDS:
        print(line, '\n')
    print(NUMBERS)
    if computer.is_winner():
        print(computer.is_winner())
        break
    if not NUMBERS:
        break
    people.move()
    for line in FIELDS:
        print(line, '\n')
    if computer.is_winner():
        print(computer.is_winner())
        break
    print(NUMBERS)
