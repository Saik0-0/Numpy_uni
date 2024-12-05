class Rainbow:
    def __init__(self, number=1):
        self.colors = ['red', 'orange', 'yellow', 'green', 'light blue', 'blue', 'violet']
        self.number = number

    def next_color(self, color):
        if self.number == 1 or self.number == 3:
            return self.colors[(self.colors.index(color) + 1) % len(self.colors)]
        else:
            return self.colors[(self.colors.index(color) - 1) % len(self.colors)]


rb = Rainbow()
print(rb.next_color('light blue'))