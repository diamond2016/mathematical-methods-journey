"""Visualize the circle of radius R and center (0,0j), and the mapping of circle with map f(z) = 1/z.

Features:
    - Plots the circle (red), and the mapping of the circle (green)
"""

from typing import Callable
import numpy as np
import matplotlib.pyplot as plt


def f(z: complex) -> complex:
    """Return the value of 1/z at z."""
    return 1 / z


def c_circle(theta: np.ndarray, w: complex, r: float) -> np.ndarray:
    """Return the array of numbers z of argument theta, in the circle of radius r and center w.
    
    z = w + r * e^(j * theta)
    """
    return w + r * np.exp(1j * theta)


def setup_complex_axes(ax: plt.Axes, title: str) -> None:
    """Apply common formatting rules for the complex plane to a given axis."""
    ax.set_aspect('equal')  # Mantiene le proporzioni corrette
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.axhline(0, color='black', linewidth=0.8)  # Asse Reale
    ax.axvline(0, color='black', linewidth=0.8)  # Asse Immaginario
    ax.set_xlabel('Real axis (Re)')
    ax.set_ylabel('Imaginary axis (Im)')
    ax.set_title(title)


def visualize_circle(ax: plt.Axes, z_points: np.ndarray, w: complex) -> None:
    """Plot the circle in the complex plane on the provided axes."""
    if ax is None:
        return

    # Estrazione vettoriale di X e Y
    x = z_points.real
    y = z_points.imag

    # Disegna il bordo del cerchio in rosso e il riempimento in azzurro
    ax.plot(x, y, color='red', linewidth=2, label='Circle contour')
    ax.fill(x, y, color='lightblue', alpha=0.5)

    # Evidenzia il centro w
    ax.plot(w.real, w.imag, 'ko', label=f'Center w ({w.real}+{w.imag}j)')
    ax.legend()
    
    setup_complex_axes(ax, 'Original Circle in Complex Plane')


def visualize_map(ax: plt.Axes, z_points: np.ndarray, mapping_func: Callable[[complex], complex]) -> None:
    """Plot the mapped points in the complex plane using the provided mapping function."""
    if ax is None:
        return

    # Applica la funzione di mappatura passata come argomento in modo vettoriale
    mapped_points = mapping_func(z_points)

    # Estrazione vettoriale di X e Y trasformati
    x_mapped = mapped_points.real
    y_mapped = mapped_points.imag

    # Disegna la mappa risultante in verde
    ax.plot(x_mapped, y_mapped, color='green', linewidth=2, label=f'Mapping: {mapping_func.__name__}(z)')
    ax.legend()
    
    setup_complex_axes(ax, 'Mapped Circle in Complex Plane')


def main():
    center: complex = 0 + 0j
    radius: float = 2.0

    if radius <= 0:
        raise ValueError("Radius r must be a positive number.")

    # 1. Genera 100 angoli in modo vettoriale da 0 a 2*pi
    theta_values = np.linspace(0, 2 * np.pi, 100)

    # 2. Genera i punti della circonferenza di partenza
    z_points = c_circle(theta_values, center, radius)

    # 3. Inizializza la figura con 2 subplot affiancati (1 riga, 2 colonne)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # 4. Chiama le funzioni di visualizzazione passando i rispettivi assi
    visualize_circle(ax=ax1, z_points=z_points, w=center)
    visualize_map(ax=ax2, z_points=z_points, mapping_func=f)

    # Ottimizza gli spazi tra i grafici e mostra la figura
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

