# RK4 Solver for Radioactive Decay

## Abstract

The fourth-order Runge-Kutta (RK4) method is a widely used numerical technique for solving ordinary differential equations. In this project, RK4 is applied to the radioactive decay equation and compared with the exact analytical solution.

---

# Introduction

Many physical systems are governed by differential equations. While some equations have analytical solutions, numerical methods are often required for more complex systems.

The RK4 method provides high accuracy while remaining computationally efficient.

---

# Theory

Radioactive decay is described by

dN/dt = -λN

where:

N = number of nuclei

λ = decay constant

The analytical solution is

N(t) = N₀e^(-λt)

---

# Numerical Method

The RK4 method estimates the solution using four intermediate slopes:

k₁
k₂
k₃
k₄

and updates the solution through a weighted average.

---

# Results

The numerical solution closely matches the exact analytical solution.

Insert Figure:

![RK4 Plot](figures/rk4_decay.png)

Maximum numerical error remained extremely small throughout the simulation.

---

# Applications

RK4 is widely used in:

- Astrophysics
- Orbital Dynamics
- Plasma Physics
- Quantum Mechanics
- Fluid Dynamics

---

# Conclusion

The RK4 method successfully reproduced the analytical solution of radioactive decay with high accuracy.

---

# References

1. Newman, Computational Physics
2. Numerical Recipes
3. Landau, Computational Physics
