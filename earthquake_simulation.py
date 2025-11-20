import random
import numpy as np
import matplotlib.pyplot as plt

def earthquake_simulation(size=50, critical=4, steps=5000):
    grid = np.random.randint(0, critical, (size, size))
    avalanche_sizes = []

    for _ in range(steps):
        grid += 1
        avalanche = 0
        unstable = True
        while unstable:
            unstable = False
            for i in range(size):
                for j in range(size):
                    if grid[i, j] >= critical:
                        avalanche += 1
                        unstable = True
                        grid[i, j] -= critical
                        if i > 0: grid[i-1, j] += 1
                        if i < size-1: grid[i+1, j] += 1
                        if j > 0: grid[i, j-1] += 1
                        if j < size-1: grid[i, j+1] += 1
        avalanche_sizes.append(avalanche)
    return avalanche_sizes

if __name__ == "__main__":
    aval = earthquake_simulation()
    plt.hist([x for x in aval if x > 0], bins=50)
    plt.title("Earthquake Avalanche Sizes")
    plt.xlabel("Event Size")
    plt.ylabel("Frequency")
    plt.show()