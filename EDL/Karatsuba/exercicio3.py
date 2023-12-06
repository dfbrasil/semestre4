import time
import random

def generate_large_number(digits):
    return random.randint(10 ** (digits - 1), 10 ** digits - 1)

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    x_high, x_low = divmod(x, 10**m)
    y_high, y_low = divmod(y, 10**m)
    
    z0 = karatsuba(x_low, y_low)
    z1 = karatsuba((x_low + x_high), (y_low + y_high))
    z2 = karatsuba(x_high, y_high)
    
    return z2 * 10**(2 * m) + ((z1 - z2 - z0) * 10**m) + z0

# Karatsuba - resultado1
x1, y1 = generate_large_number(10), generate_large_number(10)
print(f"\nEntrada 1: {x1} * {y1}")
start_time = time.time()
resultado1 = karatsuba(x1, y1)
end_time = time.time()
print(f"Resultado 1: {resultado1}")
print(f"Tempo Resultado 1: {end_time - start_time:.8f} segundos")

# Multiplicação simples resultado1
start_time = time.time()
simple_mult1 = x1 * y1
end_time = time.time()
print(f"Multiplicação Simples 1: {simple_mult1}")
print(f"Tempo Multiplicação Simples 1: {end_time - start_time:.8f} segundos")

# Karatsuba - resultado2
x2, y2 = generate_large_number(50), generate_large_number(50)
print(f"\nEntrada 2: {x2} * {y2}")
start_time = time.time()
resultado2 = karatsuba(x2, y2)
end_time = time.time()
print(f"Resultado 2: {resultado2}")
print(f"Tempo Resultado 2: {end_time - start_time:.8f} segundos")

# Multiplicação simples resultado2
start_time = time.time()
simple_mult2 = x2 * y2
end_time = time.time()
print(f"Multiplicação Simples 2: {simple_mult2}")
print(f"Tempo Multiplicação Simples 2: {end_time - start_time:.8f} segundos")

# Karatsuba - resultado3
x3, y3 = generate_large_number(100), generate_large_number(100)
print(f"\nEntrada 3: {x3} * {y3}")
start_time = time.time()
resultado3 = karatsuba(x3, y3)
end_time = time.time()
print(f"Resultado 3: {resultado3}")
print(f"Tempo Resultado 3: {end_time - start_time:.8f} segundos")

# Multiplicação simples resultado3
start_time = time.time()
simple_mult3 = x3 * y3
end_time = time.time()
print(f"Multiplicação Simples 3: {simple_mult3}")
print(f"Tempo Multiplicação Simples 3: {end_time - start_time:.8f} segundos")
