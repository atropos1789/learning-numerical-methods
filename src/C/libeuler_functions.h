#include <stdio.h>

/*
The Euler Method for approximating the solution to the IVP 
y' = f(t,y), y(t_0) = y_0
is
y_{n+1} = y_n + h*f(t_n, y_n)
*/

int forward_euler(double (*fn) (double, double), double T_INITIAL, double Y_INITIAL, double STEP_SIZE, int STEPS);

/*
The Improved Euler Method for approximating the solution to the IVP 
y' = f(t,y), y(t_0) = y_0
is
y_{n+1} = y_n + 0.5h( f(t_n, y_n) + f(t_n + h, y_n + h*f(t_n,y_n) ) )
*/

int improved_euler(double (*fn) (double, double), double T_INITIAL, double Y_INITIAL, double STEP_SIZE, int STEPS);

