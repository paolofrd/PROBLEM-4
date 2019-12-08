import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch

h = int(input('Input initial height: '))
vi = int(input('Input the velocity: '))
angle = int(input('Input the angle (degrees) of projection: '))
ax = int(input('Input horizontal acceleration (always negative: '))


x = True

while x is True:
    ay = int(input('Input vertical acceleration: '))
    if (ay == 0):
        print ('Vertical acceleration cannot be zero. Input another one.')
        x = True
    elif ay > 0:
        ay = -ay
        x = False
    elif ay < 0:
        ay = ay
        x = False
        
#convertion of degrees to radians
def rad(angle):
    angle = angle*(math.pi/180)
    return angle

vix = vi*math.cos(rad(angle))
viy = vi*math.sin(rad(angle))

#ideal motion
t_roots = []
t_positive = []
t = [(1/2)*(-9.8),viy,h] #polynomial
t_roots.extend(np.roots(t)) #transfer the roots to array t_roots

#extract the real numbers in array t_roots to t_positive
for i in t_roots:
    if i > 0:
        t_positive.append(i)

#create in interval using array t_positive
time = np.linspace(0,t_positive,50)
x = np.multiply(vix,time)
y = [] #y storage

#computation for y at a certain time
for i in range(0,50):
    if time[i] ==    0:
        fy = h
    elif time[i] > 0:
        fy = viy*time[i] + (1/2)*(-9.8)*(time[i]**2) + h
    
    y.append(fy) #store y values
    
plt.plot(x,y)

#non-ideal motion
it_roots = []
it_positive = []
ia = (1/2)*ay
it = [ia,viy,h]
it_roots.extend(np.roots(it))

for i in it_roots:
    if i > 0:
        it_positive.append(i)

itime = np.linspace(0,it_positive,50)
ix = np.multiply(vix,itime) + (1/2)*(np.multiply(ax,(np.square(itime))))
iy = []

for i in range(0,50):
    if itime[i] == 0:
        ify = h
    elif itime[i] > 0:
        ify = viy*itime[i] + (1/2)*ay*(itime[i]**2) + h
    iy.append(ify)

#plotting
plt.grid()
plt.plot(ix,iy)
plt.title('Projectile Motion')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
blu = mpatch.Patch(color = 'blue', label = 'Ideal model') #add custom legend
orange = mpatch.Patch(color = 'orange', label = 'Non-ideal')
plt.legend(handles = [blu,orange]) #apply legend to graph
plt.show()