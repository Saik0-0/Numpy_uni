class SnowFlakes:
    def __init__(self, n):
        self.n = n
        self.m = [["-" for _ in range(n)] for _ in range(n)]
        for i in range(n):
            self.m[i][i] = "*"
            self.m[i][n - i - 1] = "*"
            self.m[i][n // 2] = "*"
            self.m[n // 2][i] = "*"
        self.k = 0
        self.count = 0
        self.g = 0

    def thaw(self, times, TF=True):
        if TF:
            self.g += times
        for _ in range(times):
            self.k = 0
            while self.m[self.k][self.k] != "*":
                self.k += 1
            self.m[self.k] = ["-" for _ in range(len(self.m))]
            for j in range(len(self.m)):
                self.m[j][self.k] = "-"
            self.m[-1 - self.k] = ["-" for _ in range(len(self.m))]
            for j in range(len(self.m)):
                self.m[j][-1 - self.k] = "-"

    def thicken(self, new=False):
        if new:
            self.mainthicken(0)
        else:
            self.mainthicken(1)

    def mainthicken(self, plusorzero):
        self.count += plusorzero
        self.k = 0
        while self.m[self.k][self.k] == "-":
            self.k += 1
        for _ in range(self.g - self.k):
            self.m = [["-" for _ in range(len(self.m))]] + self.m + [["-" for _ in range(len(self.m))]]
            for i in range(len(self.m)):
                self.m[i] = ["-"] + self.m[i] + ["-"]
        self.g = 0
        for i in range(len(self.m)):
            self.m[i][i] = self.m[i][len(self.m) - i - 1] = "*"
            self.m[i][len(self.m) // 2] = self.m[len(self.m) // 2][i] = "*"
        for i in range(len(self.m)):
            if i + self.count < len(self.m):
                self.m[i + self.count][i] = "*"
            if i - self.count >= 0:
                self.m[i - self.count][i] = "*"
            if len(self.m) // 2 + self.count < len(self.m):
                self.m[i][len(self.m) // 2 + self.count] = "*"
            if len(self.m) // 2 - self.count >= 0:
                self.m[i][len(self.m) // 2 - self.count] = "*"
            if len(self.m) // 2 + self.count < len(self.m):
                self.m[len(self.m) // 2 + self.count][i] = "*"
            if len(self.m) // 2 - self.count >= 0:
                self.m[len(self.m) // 2 - self.count][i] = "*"
            if i + self.count < len(self.m):
                self.m[i + self.count][-i - 1] = "*"
            if i - self.count >= 0:
                self.m[i - self.count][-i - 1] = "*"

    def freeze(self, kol):
        for _ in range(kol):
            self.m = [["-" for _ in range(len(self.m))]] + self.m + [["-" for _ in range(len(self.m))]]
            for i in range(len(self.m)):
                self.m[i] = ["-"] + self.m[i] + ["-"]
        for _ in range(kol):
            self.k = 0
            while self.m[self.k][self.k] != "*":
                self.k += 1
            self.m[self.k - 1][self.k - 1] = self.m[-self.k][-self.k] = "*"
            self.m[self.k - 1][-self.k] = self.m[-self.k][self.k - 1] = "*"
            self.m[self.k - 1][len(self.m) // 2] = self.m[-self.k][len(self.m) // 2] = "*"
            self.m[len(self.m) // 2][self.k - 1] = self.m[len(self.m) // 2][-self.k] = "*"
            self.thicken(True)
            self.thaw(self.k - 1, False)

    def show(self):
        for row in self.m:
            print("".join(row))

sf = SnowFlakes(29)
sf.freeze(3)
sf.thicken()
sf.thaw(3)
sf.show()