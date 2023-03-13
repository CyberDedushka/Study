class Game:
    def __init__(self):
        while True:
            try:
                self.number = int(input("Введите число от 0 до 100: "))
                if self.number < 0 or self.number > 100:
                    raise ValueError("Число должно быть от 0 до 100")
                break
            except ValueError as e:
                print(f"Ошибка: {e}")

    def check(self):
        while True:
            try:
                guess = int(input("Введите угаданное число: "))
                if guess != self.number:
                    raise ValueError("Неверное число")
                print("Правильно!")
                break
            except ValueError as e:
                print(f"Ошибка: {e}")


# Пример использования класса
game = Game()
game.check()
