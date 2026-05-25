def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def extEudid(x, y): # xp*x + yp*y = gcd(x, y)
    if y == 0:
        return 1, 0, x
    else:
        xp, yp, d = extEudid(y, x%y)
        return yp, xp - (x//y)*yp, d

def fastExp(x, y, N): # x^y mod p
    if y == 0:
        return 1
    if y == 1:
        return x
    
    half = y // 2
    rem = y % 2
    sp = fastExp(x, half, N)
    val = (sp * sp) % N
    if rem == 1:
        val = (val * x) % N
    return val

def gen_prime(min, max):
    import random
    while True:
        p = random.randint(min, max)
        if is_prime(p):
            return p

def is_prime(p): # Fermat primality test
    import random
    for i in range(40):
        a = random.randint(1, p-1)
        if a % p == 0 or fastExp(a, p-1, p) > 1:
            return False
    return True

if __name__ == "__main__":
    import random
    #lower = int(input("Enter lower bound for prime generation: "))
    #upper = int(input("Enter upper bound for prime generation: "))
    #p = gen_prime(lower, upper)
    #q = gen_prime(lower, upper)
    p = int(input("Enter prime p: "))
    q = int(input("Enter prime q: "))
    print(f"Generated primes: p={p}, q={q}")
    N = p * q
    phi = (p-1) * (q-1)
    e = random.randint(2, phi-1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi-1)
    d, _, _ = extEudid(e, phi)
    d %= phi
    print(f"Public key: {N}|{e}")
    print(f"Private key: {d}")
    message = int(input("Enter message to encrypt (integer): "))
    encrypted = fastExp(message, e, N)
    print(f"Encrypted message: {encrypted}")
    decrypted = fastExp(encrypted, d, N)
    print(f"Decrypted message: {decrypted}")
