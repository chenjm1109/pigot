#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
import numpy as np
import kinematics_algorithm as ka

cycle_gait_data = Float32MultiArray()
action_command = String()


if __name__ == '__main__':
    try:
        rospy.init_node('pos_pub_node', anonymous=True)
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
            action_command.data = rospy.get_param('action_state_param', 'k')
            if (action_command.data == 'w'):
                rate, cycle_gait_np_data = ka.forward_gait()
            elif (action_command.data == 's'):
                rate, cycle_gait_np_data = ka.backward_gait()
            elif (action_command.data == 'a'):
                rate, cycle_gait_np_data = ka.turnleft_gait()
            elif (action_command.data == 'd'):
                rate, cycle_gait_np_data = ka.turnright_gait()
            elif (action_command.data == 'j'):
                rate, cycle_gait_np_data = ka.jump_gait()
            elif (action_command.data == 'k'):
                rate, cycle_gait_np_data = ka.keep_gait()
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
    except rospy.ROSInterruptException:
        pass