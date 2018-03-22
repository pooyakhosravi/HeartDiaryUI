import numpy as np
import matplotlib.pyplot as plt
import json
from pprint import pprint

data = json.load(open('data.json'))
class data_class:
    date = '0308_2018'
    hr = data["heartrate"][date]
    act = data['activity'][date]
    piechart = True
    
    rates = hr['rates']
    acts = act['activity']
    def __init__(self):
        result = [0]
        for k in self.acts:
            result.append(int(k)* np.pi * 2 / 1440)
        result.append(2 * np.pi)
        self.acts_theta = result
        self.n = 10

    def get_heartrate(self, a, b):
        x = []
        y = []
        gen = (x for x in self.rates if (int(x) > a and int(x) < b))
        for k in gen:
            x.append( int(k) * np.pi * 2 / 1440)
            y.append(self.rates[k])
        return x, y


data_class = data_class()

def onclick(event):
    if event.dblclick:
        t = event.xdata
        if t < 0:
            t = t + 2 * np.pi
        a, b = get_bounds_for_click(t)

        plot_linearHR(a * 1440 / 2 / np.pi, b * 1440 / 2 / np.pi, data_class.n)
    #data_class.n = data_class.n +  1
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))



def get_bounds_for_click(theta):
    for k in range(len(data_class.acts_theta)):
        if data_class.acts_theta[k] > theta:
            return data_class.acts_theta[k-1], data_class.acts_theta[k]





def plot_linearHR(a,b, n):
    plt.figure(n)
    plt.cla()
    x, y = data_class.get_heartrate(a, b)
    plt.plot(x, y)
    plt.show()



r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r

########

#plot_linearHR(0, 700, 1, rates)

#plot_linearHR(400, 800, 4, rates)


plt.figure(2)
ax = plt.subplot(111, projection='polar')
fig = ax.get_figure()
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

hrTheta = []
hrR = []
col = []
prevHR = '0'
for k in data_class.rates:
    hrTheta.append( int(k) * np.pi * 2 / 1440)
    hrR.append(data_class.rates[k])
    
    if data_class.rates[k] > 100 and data_class.rates[k] < 130:
        if data_class.piechart:
            color = 'w'
        else:
            color = 'y'
        ax.plot(hrTheta, hrR, linewidth = 1, c=color)
        hrTheta =[hrTheta[-1]]
        hrR = [hrR[-1]]
        col.append('y')
    elif data_class.rates[k] >= 120:
        if data_class.piechart:
            color = 'w'
        else:
            color = 'r'
        ax.plot(hrTheta, hrR, linewidth = 1, c=color)
        hrTheta =[hrTheta[-1]]
        hrR = [hrR[-1]]
        col.append('r')
    else:
        if data_class.piechart:
            color = 'w'
        else:
            color = 'b'
        ax.plot(hrTheta, hrR, linewidth = 1, c=color)
        hrTheta =[hrTheta[-1]]
        hrR = [hrR[-1]]
        col.append('b')
    prevHR = k

##########

actTheta = []
actR = []
col = []
color_map = {"shopping": 'r', "going" : 'm', "home event" : 'c',"eating": 'k', "commuting" : 'y', "working" : 'g', "exercising" : 'r', "unknown" : 'w', "sleep" : 'b'}

flag = True


for k in data_class.acts:
    if flag:
        flag = False
        prev = k
    else:
        r = np.ones(int(k) - int(prev)) * 240
        theta = np.linspace(int(prev), int(k), int(k) - int(prev), endpoint=False) * np.pi * 2 / 1440
        ax.plot(theta, r, color = color_map[data_class.acts[prev]], linewidth = 15)
        ax.text(theta[len(theta)// 2], 230, data_class.acts[prev])
        

        if data_class.piechart:
            bars = ax.bar(theta, 240, width=.1)

            for bar in bars:
                bar.set_facecolor(color_map[data_class.acts[prev]])
                bar.set_alpha(0.03)
        prev = k

r = np.ones(int(1430) - int(prev)) * 240
theta = np.linspace(int(prev), int(1430), int(1430) - int(prev), endpoint=False) * np.pi * 2 / 1440
ax.plot(theta, r, color = color_map[data_class.acts[prev]], linewidth = 15)

ax.text(theta[len(theta)// 2], 250, data_class.acts[prev])


if data_class.piechart:
    bars = ax.bar(theta, 240, width=.1)

    for bar in bars:
        bar.set_facecolor(color_map[data_class.acts[prev]])
        bar.set_alpha(0.03)


    




#ax.plot(hrTheta, hrR, linewidth = 1, c='w')
#ax.scatter(myTheta, myR, c = col, s= 1)

ax.set_rmax(242)
ax.set_rticks([50, 80, 100, 130, 170])  # less radial ticks
ax.set_rlabel_position(35)  # get radial labels away from plotted line
ax.set_xticklabels(['12am', '3am', '6am', '9am', '12pm', '3pm', '6pm', '9pm'])
#ax.axes.get_xaxis().set_visible(False)
#ax.axes.get_yaxis().set_visible(False)

ax.grid(True)

ax.set_title("Daily Activites and HeartRate",loc="left", va='bottom')
cid = fig.canvas.mpl_connect('button_press_event', onclick)

print(cid)
print(fig)
plt.show()









