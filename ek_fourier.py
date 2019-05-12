import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content
def func(x, a, b):
    return 4*a**2 * (633 * 10**(-9))**2 /(4 * np.pi**2 * np.sin(x)**2) * np.sin(np.pi * b * x / (633 * 10**(-9)) )**2

werte = csv_read("csv/einzel2.csv")
xdata = np.zeros(51)
ydata = np.zeros(51)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = (float(values[0]) ) /(1080)
        ydata[i] = (float(values[1]) - 0.175) * 10**(-9)
        i+=1

print(xdata)
guess = [1, 0.000007]
x_line = np.linspace(-0.025, 0.025)
plt.plot(xdata, ydata, "rx", label="Messwerte")
plt.plot(0, (9.4- 0.175) * 10**(-9), "ro", label="Nicht betrachteter Messwert")
popt, pcov = curve_fit(func, xdata, ydata, guess)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

print(popt)
print(np.sqrt(pcov))

#plt.xscale('log')
plt.xlabel(r"$\frac{x}{L}$ / rad")
plt.ylabel(r"$I$ /  A")
plt.legend()
plt.tight_layout()
plt.savefig("build/ek_fourier.pdf")