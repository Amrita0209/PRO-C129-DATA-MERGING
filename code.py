import csv

with open('data1.csv', newline="") as f:
  reader = csv.reader(f)
  data1 = list(reader)

with open('data2.csv', newline="") as f:
  reader = csv.reader(f)
  data2 = list(reader)

merged_array = []

headers = data1[0]
data1.pop(0)

merged_array = data1 + data2

with open("merged.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(merged_array)
