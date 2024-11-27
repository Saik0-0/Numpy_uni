import numpy as np


class Icecream:
    def __init__(self, flavors, ingredients, costs, outlays, demand):
        self.flavors = flavors
        self.ingredients = ingredients
        self.costs = costs
        self.outlays = outlays
        self.demand = demand
        self.months = {
            "January": 0,
            "February": 1,
            "March": 2,
            "April": 3,
            "May": 4,
            "June": 5,
            "July": 6,
            "August": 7,
            "September": 8,
            "October": 9,
            "November": 10,
            "December": 11,
        }

    def raw_costs(self):
        return np.multiply(self.costs, self.outlays)

    def sum_raw(self):
        return np.sum(self.outlays, axis=0)

    def sum_costs(self):
        return np.sum(self.raw_costs(), axis=1)

    def purchase_plan(self):
        return np.dot(self.outlays.T, self.demand)

    def year_costs(self):
        return self.demand * self.sum_costs().reshape(-1, 1)

    def month_costs(self, month):
        return self.year_costs()[:, self.months[month]]

    def goods_costs(self, flavor):
        return self.year_costs()[list(self.flavors).index(flavor)]

    def min_month_cost(self):
        return np.min(self.year_costs(), axis=0)

    def max_month_cost(self):
        return np.max(self.year_costs(), axis=0)

    def mean_raw(self):
        return np.mean(self.outlays, axis=0)

    def med_cost(self):
        return np.median(self.raw_costs(), axis=0)

    def useful_raw(self):
        return self.ingredients[np.where(self.sum_raw() == max(self.sum_raw()))]

