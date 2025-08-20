def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage:
if __name__ == "__main__":
    num = 5
    print("Iterative:", factorial_iterative(num))
    print("Recursive:", factorial_recursive(num))