import matplotlib.pyplot as plt
import csv

with open("./gp01/time.csv", mode="r", newline='', encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    time = []
    for row in csv_reader:
        for t in row:
            time.append(float(t))
    cases=[i for i in range(10, 1001, 10)]
    plt.plot(time, cases)
    plt.xlabel("time: ms")
    plt.ylabel("string length")
    plt.title("Time analysis for Min Cost To Convert String II")
    plt.show()

