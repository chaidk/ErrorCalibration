import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-5,5,1000)
y = 8 * np.sinc(x)

plt.figure('Grid',facecolor="lightgray")
plt.title("Grid",fontsize=20)
plt.xlabel("x",fontsize=14)
plt.ylabel("y",fontsize=14)

ax = plt.gca()
ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(plt.MultipleLocator(.1))

ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(plt.MultipleLocator(.1))


#紧凑布局
plt.tight_layout()

ax.grid(which='major',axis="both",linewidth=0.75,linestyle='-',color='orange')

ax.grid(which='minor',axis="both",linewidth=0.25,linestyle='-',color='orange')

# plt.grid(linestyle=":")

plt.plot(x,y,c="dodgerblue",label=r'$y=8sinc(x)$')

plt.legend()

plt.show()