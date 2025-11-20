import random
import matplotlib.pyplot as plt

def mm1_queue(lambda_rate=0.5, mu=0.7, steps=10000):
    queue_length = 0
    lengths = []
    for _ in range(steps):
        if random.random() < lambda_rate:
            queue_length += 1
        if queue_length > 0 and random.random() < mu:
            queue_length -= 1
        lengths.append(queue_length)
    return lengths

if __name__ == "__main__":
    L = mm1_queue()
    plt.plot(L)
    plt.title("M/M/1 Queue Simulation")
    plt.xlabel("Time")
    plt.ylabel("Queue Length")
    plt.grid()
    plt.show()