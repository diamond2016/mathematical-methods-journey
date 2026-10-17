"""Test the numerical functions and plot in ``integrals.graph_1``."""

import matplotlib.pyplot as plt
import numpy as np
import pytest

from integrals import graph_01_1


@pytest.mark.parametrize(
    ("x", "expected"),
    [(0.0, 1.0), (1.0, 0.5), (-2.0, -1.0)],
)
def test_f_returns_reciprocal_values(x: float, expected: float) -> None:
    """Return the reciprocal values for inputs away from the asymptote."""
    assert graph_01_1.f(x) == pytest.approx(expected)


def test_f_accepts_numpy_arrays() -> None:
    """Evaluate the function elementwise for plotting arrays."""
    x = np.array([0.0, 1.0, -2.0])

    np.testing.assert_allclose(graph_01_1.f(x), [1.0, 0.5, -1.0])


@pytest.mark.parametrize(
    ("x", "expected"),
    [(0.0, 0.0), (1.0, np.log(2.0)), (-3.0, np.log(2.0))],
)
def test_h_returns_log_absolute_values(x: float, expected: float) -> None:
    """Return the logarithm of the absolute shifted input."""
    assert graph_01_1.h(x) == pytest.approx(expected)


def test_main_builds_and_displays_plot(monkeypatch: pytest.MonkeyPatch) -> None:
    """Build the expected plot and invoke the display function."""
    figure, axes = plt.subplots()
    show_calls: list[None] = []
    monkeypatch.setattr(plt, "show", lambda: show_calls.append(None))

    try:
        graph_01_1.main()

        assert axes.get_xlim() == (-2.0, 5.0)
        assert axes.get_ylim() == (-5.0, 5.0)
        assert axes.get_title() == r"$f(x) = \frac{1}{x+1}$ and its integral"
        _, labels = axes.get_legend_handles_labels()
        assert len(labels) == 4
        assert len(axes.collections) == 1
        assert show_calls == [None]
    finally:
        plt.close(figure)
