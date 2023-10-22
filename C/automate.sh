#!/bin/bash

cat << \EOF > src/test.1.0.0.c
#include "libeuler_functions.h"

int main(void)
{
improved_euler( function, 0, 0, 0.001, 500000);
return 0;
};
EOF

cat << \EOF > src/test.2.0.0.c
#include "libeuler_functions.h"

int main(void)
{
runge_kutta( function, 0, 0, 0.001, 500000);
return 0;
};
EOF

gcc -Wall -Werror src/test.1.0.0.c -o bin/test.1.0.0 bin/clibeuler.so
gcc -Wall -Werror src/test.2.0.0.c -o bin/test.2.0.0 bin/clibeuler.so

# wait lemme change order of execution
# would suck if that was it
# yep that does affect it
# that sucks

# if i execute them outside of a shell script, its averaging
# test1: 0.97
# test2: 1.00

# but inside the shell script, whichever goes first is ~0.95 and whichever goes second is ~0.98

/bin/time -v ./bin/test.1.0.0 > /tmp/test.1.0.0.txt 2> data/time.1.0.0.txt
/bin/time -v ./bin/test.2.0.0 > /tmp/test.2.0.0.txt 2> data/time.2.0.0.txt


mv '/tmp/test.1.0.0.txt' 'data/test.1.0.0.txt' #copy from ram to disk

mv '/tmp/test.2.0.0.txt' 'data/test.2.0.0.txt'
