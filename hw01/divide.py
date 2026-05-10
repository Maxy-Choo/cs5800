import time
import random
import math

def divide(x, y):
    if x == 0:
        return (0, 0)
    
    q, r = divide(x // 2, y)
    q = 2 * q
    r = 2 * r
    
    if x % 2 == 1:
        r = r + 1
    
    if r >= y:
        r = r - y
        q = q + 1
    
    return (q, r)

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    for i in range(25, 30):
        a = 2 ** i
        b = random.randint(1, a)
        q1, r1 = divide(a, b)
        q2, r2 = a // b, a % b
        print(f"x={a}, y={b}")
        print(f"Divide function result: {q1}, {r1}")
        print(f"Built-in function result: {q2}, {r2}\n")
    
    a = []
    b = []
    for i in range(1, 31):
        x = 2 ** i
        y = random.randint(1, x)
        a.append((x, y))
        start = time.time()
        q, r = divide(x, y)
        elapsed = round(time.time() - start, 2)
        b.append(elapsed)
        print(f"{x} div {y} = {q} remainder {r}, time usage: {elapsed}s")
    
    plt.plot(a, b)
    plt.xlabel("x, y")
    plt.ylabel("Time (seconds)")
    plt.title("Time taken to compute division")
    plt.show()