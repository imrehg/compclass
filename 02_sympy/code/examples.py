from sympy import *

# Defining symbols
x = symbols("x")
y, z = symbols("y z")

# Equation
f = x**2 - 3 * y
print "Equation f = ", f

# Substitution
print "Subs x = 2:", f.subs({x: 2})
print "Subs x = 2, y = 1:", f.subs({x: 2, y:1})
print "Exp(I*x), x = pi:", exp(I*x).subs(x,pi)
print "Now with x = pi/4: ", exp(I*x).subs(x,pi/4)
print "Evalf : ", exp(I*x).subs(x,pi/4).evalf(5)

# Expanding expression
print "Expand: ", ((x+y)**3 * (x + y)).expand()

# Simplify
a = 1/x + (x*sin(x) - 1)/x
print "Simplify: ", simplify(a)

# Solving equation
print "Solve no1: ", solve(Eq(x**3 + 2*x**2 + 4*x + 8, 0), x)
print "Solve no2: ", solve(x**3 + 2*x**2 + 4*x + 8, x)
print "Solve no3: ", solve(x**2 - 3 * y, x)
print "Solve no4: ", solve(f, x)

# Solving system of equations
solve([Eq(x + 5*y, 2), Eq(-3*x + 6*y, 15)], [x, y])
g = [x + 5*y - 2, -3*x + 6*y - 15]
solution = solve(g, [x, y])
print "System of eq.:", solution
print "Eq. 1 with y:", g[0].subs(y,solution[y])
print "Eq. 2 with y:", g[1].subs(y,solution[y])

# Differentiate
print "Differentiate f:", diff(f, x)

# Integrate
print "Integrate f:", integrate(f, x)
print "Integrate f w/ x=(0,1):", integrate(f.subs({y:1}), (x, 0, 1))
print "Integrate f w/ x=(0,1), y=1:", integrate(f.subs({y:1}), (x, 0, 1))

# Taylor series
s = sin(x)**2
ts = s.series(x, 0, 6)
print "Taylor series", ts
