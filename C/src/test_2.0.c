#include <stdio.h>
#include "libeuler_functions.h"

int main(void)
{
    improved_euler(function, 0.0, 0.0, 0.001, 100000);
    return 0;
};
