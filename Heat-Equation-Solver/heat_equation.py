import numpy as np
import matplotlib.pyplot as plt

# =====================================
# PARAMETERS
# =====================================

L = 1.0
nx = 50

dx = L / (nx - 1)

alpha = 0.01

dt = 0.0005

nt = 1000

# =====================================
# SPATIAL GRID
# =====================================

x = np.linspace(0, L, nx)

# =====================================
# INITIAL TEMPERATURE
# =====================================

T = np.zeros(nx)

# Hot region in the center

T[20:30] = 100

T_initial = T.copy()

# =====================================
# FINITE DIFFERENCE SOLUTION
# =====================================

for n in range(nt):

    T_new = T.copy()

    for i in range(1, nx - 1):

        T_new[i] = (
            T[i]
            + alpha * dt / dx**2
            * (
                T[i+1]
                - 2*T[i]
                + T[i-1]
            )
        )

    T = T_new

# =====================================
# PLOT RESULTS
# =====================================

plt.figure(figsize=(8,5))

plt.plot(
    x,
    T_initial,
    label="Initial Temperature"
)

plt.plot(
    x,
    T,
    label="Final Temperature"
)

plt.xlabel("Position")

plt.ylabel("Temperature")

plt.title("Heat Diffusion in a One-Dimensional Rod")

plt.grid()

plt.legend()

plt.savefig(
    "heat_diffusion.png",
    dpi=300
)

plt.show()
