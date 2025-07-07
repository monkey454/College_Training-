# matplotlib style
import matplotlib.pyplot as plt
# print(plt.style.available)
import numpy as np

"""# first create sample data
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
plt.show() """

fs = 1000
t = np.arange(0, 10, 1/fs)
eeg_signal = np.sin(2*np.pi*10*t)+0.5*np.random.randn(len(t))
plt.plot(t,eeg_signal)
plt.title('EEG signal')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.show() 

x = np.linspace(0,5,100)
y1 = x**2
y2 = x
plt.fill_between(x,y1,y2,color='skyblue',alpha=0.4, label='filled area')
plt.plot(x,y1,label='y=x^2')
plt.plot(x,y2,label='y=x')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Fill between')
plt.legend()
plt.show()