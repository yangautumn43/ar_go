#!/usr/bin/env python

## Simple odom_listener that publishes imu_data (sensor_msgs/Imu) messages
## to the '/imu_data' topic that is subscribed to "robot_pose_ekf" node

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseWithCovarianceStamped
import tf
import csv

def odomCallBack(odom):
    quaternion = [odom.pose.pose.orientation.x, odom.pose.pose.orientation.y, 
    odom.pose.pose.orientation.z, odom.pose.pose.orientation.w]
    euler = tf.transformations.euler_from_quaternion(quaternion)
    print(euler)
    myfile = open(filename, 'a') 
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(euler)


def odom_listener():
    rospy.Subscriber('robot_pose_ekf/odom_combined', PoseWithCovarianceStamped, odomCallBack)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('odom_listener', anonymous=True)
    filename = rospy.get_param("~output_file")
    open(filename, 'w').close()
    print(filename)
    try:
        odom_listener()
    except rospy.ROSInterruptException:
        pass
