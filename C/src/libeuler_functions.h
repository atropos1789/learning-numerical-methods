#include <stdio.h>

int forward_euler(double (*fn) (double, double), double T_INITIAL, double Y_INITIAL, double STEP_SIZE, int STEPS);

int improved_euler(double (*fn) (double, double), double T_INITIAL, double Y_INITIAL, double STEP_SIZE, int STEPS);

int runge_kutta(double (*fn) (double, double), double T_INITIAL, double Y_INITIAL, double STEP_SIZE, int STEPS);

double function(double t, double y) 
{ 
    /* ANALYTIC SOLUTION: 
    y' = 1+t-2ty
    y = exp(-t^2)int(exp(t^2)(1+t))dt
    */

    double func_value = 1.0 + t - 2.0 * t * y;
    return func_value;
};
