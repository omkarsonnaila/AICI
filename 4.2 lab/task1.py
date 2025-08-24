# write a python function which generates fibnacci series upto n terms
def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Enter number of terms: "))
print(fibonacci_series(n))