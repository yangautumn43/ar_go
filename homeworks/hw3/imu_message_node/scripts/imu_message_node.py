#!/usr/bin/env python

## Simple imu_sender that publishes imu_data (sensor_msgs/Imu) messages
## to the '/imu_data' topic that is subscribed to "robot_pose_ekf" node

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
import tf
import csv
import math

def rpq2euler(gyro, euler):
    tmp = [0, 0, 0]
    tmp[0] = euler[0] + (gyro[1] + gyro[2]*math.sin(euler[0])*math.tan(euler[1]) + 
        gyro[0]*math.cos(euler[0])*math.tan(euler[1]))*0.005
    tmp[1] = euler[1] + (gyro[2]*math.cos(euler[0]) - gyro[0]*math.sin(euler[1]))*0.005
    tmp[2] = euler[2] + (gyro[2]*math.sin(euler[0])/math.cos(euler[1]) + 
        gyro[0]*math.cos(euler[0])/math.cos(euler[1]))*0.005
    return tmp



def imu_sender():
    pub = rospy.Publisher('imu_data', Imu, queue_size=10)
    pub_odom = rospy.Publisher('gps', Odometry, queue_size=10)
    rospy.init_node('imu_sender', anonymous=True)
    rate = rospy.Rate(35) # 10hz

    # read in time stamps and imu sensor measurements

    gyro_file = rospy.get_param("~gyro_file")
    with open(gyro_file, 'r') as f:
      gyro_list = [list(map(float,rec)) for rec in csv.reader(f, delimiter=',')]

    # print(gyro_list)
    print(len(gyro_list))

    # fill in data and send the message
    i = 0
    cov = 10
    euler = [0, 0, 0]
    gps_x = 0
    gps_y = 0
    gps_z = 0
    step = 5
    l = len(gyro_list)
    while not rospy.is_shutdown():
        if i<l: 
            euler = rpq2euler(gyro_list[i], euler)
            quaternion = tf.transformations.quaternion_from_euler(euler[0], euler[1], euler[2])
            # rospy.Time.from_sec(float_secs)
            now = rospy.get_rostime()
            # rospy.loginfo("Current time %i %i", now.secs, now.nsecs)
            rospy.loginfo("Current index %i", i)
            msg = Imu()
            msg.header.frame_id = "base_footprint"
            msg.header.stamp = now

            msg.orientation.x = quaternion[0]
            msg.orientation.y = quaternion[1]
            msg.orientation.z = quaternion[2]
            msg.orientation.w = quaternion[3]
            msg.orientation_covariance = [cov, 0, 0,  # covariance on gps_x
                                            0, cov, 0,  # covariance on gps_y
                                            0, 0, cov]  # covariance on gps_z

            msg1 = Odometry()
            msg1.header.stamp = now                   
            msg1.header.frame_id = "base_footprint"         
            msg1.pose.pose.position.x = gps_x              
            msg1.pose.pose.position.y = gps_y              
            msg1.pose.pose.position.z = gps_z              
            msg1.pose.pose.orientation.x = 1               
            msg1.pose.pose.orientation.y = 0               
            msg1.pose.pose.orientation.z = 0               
            msg1.pose.pose.orientation.w = 0               
            msg1.pose.covariance = [cov, 0, 0, 0, 0, 0,  
                                    0, cov, 0, 0, 0, 0, 
                                    0, 0, cov, 0, 0, 0, 
                                    0, 0, 0, 99999, 0, 0, 
                                    0, 0, 0, 0, 99999, 0, 
                                    0, 0, 0, 0, 0, 99999] 

            pub_odom.publish(msg1)
            pub.publish(msg)
            i = i+step

        rate.sleep()

if __name__ == '__main__':
    try:
        imu_sender()
    except rospy.ROSInterruptException:
        pass
