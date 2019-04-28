# -*-coding:utf-8 -*-
import numpy as np
import math
from scipy import interpolate

step_num = 40

def forward_gait():
    # Standard cycloidal equation.
    v_E1 = 0.1 # For example, 0.1
    v_E2 = 0.025 # For example, 0.1
    
    # 标准摆线方程
    x, y, z = np.zeros(step_num / 2), np.zeros(step_num / 2), np.zeros(step_num / 2)
    E_long = v_E1 # 纵向步长，决定线速度
    E_lateral = v_E2 # 横向步长，决定线速度
    h = 0.1 # 步高
    theta = np.linspace(0, 2 * math.pi, step_num / 2)
    for i in range(step_num / 2):
      x[i] = h * (1 - math.cos(theta[i])) / 2
      y[i] = E_lateral * (theta[i] - math.sin(theta[i])) / (2 * math.pi)
      z[i] = E_long * (theta[i] - math.sin(theta[i])) / (2 * math.pi)
        
    
    # Correction of cycloid position
    x = - x + 0.6
    y = y - E_lateral
    z = z + E_long * 3.0 / 4
    
    x_gait = np.hstack((x[10 : 20], x[0 : 20]**0 * x[19], x[0 : 10]))
    y_gait = np.hstack((y[10 : 20], np.linspace(y[19], y[0], step_num / 2), y[0 : 10]))
    z_gait = np.hstack((z[10 : 20], np.linspace(z[19], z[0], step_num / 2), z[0 : 10]))
    forward_gait = np.vstack((x_gait, y_gait, z_gait))
    return forward_gait
    
#def forward_gait():
#    # Standard cycloidal equation.
#    z, x = np.zeros(step_num / 2), np.zeros(step_num / 2)
#    E = 0.2 # step length
#    h = 0.1 # step height
#    theta = np.linspace(0, 2 * math.pi, step_num / 2)
#    for i in range(step_num / 2):
#        z[i] = E * (theta[i] - math.sin(theta[i])) / (2 * math.pi)
#        x[i] = h * (1 - math.cos(theta[i])) / 2
#    
#    # Correction of cycloid position
#    z = z - E * 1 / 4
#    x = - x + 0.6
#    y = [0.15, 0.15,  0.15,  0.15]
#    
#    x_gait = np.hstack((x[10 : 20], x[0 : 20]**0 * x[19], x[0 : 10]))
#    y_gait = interpolate_method(y)
#    z_gait = np.hstack((z[10 : 20], np.linspace(z[19], z[0], step_num / 2), z[0 : 10]))
#    forward_gait = np.vstack((x_gait, y_gait, z_gait))
#    return forward_gait

def forward_gait2():
    x = [0.55, 0.60,  0.60,  0.55]
    y = [0.15, 0.15,  0.15,  0.15]
    z = [0.00, 0.00, -0.1,  0.00]
    x_gait = interpolate_method(x)
    y_gait = interpolate_method(y)
    z_gait = interpolate_method(z)
    forward_gait = np.vstack((x_gait, y_gait, z_gait))
    return forward_gait

def keep_gait():
    x = [0.5 , 0.60,  0.60,  0.5 ]
    y = [0.15, 0.15, 0.15,  0.15]
    z = [-0.05,  -0.05,  -0.05,  -0.05 ]
    x_gait = interpolate_method(x)
    y_gait = interpolate_method(y)
    z_gait = interpolate_method(z)
    keep_gait = np.vstack((x_gait, y_gait, z_gait))
    return keep_gait
   
