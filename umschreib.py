import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv


def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def csv_write(pathToFile, data):
    with open(pathToFile, "w", newline = '') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=";", quotechar = '|', quoting=csv.QUOTE_MINIMAL )
        spamwriter.writerow(data)

werte = csv_read("csv/einzel_mittel.csv")
xdata = np.zeros(78)
ydata = np.zeros(78)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0]) - 25 
        ydata[i] = float(values[1]) 
        
        i+=1
a = np.zeros((78, 2))

a[:,0] = xdata
a[:,1] = ydata
print(a)
csv_write("test.csv", a)
                