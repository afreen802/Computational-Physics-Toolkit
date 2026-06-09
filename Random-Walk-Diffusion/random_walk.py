import numpy as np
import matplotlib.pyplot as plt

# =====================================
# PART 1: SINGLE RANDOM WALK
# =====================================

n_steps = 1000

x = [0]
y = [0]

for i in range(n_steps):

    direction = np.random.randint(0, 4)

    if direction == 0:
        x.append(x[-1] + 1)
        y.append(y[-1])

    elif direction == 1:
        x.append(x[-1] - 1)
        y.append(y[-1])

    elif direction == 2:
        x.append(x[-1])
        y.append(y[-1] + 1)

    else:
        x.append(x[-1])
        y.append(y[-1] - 1)

distance = np.sqrt(x[-1]**2 + y[-1]**2)

print("Final Distance from Origin =", distance)

plt.figure(figsize=(8,8))

plt.plot(x, y)

plt.scatter(0, 0, s=100, label="Start")

plt.scatter(x[-1], y[-1], s=100, label="End")

plt.title("2D Random Walk")

plt.xlabel("x")
plt.ylabel("y")

plt.grid()
plt.axis("equal")

plt.legend()

plt.savefig("random_walk.png", dpi=300)

plt.show()

# =====================================
# PART 2: DIFFUSION ANALYSIS
# =====================================

n_walks = 1000

step_values = [100, 200, 500, 1000, 2000, 5000]

msd_values = []

for n_steps in step_values:

    distances_squared = []

    for walk in range(n_walks):

        x = 0
        y = 0

        for step in range(n_steps):

            direction = np.random.randint(0, 4)

            if direction == 0:
                x += 1

            elif direction == 1:
                x -= 1

            elif direction == 2:
                y += 1

            else:
                y -= 1

        r_squared = x**2 + y**2

        distances_squared.append(r_squared)

    mean_r_squared = np.mean(distances_squared)

    msd_values.append(mean_r_squared)

    print(f"Steps = {n_steps}")
    print(f"MSD = {mean_r_squared}")
    print()

# =====================================
# PART 3: DIFFUSION LAW PLOT
# =====================================

plt.figure(figsize=(8,5))

plt.plot(step_values, msd_values, marker='o')

plt.xlabel("Number of Steps")

plt.ylabel("Mean Squared Displacement (MSD)")

plt.title("Diffusion Law Verification")

plt.grid()

plt.savefig("msd_plot.png", dpi=300)

plt.show()
