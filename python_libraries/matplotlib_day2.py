# matplotlib style
import matplotlib.pyplot as plt
# print(plt.style.available)
import numpy as np

# first create sample data
x = np.linspace(0, 2*np.pi, 400)
y = np.cos(x**2)

#create a figure
fig = plt.figure()

# create a subplot
axes = fig.subplots(2, 2)

axes[0,0].plot(x,y, label='cos')
axes[0,0].legend()
axes[0,1].plot(np.exp(x), label='Exponential')
axes[0,1].legend()
axes[1,0].plot(np.log10(x), label='log')
axes[1,0].legend()
axes[1,1].scatter(x,y, label='scatter')
axes[1,1].legend()
plt.show()