def pad_with_zeros(number, desired_digits):
    num_str = str(number)
    num_digits = len(num_str)
    
    if num_digits < desired_digits:
        padding_zeros = '0' * (desired_digits - num_digits)
        padded_number = padding_zeros + num_str
        return padded_number
    else:
        return num_str

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    
    if n % 2 != 0:
        n += 1
    
    m = n // 2
    
    x_str = pad_with_zeros(x, n)
    y_str = pad_with_zeros(y, n)
    
    x_high, x_low = divmod(int(x_str), 10**m)
    y_high, y_low = divmod(int(y_str), 10**m)
    
    z0 = karatsuba(x_low, y_low)
    z1 = karatsuba(x_low + x_high, y_low + y_high)
    z2 = karatsuba(x_high, y_high)
    
    return z2 * 10**(2 * m) + ((z1 - z2 - z0) * 10**m) + z0

resultado1 = karatsuba(123, 456789)
resultado2 = karatsuba(12345, 678)
resultado3 = karatsuba(123456, 78901234)

print(f"Resultado: {resultado1}")
print(f"Resultado: {resultado2}")
print(f"Resultado: {resultado3}")
print(123 * 456789)
