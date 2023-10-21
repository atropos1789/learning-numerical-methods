#%%
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#%%
#function, forward finite difference, central finite difference, backward finite difference
h = 0.01
X = np.arange(-4,4,h)

def g(x):
    return np.tanh(x)

#forward 1st and 2nd order fd
def Fdg(x): return (g(x+h) - g(x))/h
def Fddg(x): return (g(x+2*h) - 2*g(x+h) + g(x))/h**2

#central 1st and 2nd order fd
def Cdg(x): return (g(x+0.5*h) - g(x-0.5*h))/h
def Cddg(x): return (g(x+h) - 2*g(x) + g(x-h))/h**2

#backward 1st and 2nd order fd
def Bdg(x): return (g(x) - g(x-h))/h
def Bddg(x): return (g(x) - 2*g(x-h) + g(x-2*h))/h**2


fig, FX = plt.subplots()
FX.plot(X, g(X), label='g(x)')
FX.plot(X, Fdg(X), label='1st forward FD of g(x)')
FX.plot(X, Fddg(X), label='2nd forward FD of g(x)')
FX.plot(X, Cdg(X), label='1st central FD of g(x)')
FX.plot(X, Cddg(X), label='2nd central FD of g(x)')
FX.plot(X, Bdg(X), label='1st backward FD of g(x)')
FX.plot(X, Bddg(X), label='2nd backward FD of g(x)')
FX.set_xlabel('x')
FX.set_ylabel('y')
FX.set_title('finite difference methods')
FX.legend(loc="upper right")
#%%
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

#TODO: Multi-step methods, e.g. adams bashforth

#%%
#Solving a DE using FD 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import linalg as la

#choose h value, make X
h = 0.1
X = np.arange(0,1+h,h)

n=0
for n in range(len(X)):
    X[n] = round(X[n],2)
    n=+1

#defining the forcing function
def f(x):
    return np.sin(2*np.pi*x)

#constructing the A matrix
A = np.zeros((len(X),len(X)+2))
i = 0
for i in range(len(X)):
    A[i,i] = -1
    A[i,i+1] = 2
    A[i,i+2] = -1
    i =+1

#constructing the b vector
b = []
n = 0
for n in range(len(X)):
    b.append(f((n+1)*h))
    n=+1
b = np.array(b)
b = (h**2)*b

u = np.zeros(len(X)+2)
u[0] = 0 # = u(0) 
u[len(X)-1] = 0 # = u(L)

#uh oh this doesn't work 

#%%
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import linalg as linalg

#choose h value, make X
h = 0.001

#Domain
X = np.arange(0,1,h)
n = 0
for n in range( len(X) ) :
    X[n] = round(X[n],3)
    n=+1

#initial conditions
u0 = 0
u0prime = 2*np.pi
u1 = u0prime*h + u0
ivs = [u0, u1]

#inhomogeneous term g(x)
def g(x):
    return np.sin(2*np.pi*x)

#constructing the E matrix
E = np.zeros((len(X),len(X)+2))
i = 0
for i in range(len(X)) :
    E[i,i] = 1
    E[i,i+1] = -2
    E[i,i+2] = 1
    i =+1

#constructing the f vector
f = []
n = 0
for n in range(len(X)) :
    f.append(g((n+1)*h))
    n =+1
f = np.array(f)
f = (h**2)*f

#altering Eu = f to Au = b
A = np.delete(E, [0,1], axis=1)
G = np.delete(E, range(2,len(X)+2), axis=1)
G = G.dot(ivs)
b = f-G

#solving
m = linalg.solve(A,b)

#solution set
u = np.zeros(len(X)+2)
u[0] = u0 # = u(0) 
u[1] = u1 # = u(h)
k = 0
for k in range(len(X)) :
    u[k+2] = m[k]
    k =+1
u = np.delete(u, range(len(X),len(X)+2))

#plotting
fig, ux = plt.subplots()
ux.plot(X, u, label='u(x)')

#hey it worked

#%%
#analytic solution

#choose h value, make X
h = 0.001
X = np.arange(0,1,h)

def y(x) :
    return 3*x**3 - 2*x**2
n = 0
for n in range( len(X) ) :
    X[n] = round(X[n],3)
    n=+1


fig, yx = plt.subplots()
yx.plot(X, y(X), label='y(x)')

#%%
#solving the same ivp but just using a recurrence relation

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import linalg
from scipy import stats

#choose h value
h = 0.001

#Domain
X = np.arange(0,1,h)

#initial conditions
u0 = 0
u0prime = 0
u1 = u0prime*h + u0
approx = [u0, u1]

#inhomogeneous term g(x)
def g(x):
    return (18*x - 4)


for k in range(2,len(X)):
    entry = (h**2)*g((k-1)*h) + 2*approx[k-1] - approx[k-2]
    approx = np.append(approx, entry)
    k=+1
    

def y(x) :
    return 3*x**3 - 2*x**2


error = np.empty(len(approx))
real = y(X)
for k in range(0,len(approx)):
    error = np.append(error, (approx[k]-real[k]))
    k=+1


print(stats.describe(error))


fig, ux = plt.subplots()
ux.plot(X, approx)