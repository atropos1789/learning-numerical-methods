#include <stdio.h>

/*
The Improved Euler Method for approximating the solution to the IVP 
y' = f(t,y), y(t_0) = y_0
is
y_{n+1} = y_n + 0.5h( f(t_n, y_n) + f(t_n + h, y_n + h*f(t_n,y_n) ) )
*/

int improved_euler(double (*fn) (double, double), double T_INITIAL, double Y_INITIAL, double STEP_SIZE, int STEPS)
{
    double domain[STEPS+1], output[STEPS+1];
    domain[0] = T_INITIAL;
    output[0] = Y_INITIAL;
    
    for (int j = 1; j < (STEPS+1); j++)
    {
        domain[j] = T_INITIAL + j*STEP_SIZE;
    };
    
    printf("(%f, %f)\n",  domain[0], output[0]);

    for ( int i = 0; i < STEPS; i++)
    {
        double k1 = fn(domain[i], output[i]);
        double k2 = fn(domain[i] + STEP_SIZE, output[i] + STEP_SIZE*k1);
        output[i+1] = output[i] + 0.5*STEP_SIZE*(k1 + k2);
        printf("(%.17f , %.17f)\n", domain[i+1], output[i+1]);
    };
    
    return 0;
};
