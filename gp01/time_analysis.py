import matplotlib.pyplot as plt
import csv

with open("./gp01/time.csv", mode="r", newline='', encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    time=(double)csv_reader[0].split(",")
    cases=[10, 100, 1000]
    