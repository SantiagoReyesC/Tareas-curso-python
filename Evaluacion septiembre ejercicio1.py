import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-0.5, 2.5, 100)
y = x**2

x_tangente = np.linspace(-0.5, 2.5, 50)
y_tangente = 2 * x_tangente - 1


plt.plot(x, y, 'b-', linewidth=2, label='y = x^2')
plt.plot(x_tangente, y_tangente, 'g-', linewidth=0.5, label='Tangente: y = 2x - 1')




plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x² y tangente a (1,1)')
plt.legend()
plt.axhline(y=0, color='k', linestyle='-')
plt.axvline(x=0, color='k', linestyle='-')

plt.show()