import numpy as np


data = np.genfromtxt('C:/Users/alexa/Downloads/population.csv', delimiter=';',  encoding='utf-8', dtype=None, names=True)
cities = data['Города_Российской_Федерации']

print(cities)