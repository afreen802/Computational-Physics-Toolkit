# Numerical Solution of the Heat Equation

## Abstract

The heat equation is a fundamental partial differential equation describing thermal diffusion. In this project, the one-dimensional heat equation is solved numerically using the Finite Difference Method.

---

# Introduction

Heat naturally flows from regions of higher temperature to regions of lower temperature.

The heat equation provides a mathematical model for this process and is widely used in physics and engineering.

---

# Theory

The one-dimensional heat equation is:

∂T/∂t = α ∂²T/∂x²

where α is the thermal diffusivity.

The equation predicts how temperature evolves over time.

---

# Numerical Method

The spatial derivative is approximated using finite differences.

The temperature at each grid point is updated according to neighboring temperatures.

---

# Initial Conditions

The rod is initially cold except for a localized hot region at the center.

---

# Results

![Heat Diffusion](figures/heat_diffusion.png)

The simulation shows heat spreading outward from the hot region.

The temperature profile becomes smoother as time progresses.

---

# Applications

- Heat Transfer
- Materials Science
- Climate Modeling
- Astrophysics
- Engineering Simulations

---

# Conclusion

The Finite Difference Method successfully reproduced the diffusion of heat through a one-dimensional rod.

The project demonstrates numerical solution techniques for partial differential equations.

---

# References

1. Newman, Computational Physics
2. Landau, Computational Physics
3. Numerical Recipes
