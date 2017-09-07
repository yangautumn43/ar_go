#!/usr/bin/env python

## Simple odom_sender that publishes gps_data (sensor_msgs/Imu) messages
## to the '/odom' topic that is subscribed to "robot_pose_ekf" node

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
import tf
import csv

def odom_sender():
    pub = rospy.Publisher('gps', Odometry, queue_size=10)
    rospy.init_node('odom_sender', anonymous=True)
    rate = rospy.Rate(50) # 10hz

    time_file = rospy.get_param("~time_file")
    with open(time_file, 'r') as f:
      time_list = [list(map(float,rec)) for rec in csv.reader(f, delimiter=',')]
    time_list = [e[0] for e in time_list]
    # print(time_list)
    print(len(time_list))

    gps_x = 0
    gps_y = 0
    gps_z = 0
    cov_x = 0.9
    cov_y = 0.9
    cov_z = 0.9   

    i = 0 
    while not rospy.is_shutdown():
        if i<len(time_list): 
            now = rospy.get_rostime()
            rospy.loginfo("Current time %i %i", now.secs, now.nsecs)
            msg = Odometry()
            msg.header.stamp = now                   
            msg.header.frame_id = "base_footprint"         
            msg.pose.pose.position.x = gps_x              
            msg.pose.pose.position.y = gps_y              
            msg.pose.pose.position.z = gps_z              
            msg.pose.pose.orientation.x = 1               
            msg.pose.pose.orientation.y = 0               
            msg.pose.pose.orientation.z = 0               
            msg.pose.pose.orientation.w = 0               
            msg.pose.covariance = [cov_x, 0, 0, 0, 0, 0,  
                                    0, cov_y, 0, 0, 0, 0, 
                                    0, 0, cov_z, 0, 0, 0, 
                                    0, 0, 0, 99999, 0, 0, 
                                    0, 0, 0, 0, 99999, 0, 
                                    0, 0, 0, 0, 0, 99999] 

            pub.publish(msg)
            i = i+1

        rate.sleep()

if __name__ == '__main__':
    try:
        odom_sender()
    except rospy.ROSInterruptException:
        pass
