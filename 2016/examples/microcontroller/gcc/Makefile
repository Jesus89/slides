CC=gcc
DEPS = math.h
OBJ = example.o math.o 

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $<

example: $(OBJ)
	$(CC) -o $@ $^

clean:
	rm -f *.o
	rm -f example
