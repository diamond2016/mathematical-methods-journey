import sympy as sp

# Define symbolic variables
x, y = sp.symbols('x y', real=True)
z = x + sp.I * y

# Define a complex function f(z), e.g., f(z) = z^2 = (x+iy)^2 = (x^2 - y^2) + i(2xy)
f = z**2

# Separate real (u) and imaginary (v) parts
u = sp.re(f)
v = sp.im(f)

# Compute partial derivatives
du_dx = sp.diff(u, x)
dv_dy = sp.diff(v, y)
du_dy = sp.diff(u, y)
dv_dx = sp.diff(v, dx) # note: diff(v, x)

print(f"u(x,y) = {u}")
print(f"v(x,y) = {v}")
print(f"du/dx = {du_dx}, dv/dy = {dv_dy}")
print(f"du/dy = {du_dy}, -dv/dx = {-dv_dx}")

# Check conditions
cond1 = sp.simplify(du_dx - dv_dy)
cond2 = sp.simplify(du_dy + dv_dx)

if cond1 == 0 and cond2 == 0:
    print("-> Cauchy-Riemann equations are satisfied!")
else:
    print("-> Cauchy-Riemann equations are NOT satisfied.")