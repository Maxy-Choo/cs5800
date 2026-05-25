def extEuclid(x, y):
    if y == 0:
        return 1, 0 ,x
    a, b, d = extEuclid(y, x%y)
    return b, a-x//y*b, d

def fastExp(x, e, N):
    if e == 0:
        return 1
    if e == 1:
        return x % N
    half = fastExp(x, e//2, N)
    res = (half * half) % N
    if e % 2 == 1:
        res = (res * x) % N
    return res

if __name__ == "__main__":
    a1, _, _ = extEuclid(20, 79)
    print(a1)
    a2 = fastExp(2, 125, 127)
    print(a2)