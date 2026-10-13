# Complex Numbers Review

# Week 1: Complex Numbers Review

## 1. Definitions
A complex number $z$ is an element of the set $\mathbb{C}$, expressed as:
z = x + iy where:
* $x = \text{Re}(z)$ is the **real part**.
* $y = \text{Im}(z)$ is the **imaginary part**.
* $i$ is the imaginary unit, defined by $i^2 = -1$.

## 2. Polar Form
Any complex number can be represented in polar coordinates $(r, \theta)$:$$z = r(\cos \theta + i \sin \theta) = re^{i\theta}$$Where:
* $r = |z|$ is the **modulus** (distance from the origin).
* $\theta = \arg(z)$ is the **phase/argument** (angle from the positive real axis).

## 3. Key Properties
### Modulus
The magnitude of $z$ is calculated as:$$|z| = \sqrt{x^2 + y^2}$$
### Phase (Argument)
The angle $\theta$ is typically calculated using the `atan2` function to handle all quadrants:$$\theta = \operatorname{atan2}(y, x)$$

### Operations
* **Addition:** $(x_1 + iy_1) + (x_2 + iy_2) = (x_1 + x_2) + i(y_1 + y_2)$
* **Multiplication (Geometric):** Multiplying by $re^{i\theta}$ scales the magnitude by $r$ and rotates the plane by $\theta$.

---
*Next step: Implement these operations in `exercise.ipynb`.*
```

---

### 4. Template for `week01-complex-numbers/exercise.ipynb`
When you create your notebook, structure it like this (you can do this by creating cells in Jupyter):

1.  **Cell 1 (Markdown):** 
    `# Exercise: Complex Number Geometry`
    `Goal: Represent complex numbers in the plane and visualize addition/multiplication.`

2.  **Cell 2 (Code):** 
    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    # Setup the plot
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axhline(0, color='black', lw=1)
    ax.axvline(0, color='black', lw=1)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.grid(True, linestyle='--')
    ```

3.  **Cell 3 (Code):** 
    ```python
    # Define two complex numbers
    z1 = 2 + 1j
    z2 = -1 + 2j

    # Perform operations
    z_sum = z1 + z2
    z_prod = z1 * z2

    # Plotting logic (to be completed by you)
    # ...