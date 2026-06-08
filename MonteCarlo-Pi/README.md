# Monte Carlo Estimation of π

## Overview

This project estimates the value of π using the Monte Carlo method.

Random points are generated inside a square of side length 2. The ratio of points falling inside the unit circle to the total number of points is used to estimate π.

## Theory

For a unit circle:

Area = π

For the surrounding square:

Area = 4

Therefore,

π = 4 × (Points Inside Circle / Total Points)

## Methodology

1. Generate random points.
2. Check whether each point lies inside the unit circle.
3. Compute the ratio.
4. Estimate π.
5. Analyze convergence with increasing sample size.

## Results

### Circle Simulation

![Circle Simulation](figures/Circle%20Simulation.png)


### Convergence Plot

![Convergence Plot](figures/Convergence%20Plot.png)

## Technologies

- Python
- NumPy
- Matplotlib

## Future Improvements

- Parallel implementation
- Importance sampling
- Monte Carlo integration of arbitrary functions
