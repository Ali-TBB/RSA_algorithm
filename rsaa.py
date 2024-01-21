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

def generate_keypair(bits=16):
    # Step 1: Choose two large prime numbers
    p = random_prime(bits)
    q = random_prime(bits)

    # Step 2: Compute n = pq and phi(n) = (p-1)(q-1)
    n = p * q
    print("n is : ",n)
    phi_n = (p - 1) * (q - 1)

    # Step 3: Choose public exponent e
    e = random.randrange(1, phi_n)
    while not is_coprime(e, phi_n):
        e = random.randrange(1, phi_n)

    print("e is :", e)
    # Step 4: Compute private exponent d (modular inverse of e modulo phi(n))
    d = modinv(e, phi_n)

    # Public key: (e, n), Private key: (d, n)
    return ((e, n), (d, n))

def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

def random_prime(bits):
    while True:
        candidate = random.getrandbits(bits)
        if is_prime(candidate):
            return candidate

def is_coprime(a, b):
    while b:
        a, b = b, a % b
    return a == 1

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Example: Encrypt and decrypt "Hello, World!" using RSA
public_key, private_key = generate_keypair()
print("public key is :", public_key)
message = "Hello, World!"
encrypted_message = encrypt(message, public_key)
decrypted_message = decrypt(encrypted_message, private_key)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
