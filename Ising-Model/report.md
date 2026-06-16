# Monte Carlo Simulation of the Ising Model

## Abstract

The Ising model is a fundamental model in statistical mechanics used to study magnetism and phase transitions. In this project, a two-dimensional Ising system was simulated using the Metropolis Monte Carlo algorithm.

---

# Introduction

Many magnetic materials consist of microscopic magnetic moments called spins.

The Ising model approximates each spin as taking one of two possible values:

+1 or -1.

Despite its simplicity, the model exhibits complex collective behavior.

---

# Theory

The energy of the system is given by

H = -J Σ sᵢsⱼ

where:

- J = interaction strength
- s = spin variable

The probability of accepting a spin flip follows the Boltzmann distribution.

---

# Numerical Method

The Metropolis algorithm proceeds as follows:

1. Select a random spin.
2. Calculate energy change.
3. Accept or reject the flip.
4. Repeat many times.

---

# Results

The simulation demonstrates the transition from ordered magnetic states to disordered states as temperature increases.

### Spin Configuration

![Final Spins](figures/final_spins.png)

### Magnetization

![Magnetization](figures/magnetization_vs_temperature.png)

### Energy

![Energy](figures/energy_vs_temperature.png)

---

# Applications

- Magnetism
- Phase Transitions
- Critical Phenomena
- Complex Systems
- Machine Learning

---

# Conclusion

The Monte Carlo simulation successfully reproduced key qualitative features of the Ising model and demonstrated the effect of temperature on magnetic ordering.

---

# References

1. Newman, Computational Physics
2. Landau & Binder, A Guide to Monte Carlo Simulations in Statistical Physics
3. Pathria, Statistical Mechanics
