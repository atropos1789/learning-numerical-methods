CC = gcc

#C: c_euler_method c_improved_euler_method c_main
#	$(CC) obj/C/euler_method.o obj/C/improved_euler_method.o obj/C/main.o -o src/C/c_linalg
	
c_euler_method: src/C/euler_method.c
	$(CC) -c src/C/euler_method.c -o obj/C/euler_method.o

c_improved_euler_method: src/C/improved_euler_method.c
	$(CC) -c src/C/improved_euler_method.c -o obj/C/improved_euler_method.o

c_main: src/C/main.c
	$(CC) -c src/C/main.c -o obj/C/main.o

clean:
	rm -f bin/*/*
