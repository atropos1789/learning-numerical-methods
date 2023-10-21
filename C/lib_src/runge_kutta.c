#include <stdio.h>
/*
The Fourth Order Runge-Kutta approximation to the IVP y' = f(t,y)

k1 = f( t_n, y_n ) 
k2 = f( t_n + 0.5 * h, y_n + 0.5 * h * k1 )
k3 = f( t_n + 0.5 * h, y_n + 0.5 * h * k2 )
k4 = f( t_n + h, y_n + h * k3 )
y_n+1 = y_n + h * 1/6 * ( k1 + 2 * k2 + 2 * k3 + k4 )

*/



int runge_kutta(double (*fn) (double, double), double T_INITIAL, double Y_INITIAL, double STEP_SIZE, int STEPS)
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
        double k2 = fn(domain[i] + 0.5*STEP_SIZE, output[i] + 0.5*STEP_SIZE*k1);
        double k3 = fn(domain[i] + 0.5*STEP_SIZE, output[i] + 0.5*STEP_SIZE*k2);
        double k4 = fn(domain[i] + STEP_SIZE, output[i] + STEP_SIZE*k3);
        output[i+1] = output[i] + STEP_SIZE*(1.0/6.0)*(k1 + 2*k2 + 2*k3 + k4);
        printf("(%.17f , %.17f)\n", domain[i+1], output[i+1]);
    };
    
    return 0;
};
