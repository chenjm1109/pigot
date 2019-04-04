import numpy as np
import math

step_trip = 0.15
offset = 0.5
step_angle = math.pi / 6
turn_para = 2
L1 = 0.35
L2 = 0.35



def forward_gait():
    radio = 20
    gait_data = np.zeros((radio, 12))
    rate = 1
    x_line, y_line = gait_line()
    for t in range(gait_data.shape[0]):
        if (t < 10):
            xf = x_line[t]
            xb = x_line[t + 10]
            yf = y_line[t]
            yb = y_line[t + 10]
        else:
            xf = x_line[t]
            xb = x_line[t - 10]
            yf = y_line[t]
            yb = y_line[t - 10]

        lf_theta1, lf_theta2 = leg_ikine(xf, yf)
        rf_theta1, rf_theta2 = leg_ikine(xb, yb)
        lb_theta1, lb_theta2 = leg_ikine(xb, yb)
        rb_theta1, rb_theta2 = leg_ikine(xf, yf)


        gait_data[t, 0] = 0.05
        gait_data[t, 1] = lf_theta1
        gait_data[t, 2] = lf_theta2

        gait_data[t, 3] = 0.05
        gait_data[t, 4] = rf_theta1
        gait_data[t, 5] = rf_theta2

        gait_data[t, 6] = 0.05
        gait_data[t, 7] = lb_theta1
        gait_data[t, 8] = lb_theta2

        gait_data[t, 9] = 0.05
        gait_data[t, 10] = rb_theta1
        gait_data[t, 11] = rb_theta2
    return rate, gait_data

def backward_gait():
    radio = 20
    gait_data = np.zeros((radio, 12))
    rate = 1
    x_line, y_line = gait_line()
    for t in range(gait_data.shape[0]):
        if (t < 10):
            xf = x_line[t]
            xb = x_line[t + 10]
            yf = -y_line[t]
            yb = -y_line[t + 10]
        else:
            xf = x_line[t]
            xb = x_line[t - 10]
            yf = -y_line[t]
            yb = -y_line[t - 10]

        lf_theta1, lf_theta2 = leg_ikine(xf, yf)
        rf_theta1, rf_theta2 = leg_ikine(xb, yb)
        lb_theta1, lb_theta2 = leg_ikine(xb, yb)
        rb_theta1, rb_theta2 = leg_ikine(xf, yf)


        gait_data[t, 0] = 0
        gait_data[t, 1] = lf_theta1
        gait_data[t, 2] = lf_theta2

        gait_data[t, 3] = 0
        gait_data[t, 4] = rf_theta1
        gait_data[t, 5] = rf_theta2

        gait_data[t, 6] = 0
        gait_data[t, 7] = lb_theta1
        gait_data[t, 8] = lb_theta2

        gait_data[t, 9] = 0
        gait_data[t, 10] = rb_theta1
        gait_data[t, 11] = rb_theta2
    return rate, gait_data

def turnleft_gait():
    radio = 20
    gait_data = np.zeros((radio, 12))
    rate = 1
    x_line1, x_line2, y_line, t_line1, t_line2 = turn_line()
    for t in range(gait_data.shape[0]):
        xf = x_line1[t]
        xb = x_line2[t]
        y = y_line[t]
        tf = t_line1[t]
        tb = t_line2[t]

        lf_theta1, lf_theta2 = leg_ikine(xf, y)
        rf_theta1, rf_theta2 = leg_ikine(xb, y)
        lb_theta1, lb_theta2 = leg_ikine(xb, y)
        rb_theta1, rb_theta2 = leg_ikine(xf, y)


        gait_data[t, 0] = tf
        gait_data[t, 1] = lf_theta1
        gait_data[t, 2] = lf_theta2

        gait_data[t, 3] = -tb
        gait_data[t, 4] = rf_theta1
        gait_data[t, 5] = rf_theta2

        gait_data[t, 6] = -tb
        gait_data[t, 7] = lb_theta1
        gait_data[t, 8] = lb_theta2

        gait_data[t, 9] = tf
        gait_data[t, 10] = rb_theta1
        gait_data[t, 11] = rb_theta2
    return rate, gait_data
    return rate, gait_data

