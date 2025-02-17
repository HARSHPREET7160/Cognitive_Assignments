import numpy as np
import matplotlib.pyplot as plt

M = float(input("Enter a value for M: "))

x = np.linspace(-10, 10, 400)
y1 = M*x**2
y2 = M*np.sin(x)

plt.figure(figsize=(8,6))
plt.plot(x, y1,'r--',label=f'y = {M}x²')
plt.plot(x, y2,'b-',label=f'y = {M}sin(x)')

plt.legend()
plt.grid(True)
plt.title("Graphs of y = Mx² and y = Msin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
