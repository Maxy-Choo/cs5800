import matplotlib.pyplot as plt
import csv

with open("./gp01/time.csv", mode="r", newline='', encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    time = []
    
    for row in csv_reader:
        tmp = []
        for t in row:
            tmp.append(float(t))
        time.append(tmp)
    
    cases=[i for i in range(10, 1001, 10)]
    plt.plot(cases, time[0], label="10 changeable strings")
    plt.plot(cases, time[1], label="50 changeable strings")
    plt.plot(cases, time[2], label="100 changeable strings")
    plt.xlabel("string length")
    plt.ylabel("time: ms")
    plt.title("Time analysis for Min Cost To Convert String II")
    plt.legend()
    plt.show()

