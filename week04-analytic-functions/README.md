## Week 04: Analytic Functions & Cauchy-Riemann Equations

In this module, we transition from basic complex mappings and sequences to the core of complex analysis: differentiability and analyticity.

📚 Objectives & Key Concepts


1. Complex Differentiability 

($f'(z)$):Unlike real calculus, complex differentiability is an extremely rigid condition.A function $f(z)$ is differentiable at a point $z_0$ if the limit of the difference quotient exists independently of the direction from which $h \to 0$:$$f'(z_0) = \lim_{h \to 0} \frac{f(z_0 + h) - f(z_0)}{h}$$

2. The Cauchy-Riemann Equations:

Let $f(z) = u(x, y) + i v(x, y)$ be defined in a neighborhood of $z = x + iy$.

For $f(z)$ to be differentiable at $z_0$, the partial derivatives of $u$ and $v$ must satisfy the Cauchy-Riemann equations:$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$Theorem: If the partial derivatives of $u$ and $v$ are continuous and satisfy the Cauchy-Riemann equations in a domain, then $f(z)$ is analytic (holomorphic) in that domain.


3. Harmonic Functions:Real and imaginary parts ($u$ and $v$) of an analytic function satisfy Laplace's equation:$$\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$Such functions are called harmonic functions, and $v$ is known as the harmonic conjugate of $u$.


## 💡 Deep Dive: Holomorphicity vs. Analyticity

When studying complex analysis, you will frequently encounter the terms **holomorphic** and **analytic**. While they are often used interchangeably, they highlight two distinct perspectives of complex functions:

* **Holomorphic Function:** 

Focuses on **complex differentiability**. A function $f(z)$ is holomorphic in an open domain $D$ if it is complex-differentiable at every point in $D$ (satisfying the Cauchy-Riemann equations with continuous partial derivatives).

* **Analytic Function:** 

Focuses on **power series expansion**. A function $f(z)$ is analytic in an open domain $D$ if it can be represented by a convergent Taylor series in a neighborhood of every point in $D$.

### Which Concept Comes First?

In real calculus, a infinitely differentiable ($C^\infty$) function is not necessarily analytic. However, **in complex analysis, these two notions are strictly equivalent**:

$$\text{Holomorphic in } D \iff \text{Analytic in } D$$

1. **Logical Priority (Holomorphicity):** We start with **complex differentiability** (holomorphicity) because it requires only a local limit condition on the difference quotient and can be directly verified using the Cauchy-Riemann equations.
2. **Deep Consequence (Analyticity):** Thanks to *Cauchy's Integral Formula*, complex differentiability once implies infinite differentiability and local expressibility as a power series.

> **Terminology Note:** In modern mathematics, *holomorphic* is preferred when emphasizing differential geometry and the Cauchy-Riemann equations, whereas *analytic* is preferred when working with power series representations and analytic continuation.

```text
week04_analytic_functions/
├── README.md               # Theory and notes (this file)
├── exercise.ipynb          # Jupyter notebook with guided exercises
└── cauchy_riemann_check.py # Python script for numerical verification of C
```