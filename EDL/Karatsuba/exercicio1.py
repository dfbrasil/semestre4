
def karatsuba(x,y):
    if x<10 or y<10:
        return x*y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    x_high, x_low = divmod(x, 10**m)
    y_high, y_low = divmod(y, 10**m)
    
    z0 = karatsuba(x_low, y_low)
    z1 = karatsuba((x_low + x_high), (y_low + y_high))
    z2 = karatsuba (x_high, y_high)
    
    return z2 * 10**(2 * m) + ((z1 - z2 -z0) * 10**m) + z0

resultado1 = karatsuba(1234, 5678)
resultado2 = karatsuba(11111111, 22222222)
resultado3 = karatsuba(12345678, 87654321)
print(f"Resultado: {resultado1}")
print(f"Resultado: {resultado2}")
print(f"Resultado: {resultado3}")
