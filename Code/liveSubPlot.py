#!/usr/bin/python

# Create a live plot of temperature data
# Author: Jason Stafford, 04-Mar-2023 (j.stafford@bham.ac.uk)

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.dates as mdates
from matplotlib import style
from datetime import datetime


fig = plt.figure(figsize = (12,12), edgecolor='k')
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)


def animate(i):
    graph_tempdata = open('TemperatureData.txt','r').read()
    lines_t = graph_tempdata.split('\n')
    
    xt = []
    y0t = []
    y1t = []
    y2t = []
    y3t = []
    y4t = []
    y5t = []

    for line in lines_t:
        if len(line) > 1:
            tb, T1, T2, T3, T1_int, T2_int, T3_int = line.split(' ')
            timestringb = datetime.strptime(tb,'%H:%M:%S.%f')
            xt.append(timestringb)
            y0t.append(float(T1))
            y1t.append(float(T1_int))
            y2t.append(float(T2))
            y3t.append(float(T2_int))
            y4t.append(float(T3))
            y5t.append(float(T3_int))
   
    ax1.clear()   
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax1.plot(xt, y0t, 'go-', linewidth = 0.5)
    ax1.set_title("$\mathbf{T1}$")
    ax1.set_ylabel('Temperature ($\mathbf{^{o}C}$)', fontweight='bold', fontsize = 9)
    ax1.grid(True)

    ax2.clear()
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax2.plot(xt, y2t, 'bo-', linewidth = 0.5)
    ax2.set_title("$\mathbf{T2}$")
    ax2.set_ylabel('Temperature ($\mathbf{^{o}C}$)', fontweight='bold', fontsize = 9)
    ax2.grid(True)

    ax3.clear()
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax3.plot(xt, y4t, 'ko-', linewidth = 0.5)
    ax3.set_title("$\mathbf{T3}$")
    ax3.set_xlabel('Time', fontweight='bold', fontsize = 9)
    ax3.set_ylabel('Temperature ($\mathbf{^{o}C}$)', fontweight='bold', fontsize = 9)
    ax3.grid(True)

    ax4.clear()
    ax4.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax4.plot(xt, y1t, 'go--', xt, y3t, 'bo--', xt, y5t, 'ko--', linewidth = 0.5)
    ax4.set_title("$\mathbf{T_{internal}}$")
    ax4.set_xlabel('Time', fontweight='bold', fontsize = 9)
    ax4.set_ylabel('Temperature ($\mathbf{^{o}C}$)', fontweight='bold', fontsize = 9)
    ax4.legend(['T1','T2','T3'])
    ax4.grid(True)

    fig.tight_layout()

ani = FuncAnimation(fig, animate, interval=3000)
plt.show()
