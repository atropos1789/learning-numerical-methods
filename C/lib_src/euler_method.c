#include <stdio.h>    

/*
The Euler Method for approximating the solution to the IVP 
y' = f(t,y), y(t_0) = y_0
is
y_{n+1} = y_n + h*f(t_n, y_n)
*/

int forward_euler(double (*fn) (double, double), double T_INITIAL, double Y_INITIAL, double STEP_SIZE, int STEPS)
{
    double domain[STEPS+1], output[STEPS+1];
    domain[0] = T_INITIAL;
    output[0] = Y_INITIAL;
    
    for (int j = 1; j <= STEPS; j++)
    {
        domain[j] = T_INITIAL + j*STEP_SIZE;
        // printf("STEP: %f\n",domain[j]);
    };
    
    printf("(%f, %f)\n",  domain[0], output[0]);

    for ( int i = 0; i < STEPS; i++)
    {
        output[i+1] = output[i] + fn(domain[i], output[i])*STEP_SIZE;
        printf("(%.17f , %.17f)\n", domain[i+1], output[i+1]);
        // printf("%.17f\n", domain[i+1]);
    };
    
    return 0;
};
