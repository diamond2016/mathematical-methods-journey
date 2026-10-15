Using this LaTeX instructions:

- \int	Integral sign
- \frac{1}{x+1}	Fraction 1/(x+1)
- \,	Small space before dx (optional but cleaner)
- dx	Differential
- \ln	Natural log
- \	x+1\

For lower and upper bounds (definite integral):
- \int_{\text{lower}}^{\text{upper}} f(x) \, dx

And applying to the primitive:
- \Big|_{lower}^{upper}

$\int \frac{1}{x+1} \, dx = \ln|x+1| + C$

Example:

$\int_{0}^{4} \frac{1}{x+1} \, dx = \ln|x+1|\Big|_{0}^{4} = \ln(5) - ln(1) = ln(5)$

$\int_{0}^{1} \frac{1}{x+1} \, dx = \ln|x+1| \Big|_{0}^{1} = \ln(2)$