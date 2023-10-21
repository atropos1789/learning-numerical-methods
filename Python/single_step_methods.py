import numpy as np

#Numerical solutions to 1st order DEs
def f(t,y): return 1+t-2*t*y

#Forward Euler:
def Forward_Euler(f, t0, y0, h, n):
    T = np.linspace(t0, n*h, n)
    Y = np.array([y0])
    for k in range(n):
        k1 = f(T[k], Y[k])
        Y = np.append(Y, Y[k] + h*k1)
    return (T, Y)

#Improved Euler:
def Improved_Euler(f, t0, y0, h, n):
    T = np.linspace(t0, n*h, n)
    Y = np.array([y0])
    for k in range(n):
        k1 = f(T[k], Y[k])
        k2 = f(T[k+1], Y[k] + h*k1)   
        Y = np.append(Y, Y[k] + 0.5*h*(k1 + k2))
    return (T, Y)

#RK4:
def RK4(f, t0, y0, h, n):
    T = np.linspace(t0, n*h, n)
    Y = np.array([y0])
    for k in range(n):
        k1 = f(T[k], Y[k])
        k2 = f(T[k] + 0.5*h, Y[k] + 0.5*h*k1)
        k3 = f(T[k] + 0.5*h, Y[k] + 0.5*h*k2)
        k4 = f(T[k] + h, Y[k] + h*k3)
        Y = np.append(Y, Y[k] + (h/6)*(k1 + 2*k2 + 2*k3 + k4))
    return (T, Y)
