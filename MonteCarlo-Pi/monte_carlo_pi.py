import numpy as np
import matplotlib.pyplot as plt

N_values = [100, 1000, 10000, 100000]

errors = []

for N in N_values:

    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)

    inside = (x**2 + y**2) <= 1

    points_inside = np.sum(inside)

    pi_estimate = 4 * points_inside / N

    error = abs(np.pi - pi_estimate)

    errors.append(error)

    print(f"N = {N}")
    print(f"Estimated π = {pi_estimate}")

plt.plot(N_values, errors, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.show()
