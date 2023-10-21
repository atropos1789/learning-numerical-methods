CC = gcc
CFLAGS = -Wall -Werror
	
c_euler_method: src/C/euler_method.c
	$(CC) $(CFLAGS) -c src/C/euler_method.c -o obj/C/euler_method.o

c_improved_euler_method: src/C/improved_euler_method.c
	$(CC) $(CFLAGS) -c src/C/improved_euler_method.c -o obj/C/improved_euler_method.o

c_main: src/C/main.c
	$(CC) $(CFLAGS) -c src/C/main.c -o obj/C/main.o

CLibrary: 
	$(CC) $(CFLAGS) -fPIC -shared src/C/euler_method.c src/C/improved_euler_method.c -o bin/C/clibeuler.so

CMain:
	$(CC) $(CFLAGS) src/C/main.c -o bin/C/program bin/C/clibeuler.so

clean:
	rm -f bin/*/* 
	rm -f obj/*/*
