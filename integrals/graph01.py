import matplotlib.pyplot as plt
import numpy as np

"""
set_xlim(-0.95, 5)	Shows the asymptote at x = -1 and the interesting behavior near it
x = np.linspace(-0.95, 5, 1000)	Dense sampling for a smooth curve
y = np.log(1 / (x + 1))	The actual function
ax.plot(x, y, ...)	Draws the curve
ax.axvline(-1, ...)	Dashed red line marking the vertical asymptote
plt.legend()	Shows the function label and asymptote annotation
Updated title	Reflects the actual function
The plot will show ln(1/(x+1)) approaching +∞ as x → -1⁺ and slowly decreasing toward 0 as x → ∞.
"""

# Setup plot
ax = plt.gca()
ax.set_xlim(-2, 5)
ax.set_ylim(-5, 5)

# Generate data: ln(1/(x+1)) is defined for x > -1
x = np.linspace(-0.95, 5, 1000)
y = np.log(1 / (x + 1))

# Plot the curve
ax.plot(x, y, color='steelblue', linewidth=2, label=r'$\ln\!\left(\frac{1}{x+1}\right)$')

# Vertical asymptote at x = -1
ax.axvline(-1, color='red', linestyle='--', linewidth=1, label=r'asymptote $x = -1$')

# Adding labels
# plt.text(x, y, "label_text")


# Add grid and labels for clarity
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'$\ln\!\left(\frac{1}{x+1}\right)$ Visualization')
plt.legend()

plt.show()
