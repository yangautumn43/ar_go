#!/usr/bin/env python

"""
Yang Li
hw2 of Advanced Robotics
"""

import sys
import rospy
from beginner_tutorials.srv import *
import matplotlib.pyplot as plt

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)

        # get time before requesting
        t1 = rospy.Time.now()
        nsec1 = t1.nsecs

        resp1 = add_two_ints(x, y)

        # get time after requesting
        t2 = rospy.Time.now()
        nsec2 = t2.nsecs
        print (nsec2 - nsec1)
        return (nsec2 - nsec1)/1e9

    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    rospy.init_node('client', anonymous=True)

    times = []
    count = 0
    while count < 300:
        t = add_two_ints_client(23, 34)
        if (t>0):
            times.append( t )
            count += 1

    n, bins, patches = plt.hist(times, 25, facecolor='blue', alpha=0.75)
    # add a 'best fit' line
    # y = mlab.normpdf(bins, mu, sigma)
    # plt.plot(bins, y, 'r--')
    # plt.xlabel('Time slots')
    # plt.ylabel('Frequency')

    plt.show()
    