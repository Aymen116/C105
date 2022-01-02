import csv 
import pandas as ps
import plotly.express as pe

with open("class2.csv") as c:
    reader = csv.reader(c)
    file_data = list(reader)
file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n = file_data[i][1]
    new_data.append(float(n))
number = len(new_data)
total = 0
for x in new_data:
    total += x
mean = total / number
print(mean)

df = ps.read_csv("class2.csv")
figure = pe.scatter(df, x = "Student Number", y = "Marks")
figure.update_layout(shapes = [
    dict(
        type = "line",
        y0 = mean, y1 = mean,
        x0 = 0, x1 = number,
    )
])
figure.update_yaxes(rangemode = "tozero")
figure.show()