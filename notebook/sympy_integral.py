#!/usr/bin/env python3
import sympy as sp

t = sp.symbols('t', real=True)
f = sp.Rational(1, 2) + sp.Rational(1, 2) * sp.cos(sp.pi * t / 2)
F = sp.integrate(f, (t, -10, 10))

print(F)
