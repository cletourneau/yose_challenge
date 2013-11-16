def prime_factors_of(number):
    factors = []

    for divisor in range(2, number + 1):
        while number % divisor == 0:
            factors.append(divisor)
            number /= divisor

    return factors