class FileDoesNotExist(Exception):
    pass


class BadLine(Exception):
    pass


class EmptyFile(Exception):
    pass


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if not lines:
                raise EmptyFile("File is empty.")
            scores = {}
            for line in lines:
                try:
                    name, surname, score = line.strip().split()
                    score = int(score)
                except ValueError:
                    raise BadLine(f"Bad line in file: {line.strip()}")
                if (name, surname) in scores:
                    scores[(name, surname)] += score
                else:
                    scores[(name, surname)] = score
            return scores
    except FileNotFoundError:
        raise FileDoesNotExist(f"File '{filename}' does not exist.")


def print_report(scores):
    for name, surname in sorted(scores):
        print(f"{name} {surname}: {scores[(name, surname)]}")


if __name__ == '__main__':
    filename = input("Enter filename: ")
    try:
        scores = read_file(filename)
        print_report(scores)
    except (FileDoesNotExist, BadLine, EmptyFile) as e:
        print(str(e))
