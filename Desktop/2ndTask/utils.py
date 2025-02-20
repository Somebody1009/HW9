def factorial(n):
    if n < 0:
        raise ValueError('Factorial is not defined for negative numbers')
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
<<<<<<< Updated upstream
    return True 
=======
    return True

def is_power_of_5(n):
    if n <= 0:
        return False
    while n > 1:
        if n % 5 != 0:
            return False
        n = n // 5
    return True

def is_power_of_2(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0 
>>>>>>> Stashed changes
