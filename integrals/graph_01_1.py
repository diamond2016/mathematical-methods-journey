"""Plot f(x) = 1/(x+1) and its antiderivative h(x) = ln|x+1|.

Features:
    - Vertical asymptote at x = -1
    - Filled area: definite integral from 1 to 4
    - Vertical line segments at the integration bounds
"""

import matplotlib.pyplot as plt
import numpy as np


def f(x: float) -> float:
    """Return the value of 1/(x+1) at x."""
    return 1 / (x + 1)


def h(x: float) -> float:
    """Return the antiderivative ln|x+1| of f at x."""
    return np.log(np.abs(x + 1))


def main() -> None:
    """Set up and display the plot."""
    ax = plt.gca()
    ax.set_xlim(-2, 5)
    ax.set_ylim(-5, 5)

    x = np.linspace(-0.95, 5, 1000)
    y = f(x)
    y_h = h(x)

    ax.plot(x, y, color="steelblue", linewidth=2, label=r"$f(x) = \frac{1}{x+1}$")
    ax.plot(x, y_h, color="seagreen", linewidth=2, label=r"$h(x) = \ln|x+1|$")
    ax.axvline(-1, color="red", linestyle="--", linewidth=1, label=r"asymptote $x = -1$")

    ax.fill_between(
        x, y, 0,
        where=(x >= 1) & (x <= 4),
        color="steelblue", alpha=0.3,
        label=r"$\int_{1}^{4} \frac{1}{x+1}\,dx \, \approx 0.92$",
    )
    ax.plot([1, 1], [0, f(1)], color="black", linewidth=1.5)
    ax.plot([4, 4], [0, f(4)], color="black", linewidth=1.5)

    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(True, linestyle="--", alpha=0.1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(r"$f(x) = \frac{1}{x+1}$ and its integral")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

