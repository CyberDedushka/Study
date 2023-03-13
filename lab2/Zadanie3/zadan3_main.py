class IPStorage:
    ips: dict = {}
    count: int = 0

    def __init__(self, string: str = ''):
        self.string = string

    def __str__(self):
        return str(self.ips)

    def __eq__(self, other):
        return self.ips == other.ips and self.count == other.count

    def view_ips(self):
        for ip in self.ips.values():
            print(ip, '\n')

    def generate_ips(self):
        for symbol in self.string:
            if symbol.isupper() and symbol.isalpha():
                self.ips[self.count] = f'192.168.{self.string.index(symbol)}.{str(ord(symbol))}'
                self.count += 1


a = IPStorage('asdHM332 23 dfs sdfG')
b = IPStorage('asdHM332 23 dfs sdfG')
print(a == b) # True

a.view_ips()
print('----------------------')
a.generate_ips()
a.view_ips()

