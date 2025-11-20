import random
import matplotlib.pyplot as plt

def info_spread(N=1000, steps=300, beta=0.001):
    nodes = [0] * N
    info_counts = []
    nodes[random.randint(0, N-1)] = 1

    for _ in range(steps):
        sender = random.randint(0, N-1)
        if nodes[sender] == 1:
            if random.random() < beta:
                target = random.randint(0, N-1)
                nodes[target] = 1
        info_counts.append(sum(nodes))
    return info_counts

if __name__ == "__main__":
    I = info_spread()
    plt.plot(I)
    plt.title("Information Spread (Stochastic)")
    plt.xlabel("Time")
    plt.ylabel("Nodes with Information")
    plt.grid()
    plt.show()