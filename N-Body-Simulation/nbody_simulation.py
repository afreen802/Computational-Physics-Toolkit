import numpy as np
import matplotlib.pyplot as plt

# =====================================
# CONSTANTS
# =====================================

G = 6.67430e-11

M_sun = 1.989e30

AU = 1.496e11

# =====================================
# INITIAL CONDITIONS
# =====================================

x = AU
y = 0

vx = 0
vy = 29780

dt = 24 * 3600

days = 365

# =====================================
# STORAGE
# =====================================

x_positions = []
y_positions = []

# =====================================
# SIMULATION
# =====================================

for step in range(days):

    r = np.sqrt(x**2 + y**2)

    ax = -G * M_sun * x / r**3
    ay = -G * M_sun * y / r**3

    vx += ax * dt
    vy += ay * dt

    x += vx * dt
    y += vy * dt

    x_positions.append(x / AU)
    y_positions.append(y / AU)

# =====================================
# PLOT
# =====================================

plt.figure(figsize=(8,8))

plt.plot(
    x_positions,
    y_positions,
    label="Earth Orbit"
)

plt.scatter(
    0,
    0,
    s=200,
    label="Sun"
)

plt.xlabel("x (AU)")
plt.ylabel("y (AU)")

plt.title("Earth Orbit Around the Sun")

plt.grid()

plt.axis("equal")

plt.legend()

plt.savefig(
    "orbit.png",
    dpi=300
)

plt.show()
