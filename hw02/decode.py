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

def decode(msg, d, N):
    return fastExp(msg, d, N)

if __name__ == "__main__":
    msg = 73299208648
    N = 156934814459
    d = 31386785261
    print(decode(msg, d, N))