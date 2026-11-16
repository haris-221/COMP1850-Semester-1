import matplotlib.pyplot as plt

x = [k for k in range(10)]
y = [k*k for k in x]

plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('y=x^2')

plt.show()