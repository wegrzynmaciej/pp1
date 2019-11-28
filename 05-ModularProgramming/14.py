import statistics as st
import csv

ages = []

with open('05-ModularProgramming/employees.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        ages.append(row[2])

ages = [int(x) for x in ages]

mean = st.mean(ages)
median = st.median(ages)
deviation = st.stdev(ages)

print('\
    Średnia arytmetyczna: {}\n\
    Mediana: {}\n\
    Odchylenie standardowe: {} '
      .format(
          mean,
          median,
          deviation
      )
      )
