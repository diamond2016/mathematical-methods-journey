"""Plot f(x) = 1/(1 + cos^2(x).

Features:
np.arange(0, 2*pi + 1e-9, pi/2) generates [0, π/2, π, 3π/2, 2π]. 
The tiny 1e-9 guard prevents floating-point drift from dropping the final 2π tick (since 2*pi may come out as 6.283185300000001 and get excluded by the exclusive upper bound).
set_xticklabels replaces the numeric tick labels with nicely formatted LaTeX fractions.
"""

from math import pi

import matplotlib.pyplot as plt
import numpy as np


def f(x: float) -> float:
    """Return the value of 1/(cos^2(x)+1) at x."""
    return 1/(1 + (np.cos(x))**2)



def main() -> None:
    """Set up and display the plot."""
    ax = plt.gca()
    ax.set_xlim(0, 2*pi)
    ax.set_ylim(0, 1.5)

    # Tick marks at multiples of pi/2
    ax.set_xticks(np.arange(0, 2*pi + 1e-9, pi/2))
    ax.set_xticklabels([r"$0$", r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"])

    x = np.linspace(-0, 2*pi, 500)
    y = f(x)

    ax.plot(x, y, color="steelblue", linewidth=2, label=r"$f(x) = \frac{1}{1 + cos^2x}$")


    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(True, linestyle="--", alpha=0.1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(r"$f(x) = \frac{1}{1 + cos^2x}$")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

