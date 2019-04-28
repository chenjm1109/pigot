#!/usr/bin/env python
# -*- coding: utf-8 -*
 
import  os
import  sys
import  tty, termios
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Float64

 
# 全局变量
pub_action = rospy.Publisher('/pigot/action_chatter', String, queue_size=10)
action_msgs = String()
 
def keyboardLoop():
    #初始化
    rospy.init_node('smartcar_teleop')
    rate = rospy.Rate(1)
  
    #显示提示信息
    print("Reading from keyboard")
    print("Use WASD keys to control the robot")
    print("Press Caps to move faster")
    print("Press q to quit")
 
    #读取按键循环
    while not rospy.is_shutdown():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
		#不产生回显效果
        old_settings[3] = old_settings[3] & ~termios.ICANON & ~termios.ECHO
        try :
            tty.setraw( fd )
            ch = sys.stdin.read( 1 )
        finally :
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
 
        if (ch == 'p'):
          exit()
        else:
          action_msgs.data = ch
          pub_action.publish(action_msgs)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        keyboardLoop()
    except rospy.ROSInterruptException:
        pass
