import numpy as np


class Analysis:
    def __init__(self, name):
        self.name = name
        with open(name, "r", encoding="utf-8") as f:
            data = f.read().strip().split("\n")
        self.years = np.array(data[0].split(";"))
        self.file = np.array([line.split(";") for line in data[1:]])

    def __str__(self):
        return f"File: {self.name},\ncities: {len(self.file)},\nyears: {len(self.file[0]) - 1}"

    def __call__(self, *years):
        years = list(years)
        for i in range(len(list(years))):
            years[i] = np.where(self.years == years[i])[0][0]
        result = np.array([self.file[:, i] for i in years])
        return np.transpose(result).astype(int)

    def get_cities(self):
        return self.file[:, 0]

    def get_data(self):
        return self.file[:, 1:].astype(int)

    def year_vector(self, year):
        index = np.where(self.years == year)[0][0]
        return self.file[:, index].astype(int)

    def growth(self, year1, year2):
        idx1, idx2 = np.where(self.years == year1)[0][0], np.where(self.years == year2)[0][0]
        year1_data = self.file[:, idx1].astype(int)
        year2_data = self.file[:, idx2].astype(int)
        return self.file[year2_data > year1_data, 0]

    def reduct(self, year1, year2):
        idx1, idx2 = np.where(self.years == year1)[0][0], np.where(self.years == year2)[0][0]
        return np.array(
            [self.file[i, 0] for i in range(len(self.file)) if int(self.file[i, idx1]) > int(self.file[i, idx2])])

    def city(self, name):
        city_data = self.file[self.file[:, 0] == name, 1:]
        return city_data.astype(int).flatten()

    def max_growth(self, year1, year2):
        idx1, idx2 = np.where(self.years == year1)[0][0], np.where(self.years == year2)[0][0]
        return np.max(self.file[:, idx2].astype(int) - self.file[:, idx1].astype(int))

    def max_reduct(self, year1, year2):
        idx1, idx2 = np.where(self.years == year1)[0][0], np.where(self.years == year2)[0][0]
        return np.max(self.file[:, idx1].astype(int) - self.file[:, idx2].astype(int))


cities = Analysis('C:/Users/alexa/Downloads/population (1).csv')
print(cities.city('Абакан'))
print(cities('2016', '2020', '2019'))
