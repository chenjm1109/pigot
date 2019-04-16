#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Float64
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
import numpy as np
import rpy_algorithm as rpy

cycle_gait_data = Float32MultiArray()

if __name__ == '__main__':
    try:
        rospy.init_node('rpy_pub_node', anonymous=True)
        joint1_pos_pub = rospy.Publisher('/pigot/joint1_position_controller/command', Float64, queue_size=10)
        joint2_pos_pub = rospy.Publisher('/pigot/joint2_position_controller/command', Float64, queue_size=10)
        joint3_pos_pub = rospy.Publisher('/pigot/joint3_position_controller/command', Float64, queue_size=10)
        joint4_pos_pub = rospy.Publisher('/pigot/joint4_position_controller/command', Float64, queue_size=10)
        joint5_pos_pub = rospy.Publisher('/pigot/joint5_position_controller/command', Float64, queue_size=10)
        joint6_pos_pub = rospy.Publisher('/pigot/joint6_position_controller/command', Float64, queue_size=10)
        joint7_pos_pub = rospy.Publisher('/pigot/joint7_position_controller/command', Float64, queue_size=10)
        joint8_pos_pub = rospy.Publisher('/pigot/joint8_position_controller/command', Float64, queue_size=10)
        joint9_pos_pub = rospy.Publisher('/pigot/joint9_position_controller/command', Float64, queue_size=10)
        joint10_pos_pub = rospy.Publisher('/pigot/joint10_position_controller/command', Float64, queue_size=10)
        joint11_pos_pub = rospy.Publisher('/pigot/joint11_position_controller/command', Float64, queue_size=10)
        joint12_pos_pub = rospy.Publisher('/pigot/joint12_position_controller/command', Float64, queue_size=10)
        while not rospy.is_shutdown():
            j = 0
            default_angle = [0, 0, 0]
            RPY_angle_data_old = rospy.get_param('/pigot/RPY_angle_old', default_angle)
            RPY_angle_data_new_traj = rospy.get_param('/pigot/RPY_angle_new', default_angle)

            print(RPY_angle_data_old)
            print(RPY_angle_data_new_traj)
            if_traj_plan = False
            error = np.linalg.norm(np.array(RPY_angle_data_new_traj))
            print(error)
            if (error>0.05):
                if if_traj_plan:
                    rate, cycle_gait_np_data, RPY_B_traj = rpy.rpy_gait(RPY_angle_data_old, RPY_angle_data_new_traj)
                    data_length = cycle_gait_np_data.shape[0]
                    pause = rospy.Rate(data_length * rate)
                    cycle_gait_data.data = cycle_gait_np_data
                    while (j<1):
                        for i in range(data_length):
                            joint1_pos_pub.publish(cycle_gait_data.data[i, 0])
                            joint2_pos_pub.publish(cycle_gait_data.data[i, 1])
                            joint3_pos_pub.publish(cycle_gait_data.data[i, 2])
                            joint4_pos_pub.publish(cycle_gait_data.data[i, 3])
                            joint5_pos_pub.publish(cycle_gait_data.data[i, 4])
                            joint6_pos_pub.publish(cycle_gait_data.data[i, 5])
                            joint7_pos_pub.publish(cycle_gait_data.data[i, 6])
                            joint8_pos_pub.publish(cycle_gait_data.data[i, 7])
                            joint9_pos_pub.publish(cycle_gait_data.data[i, 8])
                            joint10_pos_pub.publish(cycle_gait_data.data[i, 9])
                            joint11_pos_pub.publish(cycle_gait_data.data[i, 10])
                            joint12_pos_pub.publish(cycle_gait_data.data[i, 11])
                            pause.sleep()
                        j = j + 1
                else:
                    rate, cycle_gait_np_data = rpy.rpy_adj(RPY_angle_data_new_traj)
                    data_length = cycle_gait_np_data.shape[0]
                    pause = rospy.Rate(data_length * rate)
                    cycle_gait_data.data = cycle_gait_np_data
                    print(cycle_gait_np_data)
                    
                    joint1_pos_pub.publish(cycle_gait_data.data[0, 0])
                    joint2_pos_pub.publish(cycle_gait_data.data[0, 1])
                    joint3_pos_pub.publish(cycle_gait_data.data[0, 2])
                    joint4_pos_pub.publish(cycle_gait_data.data[0, 3])
                    joint5_pos_pub.publish(cycle_gait_data.data[0, 4])
                    joint6_pos_pub.publish(cycle_gait_data.data[0, 5])
                    joint7_pos_pub.publish(cycle_gait_data.data[0, 6])
                    joint8_pos_pub.publish(cycle_gait_data.data[0, 7])
                    joint9_pos_pub.publish(cycle_gait_data.data[0, 8])
                    joint10_pos_pub.publish(cycle_gait_data.data[0, 9])
                    joint11_pos_pub.publish(cycle_gait_data.data[0, 10])
                    joint12_pos_pub.publish(cycle_gait_data.data[0, 11])
                    pause.sleep()
                
                
            else:
                pause = rospy.Rate(1)
                pause.sleep()
                
            rospy.set_param('/pigot/RPY_angle_old', RPY_angle_data_new_traj)
            rospy.set_param('/pigot/in_wait', True)
    except rospy.ROSInterruptException:
        pass