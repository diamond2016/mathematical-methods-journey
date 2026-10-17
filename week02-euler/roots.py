"""Visualize the n-th roots of a complex number on the complex plane.

Features:
    - Computes all n distinct roots using Euler's formula
    - Plots roots, the enclosing circle, and the regular polygon
"""

import numpy as np
import matplotlib.pyplot as plt


def visualize_n_th_roots(z: complex, n: int) -> None:
    """Compute and plot the n-th roots of a complex number.

    Calculates all n distinct roots of ``z`` using Euler's formula and
    displays them on the complex plane together with the enclosing
    circle and the regular polygon connecting the roots.

    Parameters
    ----------
    z : complex
        The complex number whose n-th roots are computed.
    n : int
        The order of the root. Must be a positive integer.

    Raises
    ------
    ValueError
        If ``n`` is not a positive integer.

    Side Effects
    ------------
    Prints the computed roots to stdout and displays a matplotlib
    figure.

    Examples
    --------
    >>> visualize_n_th_roots(-8 + 0j, 3)
    """
    if n <= 0:
        msg = f"n must be a positive integer, got {n}"
        raise ValueError(msg)

    # 1. Compute the modulus and principal argument
    r = np.abs(z)
    theta = np.angle(z)
    
    # 2. Modulus of the n-th roots
    R = r ** (1 / n)
    
    # 3. Generate the n roots via the exponential formula
    k = np.arange(n)
    arguments = (theta + 2 * np.pi * k) / n
    roots = R * np.exp(1j * arguments)
    
    # Print results to the console
    print(f"=== {n}-th roots of z = {z} ===")
    for i, w in enumerate(roots):
        print(f"w_{i} = {w.real:.4f} + {w.imag:.4f}i  (Polar form: R = {R:.4f}, arg = {arguments[i]:.4f} rad)")
    
    # 4. Create the matplotlib figure
    plt.figure(figsize=(7, 7))
    
    # Draw the circle of radius R
    circle = plt.Circle((0, 0), R, color='skyblue', linestyle='--', fill=False, linewidth=1.5, label=f'Circle of radius R = {R:.2f}')
    plt.gca().add_patch(circle)
    
    # Trace the regular polygon connecting the roots
    polygon_x = np.append(roots.real, roots.real[0])
    polygon_y = np.append(roots.imag, roots.imag[0])
    plt.plot(polygon_x, polygon_y, color='orange', linestyle='-', linewidth=1, alpha=0.7, label='Regular polygon')
    
    # Plot the points corresponding to the roots
    plt.scatter(roots.real, roots.imag, color='red', s=70, zorder=5, label=f'{n}-th roots')
    
    # Labels for each root
    for i, w in enumerate(roots):
        plt.annotate(f"  w_{i}", (w.real, w.imag), textcoords="offset points", xytext=(5, 5), ha='left', fontweight='bold', fontsize=11)
        
    # Configure axes and grid
    limit = R * 1.4 if R > 1 else 1.5
    plt.xlim(-limit, limit)
    plt.ylim(-limit, limit)
    plt.axhline(0, color='black', linewidth=1, linestyle='-')
    plt.axvline(0, color='black', linewidth=1, linestyle='-')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.gca().set_aspect('equal', adjustable='box')
    
    # Title and legend
    plt.title(f"Geometric Visualization of the {n}-th Roots of z = {z}", fontsize=12, fontweight='bold', pad=15)
    plt.xlabel("Real Part", fontsize=10)
    plt.ylabel("Imaginary Part", fontsize=10)
    plt.legend(loc='upper right')
    
    # Show the figure
    plt.show()


# Practical example: compute and visualize the cube roots (n = 3) of z = -8
visualize_n_th_roots(z=-8 + 0j, n=3)

# You can try other examples by modifying the parameters, e.g.:
# visualize_n_th_roots(z=1 + 1j, n=4)  # Fourth roots of 1 + i
