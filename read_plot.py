import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

fig = plt.figure()
        
ax1 = fig.add_subplot(1,1,1)

rect = fig.patch
def animate(i):
    fread = "reads.csv"
    fh = open(fread)
    xs = []
    ys = []
    for line in fh:
        xys = line.split(',')
        x = xys[0]
        y = xys[1]
        xs.append(float(x))
        ys.append(float(y))

        ax1.clear()
        ax1.plot(xs,ys)
        plt.ylabel('range')
        plt.xlabel('time')
ani = animation.FuncAnimation(fig, animate, interval = 5000)
plt.show()
