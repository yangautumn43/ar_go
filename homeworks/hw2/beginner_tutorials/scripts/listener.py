#!/usr/bin/env python

"""
Yang Li
hw2 of Advanced Robotics
"""

import rospy
from std_msgs.msg import Header
import std_msgs
import matplotlib.pyplot as plt
import sys

def callback(data):
    r_time = rospy.Time.now()
    sec = r_time.secs
    nsec = r_time.nsecs

    if (len(times) < 300):
        t = (nsec - data.stamp.nsecs)/1e9
        if t>0:
            times.append(t)
    else:
        plt.hist(times, 25, facecolor='blue', alpha=0.75)
        plt.show()
        sys.exit(1)

    rospy.loginfo(rospy.get_caller_id() + 'I heard %s at time %s', data.stamp.nsecs, r_time.nsecs)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', Header, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    times = []
    listener()
