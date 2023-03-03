import matplotlib.pylab as plt
import random, math, time
import numpy as np


class RingBuffer:
    def __init__(self, size):
        self.data = [0 for i in range(size)]
        

    def append(self, x):
        self.data.pop(0)
        self.data.append(x)

    def get(self):
        return self.data

CHUNK = 100 # x axis length ( data points)

data = RingBuffer(CHUNK) # define the arrays (lines to the graph)
data2 = RingBuffer(CHUNK)
data3 = RingBuffer(CHUNK)

fig,ax = plt.subplots()
x = np.arange(0,2*CHUNK,2)
line1, = ax.plot(x, np.random.rand(CHUNK), 'r') #initialise the graph lines
line2, = ax.plot(x, np.random.rand(CHUNK), 'b')
line3, = ax.plot(x, np.random.rand(CHUNK), 'g')
ax.set_ylim(-5,5)
ax.set_xlim(0,CHUNK)
fig.show()
i =0

while 1:
    line1.set_ydata(data.get()) # add the lines to graph
    line2.set_ydata(data2.get())
    line3.set_ydata(data3.get())
    fig.canvas.draw()
    fig.canvas.flush_events()
    #time.sleep(0.1) if need the graph refeash rate 
    i+=1
    
    data.append((random.random()-0.5)*10) # update the arrays with new value
    data2.append(math.sin(0.02*math.pi*i*10))
    data3.append(2*math.cos(0.02*math.pi*i*10))