import time


class Game:

    def __init__(self, numb):
        while (100 < numb) or (numb < 0):
            numb = int(input('Введите число больше 0 и меньше 100: '))
        self.numb = numb
        print(f'{self.numb} ', end='')
        time.sleep(2)
        print('\r', end='')
        self.child_numb = int(input('Введите число: '))

    def check(self):
        if self.numb != self.child_numb:
            raise Exception
        else:
            print('Верно')


a = Game(int(input('Введите число для запоминания: ')))
a.check()

