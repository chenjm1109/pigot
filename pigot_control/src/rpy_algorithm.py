import numpy as np
import math
import tarj_data as td
import attitude_control as ac

step_trip = 0.15
offset = 0.5
step_angle = math.pi / 6
turn_para = 2
l1 = 0.15
l2 = 0.35
l3 = 0.35
radio = 40


def rpy_gait(RPY_angle_old, RPY_angle_new_traj):
    gait_data = np.zeros((radio, 12))
    rate = 1
    RPY_angle_new_traj = np.array(RPY_angle_new_traj)
    traj = np.vstack((RPY_angle_old, RPY_angle_new_traj))
    RPY_B_traj = np.zeros((40,3))
    print(RPY_B_traj)
    print(traj)
    for i in range (3):
        RPY_B_traj[:, i] = td.interpolate_method(traj[:, i].tolist())
    print(RPY_B_traj)
    for t in range(RPY_B_traj.shape[0]):
        R = RPY_B_traj[t, 0]
        P = RPY_B_traj[t, 1]
        Y = RPY_B_traj[t, 2]

        pos_data = ac.rpy_control(R, P, Y)

        lf_theta1, lf_theta2, lf_theta3 = leg_ikine(pos_data[0,0], pos_data[0,1], pos_data[0,2])
        rf_theta1, rf_theta2, rf_theta3 = leg_ikine(pos_data[1,0], pos_data[1,1], pos_data[1,2])
        lb_theta1, lb_theta2, lb_theta3 = leg_ikine(pos_data[2,0], pos_data[2,1], pos_data[2,2])
        rb_theta1, rb_theta2, rb_theta3 = leg_ikine(pos_data[3,0], pos_data[3,1], pos_data[3,2])

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



