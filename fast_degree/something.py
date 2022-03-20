def power(a, n):
    return (1 if n == 0
            else power(a * a, n // 2) if n % 2 == 0
    else a * power(a, n - 1))

print(power(2, 64))