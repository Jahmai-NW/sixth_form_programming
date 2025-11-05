import math


# With code completion, as I type "math.", the IDE suggests all functions that I could use:
# e.g., math.sqrt(), math.sin(), math.cos(), math.pow(), etc.

numbers = [4, 9, 16, 25, 36]
square_roots = []

for num in numbers:
    # Code completion suggests 'sqrt' after typing 'math.s'
    square_roots.append(math.sqrt(num))

print("The square roots are:", square_roots)

# Code completion also helps recall list methods such as 'append', 'sort', or 'reverse'.
square_roots.sort()
print("Sorted roots:", square_roots)