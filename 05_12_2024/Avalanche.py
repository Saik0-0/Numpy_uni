class Avalanche:
    def __init__(self):
        self.string = 'O'

    def go(self):
        print(self.string)

        new_string = ''
        for i in self.string:
            if i == 'O':
                new_string += 'ooOoo'
            elif i == 'o':
                new_string += 'oOo'

        self.string = new_string


ava = Avalanche()
ava.go()
ava.go()
ava.go()