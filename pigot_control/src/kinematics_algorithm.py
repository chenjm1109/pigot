import numpy as np
import math
import tarj_data as td

step_trip = 0.15
offset = 0.5
step_angle = math.pi / 6
turn_para = 2
l1 = 0.15
l2 = 0.35
l3 = 0.35
radio = 40


def forward_gait():
    gait_data = np.zeros((radio, 12))
    rate = 1
    x_line, y_line, z_line = gait_line()
    for t in range(gait_data.shape[0]):
        if (t < 20):
            xf = x_line[t]
            xb = x_line[t + 20]
            yf = y_line[t]
            yb = y_line[t + 20]
            zf = z_line[t]
            zb = z_line[t + 20]
        else:
            xf = x_line[t]
            xb = x_line[t - 20]
            yf = y_line[t]
            yb = y_line[t - 20]
            zf = z_line[t]
            zb = z_line[t - 20]

        lf_theta1, lf_theta2, lf_theta3 = leg_ikine(xf, yf, zf)
        rf_theta1, rf_theta2, rf_theta3 = leg_ikine(xb, yb, zb)
        lb_theta1, lb_theta2, lb_theta3 = leg_ikine(xb, yb, zb)
        rb_theta1, rb_theta2, rb_theta3 = leg_ikine(xf, yf, zf)

        gait_data[t, 0] = lf_theta1
        gait_data[t, 1] = lf_theta2
        gait_data[t, 2] = lf_theta3

        gait_data[t, 3] = rf_theta1
        gait_data[t, 4] = rf_theta2
        gait_data[t, 5] = rf_theta3

        gait_data[t, 6] = lb_theta1
        gait_data[t, 7] = lb_theta2
        gait_data[t, 8] = lb_theta3

        gait_data[t, 9] = rb_theta1
        gait_data[t, 10] = rb_theta2
        gait_data[t, 11] = rb_theta3
    return rate, gait_data

def backward_gait():
    gait_data = np.zeros((radio, 12))
    rate = 1
    x_line, y_line, z_line = gait_line()
    for t in range(gait_data.shape[0]):
        if (t < 20):
            xf = x_line[t]
            xb = x_line[t + 20]
            yf = y_line[t]
            yb = y_line[t + 20]
            zf = -z_line[t]
            zb = -z_line[t + 20]
        else:
            xf = x_line[t]
            xb = x_line[t - 20]
            yf = y_line[t]
            yb = y_line[t - 20]
            zf = -z_line[t]
            zb = -z_line[t - 20]

        lf_theta1, lf_theta2, lf_theta3 = leg_ikine(xf, yf, zf)
        rf_theta1, rf_theta2, rf_theta3 = leg_ikine(xb, yb, zb)
        lb_theta1, lb_theta2, lb_theta3 = leg_ikine(xb, yb, zb)
        rb_theta1, rb_theta2, rb_theta3 = leg_ikine(xf, yf, zf)

        gait_data[t, 0] = lf_theta1
        gait_data[t, 1] = lf_theta2
        gait_data[t, 2] = lf_theta3

        gait_data[t, 3] = rf_theta1
        gait_data[t, 4] = rf_theta2
        gait_data[t, 5] = rf_theta3

        gait_data[t, 6] = lb_theta1
        gait_data[t, 7] = lb_theta2
        gait_data[t, 8] = lb_theta3

        gait_data[t, 9] = rb_theta1
        gait_data[t, 10] = rb_theta2
        gait_data[t, 11] = rb_theta3
    return rate, gait_data

def turnleft_gait():
    gait_data = np.zeros((radio, 12))
    rate = 1
    x_line1, x_line2, y_line1, y_line2, z_line = turn_line()
    for t in range(gait_data.shape[0]):
        xf = x_line1[t]
        xb = x_line2[t]
        yf = y_line1[t]
        yb = y_line2[t]
        z = z_line[t]

        lf_theta1, lf_theta2, lf_theta3 = leg_ikine(xf, yf, z)
        rf_theta1, rf_theta2, rf_theta3 = leg_ikine(xb, yb, z)
        lb_theta1, lb_theta2, lb_theta3 = leg_ikine(xb, yb, z)
        rb_theta1, rb_theta2, rb_theta3 = leg_ikine(xf, yf, z)

        gait_data[t, 0] = lf_theta1
        gait_data[t, 1] = lf_theta2
        gait_data[t, 2] = lf_theta3

        gait_data[t, 3] = rf_theta1
        gait_data[t, 4] = rf_theta2
        gait_data[t, 5] = rf_theta3

        gait_data[t, 6] = lb_theta1
        gait_data[t, 7] = lb_theta2
        gait_data[t, 8] = lb_theta3

        gait_data[t, 9] = rb_theta1
        gait_data[t, 10] = rb_theta2
        gait_data[t, 11] = rb_theta3
    return rate, gait_data

