#!/usr/bin/env python

"""
Yang Li
hw2 of Advanced Robotics
"""

import rospy
from std_msgs.msg import Header
import std_msgs

def talker():
    pub = rospy.Publisher('chatter', Header, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(100) # 10hz
    while not rospy.is_shutdown():
        # hello_str = "hello world %s" % rospy.get_time()
        s_time = std_msgs.msg.Header()
        s_time.stamp = rospy.Time.now()
        # print type(s_time)
        rospy.loginfo(s_time)
        pub.publish(s_time)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
