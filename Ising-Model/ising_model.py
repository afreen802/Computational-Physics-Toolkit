import numpy as np
import matplotlib.pyplot as plt

# =====================================
# PARAMETERS
# =====================================

N = 20
J = 1.0

temperatures = np.linspace(1.0, 4.0, 15)

mc_steps = 5000

magnetizations = []
energies = []

# =====================================
# ENERGY FUNCTION
# =====================================

def calculate_energy(spins):

    energy = 0

    for i in range(N):
        for j in range(N):

            S = spins[i, j]

            neighbors = (
                spins[(i+1)%N, j]
                + spins[(i-1)%N, j]
                + spins[i, (j+1)%N]
                + spins[i, (j-1)%N]
            )

            energy += -J * S * neighbors

    return energy / 2

# =====================================
# MONTE CARLO SIMULATION
# =====================================

for T in temperatures:

    spins = np.random.choice(
        [-1, 1],
        size=(N, N)
    )

    for step in range(mc_steps):

        i = np.random.randint(0, N)
        j = np.random.randint(0, N)

        S = spins[i, j]

        neighbors = (
            spins[(i+1)%N, j]
            + spins[(i-1)%N, j]
            + spins[i, (j+1)%N]
            + spins[i, (j-1)%N]
        )

        delta_E = 2 * J * S * neighbors

        if delta_E < 0:

            spins[i, j] *= -1

        elif np.random.rand() < np.exp(-delta_E/T):

            spins[i, j] *= -1

    M = abs(np.sum(spins)) / (N*N)

    E = calculate_energy(spins) / (N*N)

    magnetizations.append(M)
    energies.append(E)

# =====================================
# FINAL SPIN CONFIGURATION
# =====================================

plt.figure(figsize=(6,6))

plt.imshow(spins)

plt.title(
    f"Final Spin Configuration (T={T:.2f})"
)

plt.colorbar()

plt.savefig(
    "final_spins.png",
    dpi=300
)

plt.show()

# =====================================
# MAGNETIZATION PLOT
# =====================================

plt.figure(figsize=(8,5))

plt.plot(
    temperatures,
    magnetizations,
    marker='o'
)

plt.xlabel("Temperature")

plt.ylabel("Magnetization")

plt.title(
    "Magnetization vs Temperature"
)

plt.grid()

plt.savefig(
    "magnetization_vs_temperature.png",
    dpi=300
)

plt.show()

# =====================================
# ENERGY PLOT
# =====================================

plt.figure(figsize=(8,5))

plt.plot(
    temperatures,
    energies,
    marker='o'
)

plt.xlabel("Temperature")

plt.ylabel("Energy per Spin")

plt.title(
    "Energy vs Temperature"
)

plt.grid()

plt.savefig(
    "energy_vs_temperature.png",
    dpi=300
)

plt.show()
