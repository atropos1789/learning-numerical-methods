#include <stdio.h>

double function(double t, double y) 
{ 
    /* ANALYTIC SOLUTION: 
    y' = 1+t-2ty
    y = exp(-t^2)int(exp(t^2)(1+t))dt
    */

    double func_value = 1.0 + t - 2.0 * t * y;
    return func_value;
};

int main(void)
{
    forward_euler(function, 0.0, 0.0, 0.01, 1000);
    improved_euler(function, 0.0, 0.0, 0.01, 1000);
    return 0;
};
