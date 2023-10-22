CC = gcc
CFLAGS = -Wall -Werror

libeuler: 
	$(CC) $(CFLAGS) -fPIC -shared lib_src/euler_method.c lib_src/improved_euler_method.c lib_src/runge_kutta.c -o bin/clibeuler.so

CMain:
	$(CC) $(CFLAGS) src/main.c -o bin/program bin/clibeuler.so

tests:
	$(CC) $(CFLAGS) src/test_1.0.c -o bin/test_1.0 bin/clibeuler.so
	$(CC) $(CFLAGS) src/test_2.0.c -o bin/test_2.0 bin/clibeuler.so
	$(CC) $(CFLAGS) src/test_3.0.c -o bin/test_3.0 bin/clibeuler.so

test1:
	$(CC) $(CFLAGS) src/test.1.0.0.c -o bin/test.1.0.0 bin/clibeuler.so

test2:
	$(CC) $(CFLAGS) src/test.2.0.0.c -o bin/test.2.0.0 bin/clibeuler.so

clean:
	rm -f bin/*
	rm -f obj/*
