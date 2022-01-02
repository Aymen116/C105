import csv 
import pandas as ps
import plotly.express as pe
import math

with open("data.csv") as c:
    reader = csv.reader(c)
    file_data = list(reader)
data = file_data[0]
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total / n
    return mean 

square_list = []
for number in data:
    a = int(number) - mean(data)
    a = a ** 2
    square_list.append(a)
sum = 0
for i in square_list:
    sum = sum+i
result = sum / (len(data)-1)
sd = math.sqrt(result)
print(sd)