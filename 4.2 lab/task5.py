def max_of_three(a, b, c):
    # Sample 1: max_of_three(1, 2, 3) -> 3
    # Sample 2: max_of_three(10, 5, 7) -> 10
    # Sample 3: max_of_three(-1, -5, -3) -> -1

    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Sample inputs and outputs
print(max_of_three(1, 2, 3))    # Output: 3
print(max_of_three(10, 5, 7))   # Output: 10
print(max_of_three(-1, -5, -3)) # Output: -1