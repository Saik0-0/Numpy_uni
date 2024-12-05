class QuickFactorial:
    def result(self, n):
        if n == 1 or n == 0:
            return 1
        else:
            return n * QuickFactorial.result(self, n - 1)


q = QuickFactorial()
print(q.result(30))