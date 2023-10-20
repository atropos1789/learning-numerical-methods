CC = gcc

c_euler_method: src/C/euler_method.c
	$(CC) src/C/euler_method.c -o bin/C/euler_method.o

c_improved_euler_method: src/C/improved_euler_method.c
	$(CC) src/C/improved_euler_method.c -o bin/C/improved_euler_method.o

clean:
	rm -f bin/*/*
