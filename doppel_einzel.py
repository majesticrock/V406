import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content
def func(x, s, b):
    C = 1.4* 10**(-6)
    return C * (np.cos((np.pi * s * np.sin(x))/(633*10**(-9))))**2 *((633*10**(-9))/(np.pi * b * np.sin(x)))**2 * (np.sin((np.pi * b * np.sin(x))/(633*10**(-9))))**2

def funce(x):
    a= (14/3.1)
    b = 0.00026273
    return a**2 * b**2 * (633*10**(-9)/(np.pi * b * np.sin(x)))**2 * np.sin(np.pi * b * np.sin(x)/(633*10**(-9)))**2

werte = csv_read("csv/doppel.csv")
xdata = np.zeros(48)
ydata = np.zeros(48)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = (float(values[0]) + 1 )  /(1080)
        ydata[i] = (float(values[1]) - 0.000175) * 10**(-6)
        i+=1

print(xdata)
guess = [0.00025, 0.00015]

#guess = np.array([0.0002, 0.00014]) * 2
x_1 = np.linspace(-0.0095, -0.000001, 204)
x_2 = np.linspace(0.000001, 0.0125, 204)
x_line = np.array([*x_1, *x_2])
#x_line = np.linspace(-0.012, 0.012)
plt.plot(xdata, ydata, "rx", label="Messwerte")
plt.plot(0, (1.4 - 0.000175) * 10**(-6), "ro", label="Nicht betrachteter Messwert")
popt, pcov = curve_fit(func, xdata, ydata, guess)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")
plt.plot(x_line, funce(x_line), "g-", label="Einzelspaltkurve")


print(popt)
print(np.sqrt(pcov))
#plt.xscale('log')
plt.grid()
plt.xlabel(r"$\frac{x}{L}$ / rad")
plt.ylabel(r"$I$ /  A")
plt.legend()
plt.tight_layout()
plt.savefig("build/doppel_einzel.pdf")

