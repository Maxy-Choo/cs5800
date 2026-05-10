def fib_recursive(n):
    if  n<=1:
        return n
    return fib_recursive(n-1)+fib_recursive(n-2)

def fib_array(n):
    if n<=1:
        return n
    arr=[]
    arr.append(0)
    arr.append(1)
    for i in range(2, n+1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n]

def fib_compressed(n):
    if n<=1:
        return n
    
    s0, s1 = 0, 1
    for i in range(2, n+1):
        s0, s1 = s1, s0+s1
    
    return s1

if __name__ == "__main__":
    import time
    import matplotlib.pyplot as plt
    x = []
    y1 = []
    y2 = []
    y3 = []
    for i in range(5, 36, 5):
        x.append(i)
        start = time.time()
        print(f"fib({i}):\n")
        fib_recursive(i)
        t = round(time.time() - start, 2)
        print(f"Recursive Time taken: {t} seconds\n")
        y1.append(t)

        start = time.time()
        fib_array(i)
        t = round(time.time() - start, 2)
        print(f"Array Time taken: {t} seconds\n")
        y2.append(t)

        start = time.time()
        fib_compressed(i)
        t = round(time.time() - start, 2)
        print(f"Compressed Time taken: {t} seconds\n")
        y3.append(t)
    
    plt.plot(x, y1, label="Recursive")
    plt.plot(x, y2, label="Array")
    plt.plot(x, y3, label="Compressed")
    plt.xlabel("n")
    plt.ylabel("Time (seconds)")
    plt.title("Time taken to compute Fibonacci numbers")
    plt.legend()
    plt.show()
    