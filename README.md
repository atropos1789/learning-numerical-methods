# learning-numerical-methods

This is a repository I will be using for learning how to implement various numerical schemes using C, C++, and Fortran.

The algorithms implemented will be the numerical integration schemes discussed in Chapter 8 of Differential Equations by Boyce and Diprima and Chapter 6 of Numerical Analysis by Atkinson, to solve the IVP `y' = f(t,y), y(t0) = y0`.

Notationally, let `f(t_n, y_n) = f_n`


- Euler's Method

```
k1 = f(t_n, y_n)
y_n+1 = y_n + h * k1
```

- Improved Euler Method/ Heun's Method

```
k1 = f(t_n, y_n)
k2 = f( t_n + h, y_n + h * k1)
y_n+1 = y_n + h * (1/2)( k1 + k2 )
```

- RK4

```
k1 = f( t_n, y_n ) 
k2 = f( t_n + 0.5 * h, y_n + 0.5 * h * k1 )
k3 = f( t_n + 0.5 * h, y_n + 0.5 * h * k2 )
k4 = f( t_n + h, y_n + h * k3 )
y_n+1 = y_n + h * (1/6)( k1 + 2 * k2 + 2 * k3 + k4)
```

- Adams-bashforth
- Adams-moulton
- predictor-corrector