def turnright_gait():
    gait_data = np.zeros((radio, 12))
    rate = 1
    x_line1, x_line2, y_line1, y_line2, z_line = turn_line()
    for t in range(gait_data.shape[0]):
        xf = x_line1[t]
        xb = x_line2[t]
        yf = y_line1[t]
        yb = y_line2[t]
        z = z_line[t]

        lf_theta1, lf_theta2, lf_theta3 = leg_ikine(xb, yb, z)
        rf_theta1, rf_theta2, rf_theta3 = leg_ikine(xf, yf, z)
        lb_theta1, lb_theta2, lb_theta3 = leg_ikine(xf, yf, z)
        rb_theta1, rb_theta2, rb_theta3 = leg_ikine(xb, yb, z)

        gait_data[t, 0] = lf_theta1
        gait_data[t, 1] = lf_theta2
        gait_data[t, 2] = lf_theta3

        gait_data[t, 3] = rf_theta1
        gait_data[t, 4] = rf_theta2
        gait_data[t, 5] = rf_theta3

        gait_data[t, 6] = lb_theta1
        gait_data[t, 7] = lb_theta2
        gait_data[t, 8] = lb_theta3

        gait_data[t, 9] = rb_theta1
        gait_data[t, 10] = rb_theta2
        gait_data[t, 11] = rb_theta3
    return rate, gait_data

def jump_gait():

    return 

def keep_gait():
    gait_data = np.zeros((radio, 12))
    rate = 1
    x_line, y_line, z_line = keep_line()
    for t in range(gait_data.shape[0]):
        if (t < 20):
            xf = x_line[t]
            xb = x_line[t + 20]
            yf = y_line[t]
            yb = y_line[t + 20]
            zf = z_line[t]
            zb = z_line[t + 20]
        else:
            xf = x_line[t]
            xb = x_line[t - 20]
            yf = y_line[t]
            yb = y_line[t - 20]
            zf = z_line[t]
            zb = z_line[t - 20]

        lf_theta1, lf_theta2, lf_theta3 = leg_ikine(xf, yf, zf)
        rf_theta1, rf_theta2, rf_theta3 = leg_ikine(xb, yb, zb)
        lb_theta1, lb_theta2, lb_theta3 = leg_ikine(xb, yb, zb)
        rb_theta1, rb_theta2, rb_theta3 = leg_ikine(xf, yf, zf)

        gait_data[t, 0] = lf_theta1
        gait_data[t, 1] = lf_theta2
        gait_data[t, 2] = lf_theta3

        gait_data[t, 3] = rf_theta1
        gait_data[t, 4] = rf_theta2
        gait_data[t, 5] = rf_theta3

        gait_data[t, 6] = lb_theta1
        gait_data[t, 7] = lb_theta2
        gait_data[t, 8] = lb_theta3

        gait_data[t, 9] = rb_theta1
        gait_data[t, 10] = rb_theta2
        gait_data[t, 11] = rb_theta3
    return rate, gait_data

    
def leg_ikine(x, y, z):  
    theta1 = math.atan2(y, x) + math.atan2(l1, -(x**2 + y**2 - l1**2)**0.5)
    c1 = math.cos(theta1)    
    s1 = math.sin(theta1) 
    c3 = (x**2 + y**2 + z**2 - l1**2 - l2**2 - l3**2) / (2 * l2 * l3)
    s3 = (1 - c3**2)**0.5
    theta3 = math.atan2(s3, c3)
    s2p = (l3 * s3) / ((y * s1 + x * c1)**2 + z**2)**0.5
    c2p = (1 - s2p**2)**0.5
    theta2p = -math.atan2(s2p, c2p)
    thetap = -math.atan2(z, -(y * s1 + x * c1))
    theta2 = theta2p - thetap
    return theta1 - math.pi, theta2, theta3


def gait_line():
    data = td.forward_gait()
    x_line = data[0, :]
    y_line = data[1, :]
    z_line = data[2, :]
    return x_line, y_line, z_line

def keep_line():
    data = td.keep_gait()
    x_line = data[0, :]
    y_line = data[1, :]
    z_line = data[2, :]
    return x_line, y_line, z_line

def turn_line():
    data = td.turn_gait()
    x_line1 = data[0, :]
    x_line2 = data[1, :]
    y_line1 = data[2, :]
    y_line2 = data[3, :]
    z_line = data[4, :]
    return x_line1, x_line2, y_line1, y_line2, z_line

def jump_line():
    xf_line = np.zeros((20))

    return


