import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-np.pi/2 + 0.01, np.pi/2 - 0.01, 1000)

sinus = np.sin(x)
cosinus = np.cos(x)
tangenta = np.tan(x)
cotangenta = 1/np.tan(x)

plt.figure(figsize=(10, 7))
plt.plot(x, sinus, label='sin x')
plt.plot(x, cosinus, label='cos x')
plt.plot(x, tangenta, label='tangenta x')
plt.plot(x, cotangenta, label='cotangenta x')

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True)
plt.ylim(-10, 10)
plt.legend()
plt.title("Functii sin, cos, tg, ctg")
plt.xlabel("Val x")
plt.ylabel("Val functii")
plt.show()