def turnright_gait():
    radio = 20
    gait_data = np.zeros((radio, 12))
    rate = 1
    x_line1, x_line2, y_line, t_line1, t_line2 = turn_line()
    for t in range(gait_data.shape[0]):
        xf = x_line1[t]
        xb = x_line2[t]
        y = y_line[t]
        tf = t_line1[t]
        tb = t_line2[t]

        lf_theta1, lf_theta2 = leg_ikine(xb, y)
        rf_theta1, rf_theta2 = leg_ikine(xf, y)
        lb_theta1, lb_theta2 = leg_ikine(xf, y)
        rb_theta1, rb_theta2 = leg_ikine(xb, y)


        gait_data[t, 0] = tb
        gait_data[t, 1] = lf_theta1
        gait_data[t, 2] = lf_theta2

        gait_data[t, 3] = tf
        gait_data[t, 4] = rf_theta1
        gait_data[t, 5] = rf_theta2

        gait_data[t, 6] = tf
        gait_data[t, 7] = lb_theta1
        gait_data[t, 8] = lb_theta2

        gait_data[t, 9] = tb
        gait_data[t, 10] = rb_theta1
        gait_data[t, 11] = rb_theta2
    return rate, gait_data

def jump_gait():
    radio = 20
    gait_data = np.zeros((radio, 12))
    rate = 1
    xf_line, yf_line, xb_line, yb_line = jump_line()
    for t in range(gait_data.shape[0]):
        xf = xf_line[t]
        yf = yf_line[t]
        xb = xb_line[t]
        yb = yb_line[t]

        lf_theta1, lf_theta2 = leg_ikine(xf, yf)
        rf_theta1, rf_theta2 = leg_ikine(xf, yf)
        lb_theta1, lb_theta2 = leg_ikine(xb, yb)
        rb_theta1, rb_theta2 = leg_ikine(xb, yb)


        gait_data[t, 0] = 0
        gait_data[t, 1] = lf_theta1
        gait_data[t, 2] = lf_theta2

        gait_data[t, 3] = 0
        gait_data[t, 4] = rf_theta1
        gait_data[t, 5] = rf_theta2

        gait_data[t, 6] = 0
        gait_data[t, 7] = lb_theta1
        gait_data[t, 8] = lb_theta2

        gait_data[t, 9] = 0
        gait_data[t, 10] = rb_theta1
        gait_data[t, 11] = rb_theta2
    return rate, gait_data

def keep_gait():
    radio = 20
    gait_data = np.zeros((radio, 12))
    rate = 1
    x_line, y_line = keep_line()
    for t in range(gait_data.shape[0]):
        if (t < 10):
            xf = x_line[t]
            xb = x_line[t + 10]
            yf = y_line[t]
            yb = y_line[t + 10]
        else:
            xf = x_line[t]
            xb = x_line[t - 10]
            yf = y_line[t]
            yb = y_line[t - 10]

        lf_theta1, lf_theta2 = leg_ikine(xf, yf)
        rf_theta1, rf_theta2 = leg_ikine(xb, yb)
        lb_theta1, lb_theta2 = leg_ikine(xb, yb)
        rb_theta1, rb_theta2 = leg_ikine(xf, yf)


        gait_data[t, 0] = 0.05
        gait_data[t, 1] = lf_theta1
        gait_data[t, 2] = lf_theta2

        gait_data[t, 3] = 0.05
        gait_data[t, 4] = rf_theta1
        gait_data[t, 5] = rf_theta2

        gait_data[t, 6] = 0.05
        gait_data[t, 7] = lb_theta1
        gait_data[t, 8] = lb_theta2

        gait_data[t, 9] = 0.05
        gait_data[t, 10] = rb_theta1
        gait_data[t, 11] = rb_theta2
    return rate, gait_data

    
def leg_ikine(x,y):
    c2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    s2 = (1 - c2**2) ** 0.5 # Take the positive solution here.
    theta2 = math.atan2(s2, c2)
    k1 = L1 + L2 * c2
    k2 = L2 * s2
    theta1 = math.atan2(y, x) - math.atan2(k2, k1)
    return theta1, theta2


