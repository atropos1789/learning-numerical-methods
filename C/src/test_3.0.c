#include <stdio.h>
#include "libeuler_functions.h"

int main(void)
{
    runge_kutta(function, 0.0, 0.0, 0.001, 100000);
    return 0;
};
