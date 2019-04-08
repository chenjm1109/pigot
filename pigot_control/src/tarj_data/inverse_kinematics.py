import math
from decimal import *
import numpy as np

getcontext().prec = 50

l1 = 0.15
l2 = 0.35
l3 = 0.35


def leg_ikine(x, y, z):  
    theta1 = math.atan2(y, x) + math.atan2(l1, -(x**2 + y**2 - l1**2)**0.5)
    c1 = math.cos(theta1)    
    s1 = math.sin(theta1) 
    c3 = (x**2 + y**2 + z**2 - l1**2 - l2**2 - l3**2) / (2 * l2 * l3)
    s3 = (1 - c3**2)**0.5
    theta3 = math.atan2(s3, c3)
    s2p = (l3 * s3) / ((y * s1 + x * c1)**2 + z**2)**0.5
    c2p = (1 - s2p**2)**0.5
    theta2p = math.atan2(s2p, c2p)
    thetap = math.atan2(z, -(y * s1 + x * c1))
    theta2 = thetap - theta2p
    return theta1 - math.pi, theta2, theta3
    
def leg_fkine(theta1, theta2, theta3):
    theta1 = theta1 * math.pi / 180
    theta2 = theta2 * math.pi / 180
    theta3 = theta3 * math.pi / 180
    x = l1 * math.sin(theta1) + l2 * math.cos(theta1) * math.cos(theta2) + l3 * math.cos(theta1) * math.cos(theta2 + theta3)
    y = l1 * math.cos(theta1) + l2 * math.sin(theta1) * math.cos(theta2) + l3 * math.sin(theta1) * math.cos(theta2 + theta3)
    z = l2 * math.sin(theta2) + l3 * math.sin(theta2 + theta3)
    return x, y, z


#x, y, z = leg_fkine(0, 45, 0)
theta1, theta2, theta3 = leg_ikine(0.4949, 0.2, 0)



theta1 = theta1 * 180 / math.pi
theta2 = theta2 * 180 / math.pi
theta3 = theta3 * 180 / math.pi
'''
data = np.array([0,0,0,0,0,0])
step_length = 3
for i in range(-45, 45, step_length):
    for j in range(-90, 45, step_length):
        for k in range(0, 180, step_length):
            x, y, z = leg_fkine(i, j, k)
            data_new = np.array([x, y, z, i, j, k])
            data = np.vstack((data, data_new))
'''           

