import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
cmap = colors.ListedColormap(['black', 'green', 'red'])
def initialize_forest(n, p_tree, p_burn):
    forest = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if np.random.rand() < p_tree:
                forest[i, j] = 1
            elif np.random.rand() < p_burn:
                forest[i, j] = 2
    return forest

def update_forest(forest, f, p_burn):
    new_forest = np.zeros_like(forest)
    n = forest.shape[0]
    for i in range(n):
        for j in range(n):
            if forest[i, j] == 0:
                new_forest[i, j] = 0
            elif forest[i, j] == 1:
                new_forest[i, j] = 1
                if np.random.rand() < f:
                    new_forest[i, j] = 2
            elif forest[i, j] == 2:
                new_forest[i, j] = 0
                for k in range(max(i-1, 0), min(i+2, n)):
                    for l in range(max(j-1, 0), min(j+2, n)):
                        if forest[k, l] == 1 and np.random.rand() < p_burn:
                            new_forest[k, l] = 2

    plt.imshow(new_forest, cmap=cmap)
    plt.pause(0.5)
    return new_forest

# Initialize the forest
n = 100
p_tree = 1
p_burn = 0.1
forest = initialize_forest(n, p_tree, p_burn)

# Set the parameters of the forest fire model

f = 0.01 # probability that a non-burning tree will spontaneously catch fire
p_burn = 0.01 # probability that a burning tree will ignite each of its non-burning neighbors

# Simulate the forest fire for some number of steps
n_steps = 1000
for i in range(50):
    forest = update_forest(forest, f, p_burn)




