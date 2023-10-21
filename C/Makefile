CC = gcc
CFLAGS = -Wall -Werror
	
CLibrary: 
	$(CC) $(CFLAGS) -fPIC -shared lib_src/euler_method.c lib_src/improved_euler_method.c lib_src/runge_kutta.c -o bin/clibeuler.so

CMain:
	$(CC) $(CFLAGS) src/main.c -o bin/program bin/clibeuler.so

clean:
	rm -f bin/*
	rm -f obj/*
