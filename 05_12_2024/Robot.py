class Robot:
    def __init__(self, coord: tuple):
        self.x = coord[0]
        self.y = coord[1]
        self.commands = [coord]

    def move(self, string):
        self.commands = [(self.x, self.y)]
        for command in string:
            if command == 'N':
                self.y += 1
                self.commands.append((self.x, self.y))
            elif command == 'S':
                self.y -= 1
                self.commands.append((self.x, self.y))
            elif command == 'E':
                self.x += 1
                self.commands.append((self.x, self.y))
            elif command == 'W':
                self.x -= 1
                self.commands.append((self.x, self.y))
        return self.x, self.y

    def path(self):
        return self.commands


r = Robot((0, 0))
print(r.move('NENWEE'))
print(*r.path())
print()
print(r.move('ENWEWSNN'))
print(*r.path())
print()
print(r.move('NNNNNNNSSWENWEWSNN'))
print(*r.path())