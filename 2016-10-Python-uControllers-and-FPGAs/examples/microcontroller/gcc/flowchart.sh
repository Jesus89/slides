# GCC Compilation step by step
# Equivalent to `gcc example.c math.c -o example`

# Preprocessing

gcc -E example.c > example.i
gcc -E math.c > math.i

# Compilation

gcc -S example.i  # > example.s
gcc -S math.i  # > math.s

# Assembler

gcc -c example.s  # > example.o
gcc -c math.s  # > math.o

# Linking

gcc example.o math.o -o example  # > example