def gait_line():
    x_line = np.zeros((20))
    y_line = np.zeros((20))

    x_line[0 : 5] = np.linspace(0.46, 0.5, 5)
    x_line[5 : 15] = np.linspace(0.5, 0.5, 10)
    x_line[15 : 20] = np.linspace(0.5, 0.46, 5)

    y_line[0 : 5] = np.linspace(0.0, 0.0, 5)
    y_line[5 : 15] = np.linspace(0.0, -0.25, 10)
    y_line[15 : 20] = np.linspace(-0.25, 0.0, 5)

    return x_line, y_line

def keep_line():
    x_line = np.zeros((20))
    y_line = np.zeros((20))

    x_line[0 : 5] = np.linspace(0.47, 0.5, 5)
    x_line[5 : 15] = np.linspace(0.5, 0.5, 10)
    x_line[15 : 20] = np.linspace(0.5, 0.47, 5)

    y_line[0 : 5] = np.linspace(0.0, 0.03, 5)
    y_line[5 : 15] = np.linspace(0.03, -0.03, 10)
    y_line[15 : 20] = np.linspace(-0.03, 0.0, 5)

    return x_line, y_line

def turn_line():
    x_line1 = np.zeros((20))
    x_line2 = np.zeros((20))
    y_line = np.zeros((20))
    t_line1 = np.zeros((20))
    t_line2 = np.zeros((20))

    x_line1[0 : 4] = np.linspace(0.5, 0.45, 4)
    x_line1[4 : 8] = np.linspace(0.45, 0.45, 4)
    x_line1[8 : 12] = np.linspace(0.45, 0.5, 4)
    x_line1[12 : 16] = np.linspace(0.5, 0.5, 4)
    x_line1[16 : 20] = np.linspace(0.5, 0.5, 4)

    x_line2[0 : 4] = np.linspace(0.5, 0.5, 4)
    x_line2[4 : 8] = np.linspace(0.5, 0.5, 4)
    x_line2[8 : 12] = np.linspace(0.5, 0.45, 4)
    x_line2[12 : 16] = np.linspace(0.45, 0.48, 4)
    x_line2[16 : 20] = np.linspace(0.48, 0.5, 4)

    # Stand in place. There are some paramester to adjust the error which moves robot backward.
    y_line[0 : 20] = np.linspace(0.0, 0.0, 20)


    t_line1[0 : 4] = np.linspace(0.0, 0.0, 4)
    t_line1[4 : 8] = np.linspace(0.0, math.pi / 15, 4)
    t_line1[8 : 12] = np.linspace(math.pi / 15, math.pi / 15, 4)
    t_line1[12 : 16] = np.linspace(math.pi / 15, 0.0, 4)
    t_line1[16 : 20] = np.linspace(0.0, 0.0, 4)

    t_line2[0 : 4] = np.linspace(0.0, 0.0, 4)
    t_line2[4 : 8] = np.linspace(0.0, 0.0, 4)
    t_line2[8 : 12] = np.linspace(0.0, 0.0, 4)
    t_line2[12 : 16] = np.linspace(0.0, 0.0, 4)
    t_line2[16 : 20] = np.linspace(0.0, 0.0, 4)

    return x_line1, x_line2, y_line, t_line1, t_line2

def jump_line():
    xf_line = np.zeros((20))
    yf_line = np.zeros((20))
    xb_line = np.zeros((20))
    yb_line = np.zeros((20))

    xb_line[0 : 7] = np.linspace(0.5, 0.3, 7)
    xb_line[7 : 8] = np.linspace(0.3, 0.5, 1)
    xb_line[8 : 20] = np.linspace(0.5, 0.5, 12)

    yb_line[0 : 7] = np.linspace(0.0, 0.0, 7)
    yb_line[7 : 8] = np.linspace(0.0, -0.4, 1)
    yb_line[8 : 20] = np.linspace(-0.4, 0.0, 12)

    xf_line[0 : 7] = np.linspace(0.5, 0.5, 7)
    xf_line[7 : 17] = np.linspace(0.5, 0.3, 10)
    xf_line[17 : 20] = np.linspace(0.3, 0.5, 3)

    yf_line[0 : 7] = np.linspace(0.0, 0.0, 7)
    yf_line[7 : 17] = np.linspace(0.0, 0.4, 10)
    yf_line[17 : 20] = np.linspace(0.4, 0.0, 3)

    return xf_line, yf_line, xb_line, yb_line


