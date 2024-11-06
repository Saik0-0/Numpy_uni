import numpy as np

flowers = []
for i in range(5):
    flower = list(map(int, input().split()))
    flowers.append(flower)

prices = np.array(flowers)[:, -1]
flowers = np.array(flowers)[:, :-1]
print(np.linalg.solve(flowers, prices))
