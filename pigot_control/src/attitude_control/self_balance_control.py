#!/usr/bin/env python
# license removed for brevity
'''
Subscribe to the '/pigot/imu' topic, convert it to Euler-Angle, 
and then transmit the control signal (the inverse of Euler-Angle) 
to the kinematics algorithm.

Created on Tue Apr 9 20:00:00 2019
author: JimCHAN
email: 522706601@qq.com
'''
import rospy
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import Imu
import math

rate = 1 # Set the frequency of detecting and converting IMU signals.

def sbc_cb(data):
    if rospy.get_param('/pigot/in_wait', True):
        # Read the quaternion parameters of the robot IMU
        x = data.orientation.x
        y = data.orientation.y
        z = data.orientation.z
        w = data.orientation.w

        # Read the quaternion parameters of the ground IMU
        ground_rpy_angle = [0, 0, 0]
        
        # Convert the quaternion to Euler-Angle. Ref: https://blog.csdn.net/xiaoma_bk/article/details/79082629
        # Take the negative number to adjust the orientation.
        rpy_angle = [0, 0, 0]
        rpy_angle[1] = -math.atan2(2 * (w * x + y * z), 1 - 2 * (x**2 + y**2))
        rpy_angle[0] = -math.asin(2 * (w * y - z * x))
        rpy_angle[2] = -math.atan2(2 * (w * z + x * y), 1 - 2 * (y**2 + z**2))

        rospy.set_param('/pigot/RPY_angle_new', rpy_angle)
        rospy.set_param('/pigot/in_wait', False)
    return

if __name__ == '__main__':
    try:
        rospy.init_node('sbc_node', anonymous=True)
        pause = rospy.Rate(rate)
        while not rospy.is_shutdown():
            rospy.Subscriber("/pigot/imu", Imu, sbc_cb)
            pause.sleep()
    except rospy.ROSInterruptException:
        pass