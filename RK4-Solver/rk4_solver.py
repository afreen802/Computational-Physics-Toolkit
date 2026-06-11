import numpy as np
import matplotlib.pyplot as plt

# =====================================
# PARAMETERS
# =====================================

N0 = 100
lam = 0.1

t0 = 0
tf = 50
h = 0.5

# =====================================
# DIFFERENTIAL EQUATION
# dN/dt = -lambda*N
# =====================================

def f(t, N):
    return -lam * N

# =====================================
# RK4 METHOD
# =====================================

t_values = [t0]
N_values = [N0]

t = t0
N = N0

while t < tf:

    k1 = h * f(t, N)

    k2 = h * f(
        t + h/2,
        N + k1/2
    )

    k3 = h * f(
        t + h/2,
        N + k2/2
    )

    k4 = h * f(
        t + h,
        N + k3
    )

    N = N + (k1 + 2*k2 + 2*k3 + k4)/6

    t = t + h

    t_values.append(t)
    N_values.append(N)

# =====================================
# EXACT SOLUTION
# =====================================

t_exact = np.linspace(t0, tf, 500)

N_exact = N0 * np.exp(-lam * t_exact)

# =====================================
# ERROR ANALYSIS
# =====================================

N_exact_rk4 = N0 * np.exp(
    -lam * np.array(t_values)
)

error = np.abs(
    np.array(N_values) -
    N_exact_rk4
)

print(
    "Maximum Error =",
    np.max(error)
)

# =====================================
# PLOT
# =====================================

plt.figure(figsize=(8,5))

plt.plot(
    t_values,
    N_values,
    'o',
    label='RK4 Solution'
)

plt.plot(
    t_exact,
    N_exact,
    label='Exact Solution'
)

plt.xlabel("Time")

plt.ylabel("N(t)")

plt.title(
    "Radioactive Decay: RK4 vs Exact Solution"
)

plt.grid()

plt.legend()

plt.savefig(
    "rk4_decay.png",
    dpi=300
)

plt.show()
