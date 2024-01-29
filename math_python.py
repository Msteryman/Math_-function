import matplotlib.pyplot as plt
import numpy as np
import os
os.system('cls')
a = (input("введите уравнения"))

x = np.arange(-60,60,0.001)
ypoints = eval(a)
plt.plot(x, ypoints)
plt.grid(True)
plt.show()


