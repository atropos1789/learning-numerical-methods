CC = gcc
CFLAGS = -Wall -Werror
	
c_euler_method: src/C/euler_method.c
	$(CC) $(CFLAGS) -c src/euler_method.c -o obj/euler_method.o

c_improved_euler_method: src/C/improved_euler_method.c
	$(CC) $(CFLAGS) -c src/improved_euler_method.c -o obj/improved_euler_method.o

CLibrary: 
	$(CC) $(CFLAGS) -fPIC -shared src/euler_method.c src/improved_euler_method.c -o bin/clibeuler.so

CMain:
	$(CC) $(CFLAGS) src/main.c -o bin/program bin/clibeuler.so

clean:
	rm -f bin/*
	rm -f obj/*
