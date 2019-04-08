# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:57:11 2019

@author: jim
"""
import numpy as np
from math import *

def rpy_control(R, P, Y):
    # Define the structure paramesters of robot
    l = 0.8 # The length of platform.
    w = 0.8 # The width of platform.
    
    # Rebuild the Euler-angle.
    R = R
    P = P
    Y = Y
    
    # Foot position vector
    det = np.array([[ l/2, -0.55, -0.55],
                    [ l/2, -0.55,  0.55],
                    [-l/2, -0.55, -0.55],
                    [-l/2, -0.55,  0.55],])
    
    pos_data = np.zeros((4, 3))
    for i in range(4):
        detx = det[i, 0]
        dety = det[i, 1]
        detz = det[i, 2]
        rotx = np.mat([[ 1,       0,       0     ],
                       [ 0,       cos(R), -sin(R)],
                       [ 0,       sin(R),  cos(R)]])
                      
        rotz = np.mat([[ cos(P), -sin(P),  0     ],
                       [ sin(P),  cos(P),  0     ],
                       [ 0,       0,       1     ]])
                       
        roty = np.mat([[ cos(Y),  0,      -sin(Y)],
                       [ 0,       1,       0     ],
                       [ sin(Y),  0,       cos(Y)]]) 
        det_vec = np.mat([[detx], [dety], [detz]])
        off_vec = np.mat([[ l/2, l/2, -l/2, -l/2], 
                          [ 0,   0,    0,    0  ], 
                          [-w/2, w/2, -w/2, w/2 ]])
        pos_vec = rotx * roty * rotz * det_vec - off_vec[:, i]
        # Converte the global coordinate into the kinematics coordinates of each leg.  
        x = -pos_vec[1]
        z = pos_vec[0]
        if (i%2)==0 :
            y = -pos_vec[2]
        else:
            y = pos_vec[2]
        pos_data[i, :] = np.array([x, y, z]).T
    return pos_data

