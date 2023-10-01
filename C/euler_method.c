#include <stdio.h>    

/* 
Change from constants to values supposed by the user at runtime.
*/

#define h 0.01
#define n 1000

#define t0 0.0
#define y0 0.0

double function(double t, double y) { 

    /* ANALYTIC SOLUTION: 
    y' = 1+t-2ty
    y = exp(-t^2)int(exp(t^2)(1+t))dt
    */

    double func_value = 1.0 + t - 2.0 * t * y;
    return func_value;
};

int forward_euler(double (*fn) (double, double), double T_INITIAL, double Y_INITIAL, double STEP_SIZE, int STEPS) {

    double domain[STEPS], output[STEPS];
    domain[0] = T_INITIAL;
    output[0] = Y_INITIAL;
    
    for (int j = 1; j <= STEPS; j++) {
        domain[j] = T_INITIAL + j*STEP_SIZE;
    };
    
    printf("(%f, %f)\n",  domain[0], output[0]);

    for ( int i = 0; i < STEPS; i++) {
        output[i+1] = output[i] + fn(domain[i], output[i])*STEP_SIZE;
        printf("(%.17f, %.17f)\n", domain[i+1], output[i+1]);
    };
    
    return 0;
};

int main(void) {
    forward_euler(function, t0, y0, h, n);

    return 0;
};
