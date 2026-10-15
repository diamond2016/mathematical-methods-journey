import matplotlib.pyplot as plt
import numpy as np

"""Plot f(x) = 1/(x+1) and its antiderivative h(x) = ln|x+1|.

Features:
    - Vertical asymptote at x = -1
    - Filled area: definite integral ∫₁⁴ 1/(x+1) dx ≈ 0.92
    - Vertical line segments at the integration bounds (x = 1, x = 4)
"""

# function to study
def f(x):
    return 1 / (x + 1)

# integral of the function: ∫ 1/(x+1) dx = ln|x+1|
def h(x):
    return np.log(np.abs(x + 1))

# Setup plot
ax = plt.gca()
ax.set_xlim(-2, 5)
ax.set_ylim(-5, 5)

# Generate data: ln(1/(x+1)) is defined for x > -1
x = np.linspace(-0.95, 5, 1000)
y = f(x)
y_h = h(x)

# Plot the curve
ax.plot(x, y, color='steelblue', linewidth=2, label=r'$f(x) = \frac{1}{x+1}$')

# Plot the integral curve
ax.plot(x, y_h, color='seagreen', linewidth=2, label=r'$h(x) = \ln|x+1|$')

# Vertical asymptote at x = -1
ax.axvline(-1, color='red', linestyle='--', linewidth=1, label=r'asymptote $x = -1$')

# Fill the area under the curve from x=1 to x=4
ax.fill_between(x, y, 0, where=(x >= 1) & (x <= 4), color='steelblue', alpha=0.3, label=r'$\int_{1}^{4} \frac{1}{x+1}\,dx \, \approx 0.92$')

# Vertical line segments from y=0 to f(x) at the bounds
ax.plot([1, 1], [0, f(1)], color='black', linewidth=1.5)
ax.plot([4, 4], [0, f(4)], color='black', linewidth=1.5)

# Adding labels
# plt.text(x, y, "label_text")


# Add grid and labels for clarity
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.1)
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'$f(x) = \frac{1}{x+1}$ and its integral')
plt.legend()

# Show plot
plt.show()

