#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
import numpy as np


cycle_gait_data = Float32MultiArray()
action_command = String()
rpy_angle = Float32MultiArray()

rate = 1

if __name__ == '__main__':
    try:
        rospy.init_node('attitude_pub_node', anonymous=True)
        k = 0.2
        d0 = [0, 0, 0]
        d1 = [0, 0, k]
        d2 = [0, 0, -k]
        d3 = [k, 0, 0]
        d4 = [-k, 0, 0]
        d5 = [0, k, -k]
        d6 = [0, -k, k]
        d7 = [-k, k/ 2, 0]
        d8 = [k, -k/2, 0]
        d9 = [0, 0, 0]
        t = 0
        pause = rospy.Rate(rate)
        while not rospy.is_shutdown():
            if t%10 == 0:
                rospy.set_param('stewart/RPY_angle_new', d0)
            elif t%10 == 1:
                rospy.set_param('stewart/RPY_angle_new', d1)
            elif t%10 == 2:
                rospy.set_param('stewart/RPY_angle_new', d2)
            elif t%10 == 3:
                rospy.set_param('stewart/RPY_angle_new', d3)
            elif t%10 == 4:
                rospy.set_param('stewart/RPY_angle_new', d4)
            elif t%10 == 5:
                rospy.set_param('stewart/RPY_angle_new', d5)
            elif t%10 == 6:
                rospy.set_param('stewart/RPY_angle_new', d6)
            elif t%10 == 7:
                rospy.set_param('stewart/RPY_angle_new', d7)
            elif t%10 == 8:
                rospy.set_param('stewart/RPY_angle_new', d8)
            elif t%10 == 9:
                rospy.set_param('stewart/RPY_angle_new', d9)
            t = t + 1
            pause.sleep()
    except rospy.ROSInterruptException:
        pass