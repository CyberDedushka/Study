class FileNotExistException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'FileNotExistException, {0} '.format(self.message)
        else:
            return 'FileNotExistException has been raised'


class BadStringException(FileNotExistException):
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        if self.message:
            return 'BadStringException, {0} '.format(self.message)
        else:
            return 'BadStringException has been raised'


class ClearFileException(FileNotExistException):
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        if self.message:
            return 'ClearFileException, {0} '.format(self.message)
        else:
            return 'ClearFileException has been raised'
