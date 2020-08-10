#   name  dist   width selection time
#['mkw60', '512', '32', '0', '1279.50']
import math
import statistics
import csv

file = open("experiment_fitts_log.txt", "r")
records = {}


for i in file:
    name, distance, width, selection, time = i.split()
    time = round((float(time)/1000),4)
    value = (distance, width)
    ID = math.log2(((int(distance) / int(width)) + 1))
    if value in records:
        records[value].append((time, ID))
    else:
        records[value] = [(time, ID)]

print(records)


results = []
sum_time = {}
sum_id = {}

for name, values in records.items():
    distance = int(name[0])
    width = int(name[1])
    Id_mean = []
    time_mean = []
    for time, id in values:
        sum_time[id] = sum_time.get(id,0) + time
        sum_id[id] = sum_id.get(id, 0) + 1

for key in sum_time.keys():
    sum_time[key] /= sum_id[key]

results.insert(0,["ID",	"mean time"])

# print(results)

with open("summary.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(sum_time.items())



