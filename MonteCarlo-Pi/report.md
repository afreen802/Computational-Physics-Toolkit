# Monte Carlo Estimation of π Using Random Sampling

## Abstract

The Monte Carlo method is a numerical technique that uses random sampling to solve mathematical and physical problems. In this project, the value of π is estimated by generating random points inside a square and determining the fraction that falls within an inscribed unit circle. The accuracy of the estimate is studied as the number of random samples increases.

---

# 1. Introduction

Many physical systems involve randomness and uncertainty. Traditional analytical methods are often difficult or impossible to apply to such systems. Monte Carlo methods provide an alternative approach by using random sampling to approximate solutions.

One of the simplest demonstrations of the Monte Carlo technique is the estimation of π. By generating random points and analyzing their geometric distribution, an approximation of π can be obtained.

---

# 2. Theory

Consider a circle of radius 1 centered at the origin.

The equation of the circle is:

\[
x^2+y^2=1
\]

The area of the circle is:

\[
A_{circle}=\pi r^2=\pi
\]

Since the radius is 1,

\[
A_{circle}=\pi
\]

The circle is enclosed within a square of side length 2.

The area of the square is:

\[
A_{square}=2\times2=4
\]

Therefore,

\[
\frac{A_{circle}}{A_{square}}
=
\frac{\pi}{4}
\]

which gives

\[
\pi
=
4\times
\frac{\text{Points Inside Circle}}
{\text{Total Points}}
\]

This relationship forms the basis of the Monte Carlo estimation.

---

# 3. Methodology

The following algorithm was implemented:

1. Generate N random points uniformly distributed in the square [-1,1] × [-1,1].
2. Check whether each point satisfies

\[
x^2+y^2 \le 1
\]

3. Count the number of points inside the circle.
4. Estimate π using

\[
\pi
=
4\times
\frac{\text{Points Inside Circle}}
{\text{Total Points}}
\]

5. Repeat for different sample sizes.
6. Analyze the resulting error.

---

# 4. Implementation

The simulation was implemented in Python using:

- NumPy
- Matplotlib

NumPy was used for efficient random number generation and array operations, while Matplotlib was used for visualization.

---

# 5. Results

## Example Estimate

For a simulation with 100,000 random points:

| Quantity | Value |
|-----------|---------|
| Total Points | 100000 |
| Points Inside Circle | 78562 |
| Estimated π | 3.14248 |
| Actual π | 3.14159 |
| Error | 0.00089 |

(Note: values may vary between runs because of randomness.)

---

## Visualization

### Random Point Distribution

The generated points form a visual approximation of the circle inside the square.

Insert image:

![Circle Simulation](figures/circle_simulation.png)

---

### Convergence Analysis

As the number of samples increases, the estimate approaches the true value of π.

Insert image:

![Convergence Plot](figures/convergence_plot.png)

---

# 6. Error Analysis

The absolute error is defined as

\[
\text{Error}
=
|\pi_{actual}-\pi_{estimated}|
\]

Monte Carlo methods exhibit a convergence rate proportional to

\[
\frac{1}{\sqrt{N}}
\]

where N is the number of samples.

This means that increasing the sample size by a factor of 100 typically reduces the error by only a factor of 10.

Although convergence is relatively slow, Monte Carlo methods remain powerful because they can solve problems that are difficult for deterministic numerical techniques.

---

# 7. Applications

Monte Carlo methods are widely used in:

- Statistical Physics
- Computational Physics
- Radiation Transport
- Astrophysics
- Financial Modeling
- Machine Learning
- Quantum Simulations
- Engineering Analysis

---

# 8. Conclusion

The Monte Carlo method successfully estimated the value of π using random sampling. The results demonstrated that increasing the number of samples improves accuracy and reduces error. The project illustrates fundamental concepts in computational physics, numerical methods, probability theory, and scientific computing.

---

# 9. Future Work

Possible extensions include:

- Monte Carlo integration of arbitrary functions
- Importance sampling
- Metropolis algorithm
- Markov Chain Monte Carlo (MCMC)
- Parallel Monte Carlo simulations
- Applications to statistical mechanics

---

# References

1. Newman, M. Computational Physics.
2. Landau, Paez, and Bordeianu. Computational Physics.
3. Numerical Recipes in Python.
4. Monte Carlo Methods in Statistical Physics.
