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
    import time, matplotlib.pyplot as plt
    exp = [i for i in range(100000)]
    t = []
    for i in exp:
        start = time.perf_counter()
        fastExp(2, i, 100)
        end = time.perf_counter()
        t.append(end-start)
    
    plt.plot(exp, t)
    plt.xlabel("Exponent")
    plt.ylabel("Time(s)")
    plt.title("Time taken for fast exponentiation")
    plt.show()