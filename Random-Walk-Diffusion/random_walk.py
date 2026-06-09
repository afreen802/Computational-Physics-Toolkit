import numpy as np
import matplotlib.pyplot as plt

n_steps = 1000

x = [0]
y = [0]

for i in range(n_steps):

    direction = np.random.randint(0,4)

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

plt.figure(figsize=(8,8))

plt.plot(x,y)

plt.scatter(0,0)

plt.scatter(x[-1],y[-1])

plt.title("2D Random Walk")

plt.xlabel("x")
plt.ylabel("y")

plt.grid()

plt.axis("equal")

plt.savefig("random_walk.png", dpi=300)

plt.show()

distance = np.sqrt(x[-1]**2 + y[-1]**2)

print("Final distance from origin =", distance)
