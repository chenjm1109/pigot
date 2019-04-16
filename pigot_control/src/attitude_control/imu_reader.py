#!/usr/bin/env python
# license removed for brevity

import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64
import math

def imu_cb(imu_data):
    pause = rospy.Rate(1)

    # Read the quaternion of the robot IMU
    x = imu_data.orientation.x
    y = imu_data.orientation.y
    z = imu_data.orientation.z
    w = imu_data.orientation.w

    # Read the angular velocity of the robot IMU
    w_x = imu_data.angular_velocity.x
    w_y = imu_data.angular_velocity.y
    w_z = imu_data.angular_velocity.z

    # Read the linear acceleration of the robot IMU
    a_x = imu_data.linear_acceleration.x
    a_y = imu_data.linear_acceleration.y
    a_z = imu_data.linear_acceleration.z

    # Convert Quaternions to Euler-Angles
    rpy_angle = Float64
    r = math.atan2(2 * (w * x + y * z), 1 - 2 * (x**2 + y**2))
    p = math.asin(2 * (w * y - z * x))
    y = math.atan2(2 * (w * z + x * y), 1 - 2 * (y**2 + z**2))
    rpy_angle.data = r
    print(rpy_angle.data)

    # Publish the data
    
    ori_pub.publish(rpy_angle)

    pause.sleep()
    return

if __name__ == '__main__':
    rospy.init_node('imu_node', anonymous=True)
    ori_pub = rospy.Publisher('/pigot/ori_rpy', Float64, queue_size=10)
    rospy.Subscriber("/pigot/imu", Imu, imu_cb)
    rospy.spin()