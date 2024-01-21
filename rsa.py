num = 2211282552952966643528108525502623092761208950247001539441374831912882294140
2001986512729726569746599085900330031400051170742204560859276357953757185954
2988389587092292384910067030341246205457845664136645406842143612930176940208
46391065875914794251435144458199
import random

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def generate_primes_by_digits(num_digits):
    primes = []
    lower_bound = 10 ** (num_digits - 1) + 1
    upper_bound = 10 ** num_digits - 1

    for candidate in range(lower_bound, upper_bound + 1, 2):
        if is_prime(candidate):
            primes.append(candidate)

    return primes

# Example: Generate all prime numbers with 3 digits
num_digits = 28
prime_list = generate_primes_by_digits(num_digits)
print(f"All prime numbers with {num_digits} digits:", prime_list)
