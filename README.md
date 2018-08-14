# ar_go
    Autonomous vehicle project repo of Advanced Robotics
    Team members: Yang, Radhen, Jay, Ao and Yueming

Please get your tasks and update your progress on the project in the **Progress** section

    * Setup regular meeting schedule for the rest of the time
    * Report your recent progress
    * Share ideas

## To Talk
### Current status of IMU [Jay]
    * Can you publish imu message

### Current status of Motor and Servo controller [Radhen]
    * What is in the pid-control folder
    * Smoothly

### Current status of IR sensors [Radhen]
    * What should we do with the out-range measurements

### Current status of Camera [Yang] 
    * Use 'libuvc_camera' to publish camera image and info
    * Use the 'camera_calibration' package to calibrate our lens-fixed fisheye camera
    
### Current status of SLAM [Yang & Jay]
    * We now use 'orb-slam2' to do visual slam
    * Need to publish to '/VO' topic
    
### Current status of Stop-sign detector [Ao]
    * Image delay when I try it
    * No worry about distance

### Current status of Ball detector [Yueming & Ao]
    * How to detect the ball -- blob detector?


## Progress
    Format:
       * Name
       * What you have done
       * What you are doing
       * Some of your ideas

### Yang
* [x] Done with the camera ROS node (now we switch back to `libuvc_camera`)
* [x] Done with the camera calibration
* [x] Get ORB-SLAM2 working with oCam
* Working on visual-inertial SLAM
* [x] Need to let orb-slam publish data to topic `/vo` (visual odometry)
* Need to get robot-pose-ekf sub to `/vo` and `/imu` and publish to `/odom_combined`
* Test loop closure of ORB-SLAM2


### Radhen
* [x] Got ros_pololu_servo package working for steering
* [x] Wrote PID controller for steering
* Need to set the gains for real run to drive in straight line
* Plan to integrate thrust motor with the ros_pololu_servo package
* Need to write code to take right angle turns 

### Jay
* [x] Got IMU to publish at IMU topic
* [x] Tested IR sensors on arduino
* [x] Tested Buck converter
* [x] ORB-SLAM2 successfully running on odroid
* How to identify a drivable area
* Controller design using feedback from camera
 

### Ao
* Working on stop-sign detection
    - be able to detect the stop-sign but still need the distance informance
* Working on rolling ball detection

### Yueming
* Working on rolling ball detection


## Competition description

### The challenges we choose:
* Stop in front of stop-sign
* Avoid a rolling ball
* Visual inertial SLAM

Below is the brief description of the competition:

![competition description][pics/competition_description.JPG]



Note since the second meeting (April 7, 2017):
![second meeting note][meeting-2]

ROS topics that are needed for the project [parts]:
![ros topics][ros-topics]

Note of the first meeting:
![first meeting note][meeting-1]





[comp-describ]:pics/competition_description.JPG
[meeting-1]:pics/first_meeting_framework.JPG
[ros-topics]:pics/ros_topics_needed_[part].JPG
[meeting-2]:pics/meeting_April_7.JPG
