import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y1 = np.power(x,2)
y2 = np.sin(x)
y3 = np.exp(x)
y4 = np.log(np.abs(x)+1)

plt.figure(figsize=(10,10)) 

plt.plot(x, y1,label="y=x²",color='b', linestyle='--')
plt.plot(x, y2,label="y=sin(x)",color='g',linestyle='--')
plt.plot(x, y3,label="y=e^x",color='r',linestyle='-.')
plt.plot(x, y4,label="y=log(|x| + 1)",color='m', linestyle=':')


plt.title("Graphs of Different Mathematical Functions")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.legend()
plt.grid(True)
plt.show()
