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
    return 4 * np.cos(np.pi * s * np.sin(x)/(633*10**(-9)))**2 *(633*10**(-9)/(np.pi * b * np.sin(x)))**2 *np.sin(np.pi * b * np.sin(x)/(633*10**(-9)))**2
    

werte = csv_read("csv/doppel.csv")
xdata = np.zeros(49)
ydata = np.zeros(49)

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
guess = [0.003, 0.0015]
x_line = np.linspace(-0.012, 0.012)
plt.plot(xdata, ydata, "rx", label="Messwerte")
plt.plot(0, (1.4- 0.175) * 10**(-6), "ro", label="Nicht betrachteter Messwert")
popt, pcov = curve_fit(func, xdata, ydata, guess)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")


print(popt)
print(np.sqrt(pcov))
#plt.xscale('log')
plt.grid()
plt.xlabel(r"$\frac{x}{L}$ / rad")
plt.ylabel(r"$I$ /  A")
plt.legend()
plt.tight_layout()
plt.savefig("build/doppel.pdf")