def turn_gait(direction):
    # Calculate the landing points after turning
    turn_angle = - direction * 10 * math.pi / 180
    old_foot_y = np.array([-0.35,  0.35, -0.35,  0.35]) # The width direction
    old_foot_z = np.array([ 0.40,  0.40, -0.40, -0.40]) # The length direction
    new_foot_y, new_foot_z = np.zeros(4), np.zeros(4)
    r = (0.35**2 + 0.40**2) ** 0.5
    for i in range(4):
        theta = math.atan2(old_foot_z[i], old_foot_y[i]) - turn_angle
        new_foot_y[i] = r * math.cos(theta)
        new_foot_z[i] = r * math.sin(theta)
    
    # Calculate the offset of the landing points.
    offset_y, offset_z = np.zeros(4), np.zeros(4)
    offset_y = new_foot_y - old_foot_y
    offset_z = new_foot_z - old_foot_z
    offset_y[0], offset_y[2] = -offset_y[0], -offset_y[2]
    
    
    x1 = [0.60, 0.55, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60 ]
    x2 = [0.60, 0.60, 0.60, 0.55, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60 ] 
    x3 = [0.60, 0.60, 0.60, 0.60, 0.60, 0.55, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60 ]
    x4 = [0.60, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60, 0.55, 0.60, 0.60, 0.60, 0.60 ]

    y1 = np.hstack((np.linspace(0.15, 0.15 + offset_y[0], 3), np.linspace(0.15 + offset_y[0], 0.15 + offset_y[0], 6), np.linspace(0.15 + offset_y[0], 0.15, 3)))
    y2 = np.hstack((np.linspace(0.15, 0.15, 2), np.linspace(0.15, 0.15 + offset_y[1], 3), np.linspace(0.15 + offset_y[1], 0.15 + offset_y[1], 4), np.linspace(0.15 + offset_y[1], 0.15, 3)))
    y3 = np.hstack((np.linspace(0.15, 0.15, 4), np.linspace(0.15, 0.15 + offset_y[2], 3), np.linspace(0.15 + offset_y[2], 0.15 + offset_y[2], 2), np.linspace(0.15 + offset_y[2], 0.15, 3)))
    y4 = np.hstack((np.linspace(0.15, 0.15, 6), np.linspace(0.15, 0.15 + offset_y[3], 3), np.linspace(0.15 + offset_y[3], 0.15, 3)))

    z1 = np.hstack((np.linspace(0., 0. + offset_z[0], 3), np.linspace(0. + offset_z[0], 0. + offset_z[0], 6), np.linspace(0. + offset_z[0], 0., 3)))
    z2 = np.hstack((np.linspace(0., 0., 2), np.linspace(0., 0. + offset_z[1], 3), np.linspace(0. + offset_z[1], 0. + offset_z[1], 4), np.linspace(0. + offset_z[1], 0., 3)))
    z3 = np.hstack((np.linspace(0., 0., 4), np.linspace(0., 0. + offset_z[2], 3), np.linspace(0. + offset_z[2], 0. + offset_z[2], 2), np.linspace(0. + offset_z[2], 0., 3)))
    z4 = np.hstack((np.linspace(0., 0., 6), np.linspace(0., 0. + offset_z[3], 3), np.linspace(0. + offset_z[3], 0., 3)))
    
    x1_gait = interpolate_method(x1)
    x2_gait = interpolate_method(x2)
    x3_gait = interpolate_method(x3)
    x4_gait = interpolate_method(x4)
    
    y1_gait = interpolate_method(y1.tolist())
    y2_gait = interpolate_method(y2.tolist())
    y3_gait = interpolate_method(y3.tolist())
    y4_gait = interpolate_method(y4.tolist())
    
    z1_gait = interpolate_method(z1.tolist())
    z2_gait = interpolate_method(z2.tolist())
    z3_gait = interpolate_method(z3.tolist())
    z4_gait = interpolate_method(z4.tolist())
    
    turn_gait = np.vstack((x1_gait, x2_gait, x3_gait, x4_gait, 
                           y1_gait, y2_gait, y3_gait, y4_gait, 
                           z1_gait, z2_gait, z3_gait, z4_gait))
    return turn_gait

def slantleft_gait(direction):
    slant_length = 0.05
    # Standard cycloidal equation.
    z, x = np.zeros(step_num / 2), np.zeros(step_num / 2)
    E = 0.1 # step length
    h = 0.05 # step height
    theta = np.linspace(0, 2 * math.pi, step_num / 2)
    for i in range(step_num / 2):
        z[i] = E * (theta[i] - math.sin(theta[i])) / (2 * math.pi)
        x[i] = h * (1 - math.cos(theta[i])) / 2
    
    # Correction of cycloid position
    z = z - E / 2
    x = - x + 0.6
    y = [0.15, 0.15,  0.15,  0.15]
    
    x1_gait = np.hstack((x[10 : 20], x[0 : 20]**0 * x[19], x[0 : 10]))
    x2_gait = np.hstack((x1_gait[20 : 40], x1_gait[0 : 20]))

    if direction==1:
        y1_gait = np.hstack((np.linspace(0.15 + slant_length/2, 0.15 + slant_length, 10), np.linspace(0.15 + slant_length, 0.15, 20), np.linspace(0.15, 0.15 + slant_length/2, 10) ))
        y2_gait = np.hstack((np.linspace(0.15 - slant_length/2, 0.15, 10), np.linspace(0.15, 0.15 - slant_length, 20), np.linspace(0.15 - slant_length, 0.15 - slant_length/2, 10) ))
    elif direction==-1:
        y1_gait = np.hstack((np.linspace(0.15 - slant_length/2, 0.1, 10), np.linspace(0.15 - slant_length, 0.15, 20), np.linspace(0.15, 0.15 - slant_length/2, 10) ))
        y2_gait = np.hstack((np.linspace(0.15 + slant_length/2, 0.15, 10), np.linspace(0.15, 0.15 + slant_length, 20), np.linspace(0.15 + slant_length, 0.15 + slant_length/2, 10) ))

    z1_gait = np.hstack((z[10 : 20], np.linspace(z[19], z[0], step_num / 2), z[0 : 10]))
    z2_gait = np.hstack((z1_gait[20 : 40], z1_gait[0 : 20]))
    slantleft_gait = np.vstack((x1_gait, x2_gait,  
                                y1_gait, y2_gait, 
                                z1_gait, z2_gait))
    return slantleft_gait




def interpolate_method(y):
    t = len(y)
    x = np.linspace(0, t, t)
    xnew=np.linspace(0, t, step_num)
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

a = forward_gait()
print(a)
