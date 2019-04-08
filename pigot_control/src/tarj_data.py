# -*-coding:utf-8 -*-
import numpy as np
from scipy import interpolate
# import pylab as pl

def forward_gait():
    x = [0.46, 0.50,  0.50,  0.46]
    y = [0.15, 0.15,  0.15,  0.15]
    z = [0.00, 0.00, -0.25,  0.00]
    x_gait = interpolate_method(x)
    y_gait = interpolate_method(y)
    z_gait = interpolate_method(z)
    forward_gait = np.vstack((x_gait, y_gait, z_gait))
    return forward_gait
    
def keep_gait():
    x = [0.47, 0.5,  0.5,  0.47]
    y = [0.15,  0.15,  0.15,  0.15]
    z = [0.0,  0.0,  0.0,  0.0 ]
    x_gait = interpolate_method(x)
    y_gait = interpolate_method(y)
    z_gait = interpolate_method(z)
    keep_gait = np.vstack((x_gait, y_gait, z_gait))
    return keep_gait
    
def turn_gait():
    x1 = [0.5, 0.45, 0.45, 0.5, 0.5]
    x2 = [0.5, 0.5, 0.4, 0.45, 0.5] 
    y1 = [0.15, 0.2,  0.2,  0.2, 0.15]
    y2 = [0.15, 0.15,  0.15,  0.15, 0.15]
    z =  [0.0, 0.0,  0.0,  0.0, 0.0]
    x1_gait = interpolate_method(x1)
    x2_gait = interpolate_method(x2)
    y1_gait = interpolate_method(y1)
    y2_gait = interpolate_method(y2)
    z_gait = interpolate_method(z)
    turn_gait = np.vstack((x1_gait, x2_gait, y1_gait, y2_gait, z_gait))
    return turn_gait

def interpolate_method(y):
    t = len(y)
    x = np.linspace(0, t, t)
    xnew=np.linspace(0, t, 40)
    #pl.plot(x,y,"ro")
    for kind in ["slinear"]:#插值方式
        #"nearest","zero"为阶梯插值
        #slinear 线性插值
        #"quadratic","cubic" 为2阶、3阶B样条曲线插值
        f=interpolate.interp1d(x,y,kind=kind)
        # ‘slinear’, ‘quadratic’ and ‘cubic’ refer to a spline interpolation of first, second or third order)
        ynew=f(xnew)
        #pl.plot(xnew,ynew,label=str(kind))
    #pl.legend(loc="lower right")
    #pl.show()
    return ynew
    
print(interpolate_method([1,2]))


