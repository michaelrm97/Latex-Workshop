import matplotlib.pyplot as plt
from math import exp

filename = 'xplot.png'

tmin = 0
step = 0.001
tmax = 5

times = [step * t for t in range(int(tmin / step), int(tmax / step) + 1)]
x = [2.5 - 1.5 * exp(-4*t) for t in times]

plt.plot(times, x)
plt.title(f'x(t) for {tmin} <= t <= {tmax}')
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.savefig(filename)
