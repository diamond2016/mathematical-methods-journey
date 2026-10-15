"""Plot f(x) = cosx/(1 + sinx) and its antiderivative h(x) = ln|1 + sinx|.

Features:
    - Vertical asymptote at x = 3/2 pi
"""
from math import pi

import matplotlib.pyplot as plt
import numpy as np


def f(x: float) -> float:
    """Return the value of 1/(x+1) at x."""
    return np.cos(x)/(1 + np.sin(x))


def h(x: float) -> float:
    """Return the antiderivative ln|x+1| of f at x."""
    return np.log(np.abs(np.sin(x) + 1))


def main() -> None:
    """Set up and display the plot."""
    ax = plt.gca()
    ax.set_xlim(0, 2*pi)
    ax.set_ylim(-5, 5)

    x = np.linspace(-0, 2*pi, 500)
    y = f(x)
    y_h = h(x)

    ax.plot(x, y, color="steelblue", linewidth=2, label=r"$f(x) = \frac{1}{x+1}$")
    ax.plot(x, y_h, color="seagreen", linewidth=2, label=r"$h(x) = \ln|x+1|$")
    ax.axvline((3/2)*pi, color="red", linestyle="--", linewidth=1, label=r"asymptote x = 3\2 pi")


    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(True, linestyle="--", alpha=0.1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(r"$f(x) = \frac{cos(x)}{1+sin(x)}$ and its integral")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

