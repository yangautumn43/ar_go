# Components of the Autonomous Car

## Contents
1. [Chasis](#chasis)
2. [ODroid - running Ubuntu 16.04 MATE](#odroid-xu4)
3. [Wifi module - plug and play](#wifi-module)
4. [Camera - oCam](#camera---yang-li)
5. [IR sensor - SHARP](#ir-sensors---radhen)
6. [IMU](#imu---jay)
7. [Servo controller](#servo-controller---radhen)
8. [Electronic speed control (ESC)](#electronic-speed-control-esc)
9. [Buck converter](#buck-converter)
10. [Visual-inertial SLAM](#visual-inertial-slam---yang-li)


## Chasis

[1/10 AMP MT 2WD Monster Truck RTR ECX03028T2](http://www.horizonhobby.com/product/cars-and-trucks/cars-and-trucks-14524--1/electric-cars-and-trucks/1-10-amp-mt-2wd-monster-truck-rtr--black-green-p-ecx03028t2)



## ODROID-XU4

**Running Ubuntu 16.04 MATE**

### Odroid Setup

You now have an [ODROID-XU4](http://odroid.com/dokuwiki/doku.php?id=en:odroid-xu4), which is a small, yet powerful, processing board that can run GUN/Linux and ROS. We have already configured it with ROS and Ubuntu. You can use the monitors and keyboards in the lab to connect to it and do initial configuration (e.g. connecting to the lab wifi, figuring out the IP address, setting a new password, etc), but once you have it configured you will not need to use a monitor. Instead, you should use ssh to connect to it from your computer (and commands like scp to copy code) and launch ros nodes from the command line. Your first task is to move all of your code over to the Odroid and test your Lab 2 code.

**Question**: Describe the setup process and any challenges you encountered.

ROS nodes running on different computers can communicate with each other. In this section you should configure your Odroid and computer to communicate with each other. Read the tutorial on this at http://wiki.ros.org/ROS/Tutorials/MultipleMachines for details. You should also read the networking troubleshooting guide at http://wiki.ros.org/ROS/NetworkSetup as you will need to do some network setup to make this work right. To summarize the first step (2.3 in the NetworkSetup) is to add an entry in the ```/etc/hosts``` on your machine and the Odroid to allow them to resolve the IP addresses against the hostname of the machines. You can then start the roscore on the Odroid1 and tell your computer where that core resides with the command ```export ROS_MASTER_URI=http://odroid:11311```, where *odriod* is the hostname of your Odriod.

Once this is configured you can launch some rosnodes on the Odroid and others on your computer and they will be able to communicate with each other. This is advantageous as you can run the nodes that you are not changing on the Odroid and the ones that you are changing on your own laptop (to allow easier editing and faster compiling). This is also good since you can run the vision processing code on the Odroid to prevent sending all of the images across the network, which can cause significant slowdowns.

**Question**: Describe the setup process for getting ROS to run on both your Odroid and your laptop. Write two nodes that communicate with each other to determine the network latency. To do this you can have node A send a message with a header time and then have node B just echo that message back to node A. Record the length of time that it takes for the message to do the round trip. Try changing the amount of data transmitted in the message (e.g. add an array or image that you transmit) to see how this impacts the latency. Compare this when running the nodes on a single machine versus across the network.

Some important reminders regarding your Odroid:
1. When you are switching batteries, you can plug the Odroid into the wall power in addition to providing power from the battery. Do not leave both connected for any significant amount of time.
2. Make sure to issue the ```sudo shutdown``` command before disconnecting power from the Odroid. If you do not, you may corrupt the file system or you may not be able to log in properly.
3. You should set the password on your Odroid account to something your group knows and not just the default password as this could cause confusion among groups.
4. You should primarily be connected to the lab wifi, which is not connected to the internet. You can connect to unl-air to update software, but you will not be able to easily set the ROS master node to another computer while on unl-air.
5. If you have trouble getting your computer running ROS to talk with the Odroid be sure to double check the IP addresses and hostnames in ```/etc/hosts``` on both computers.

refrence to: http://cse.unl.edu/~carrick/courses/2015/439/lab3/lab3.html

## Wifi module

```
plug and play. Nothing special.
```

## Camera - Yang Li
oCam-iMGN-U by www.withrobot.com

- 1MP USB 3.0 Mono Camera
- Global shutter
- High speed up to 160 frames-per-second at the 320 x 240 resolution
- UVC compliance

### How to run oCam-viewer
Use [oCam_viewer_Linux](https://github.com/withrobot/oCam/tree/master/Software/oCam_viewer_Linux)

build it and then
```bash
$ cd OCAM_VIEWER_BUILD_DIRECTORY
$ ./oCam-viewer
```
### How to get image?

USB --> Kernel (through xhci and V4L2) --> User Space (ROS)

```bash
ls /dev/video0
```
make sure the camera is connected correctly

```bash
sudo apt-get update
sudo apt-get install guvcview
```
install camera view application guvcview. Run it and you should be able to see the image catched by your camera.

Get started with the following launch file. If you need assistance with your webcam's supported resolutions and frame rates, try:
```bash
v4l2-ctl --list-formats-ext
```
Installing "V4l2-ctl" on Ubuntu

Here's how to install "V4l2-ctl" on Ubuntu Linux operating system:
```
sudo apt-get install v4l-utils
```


### METHOD 1: Use the oCam library (This is the way we use on ODROID)
#### 1. Use [ocam_publisher](https://github.com/yangautumn/ar_go_ws/tree/master/src/ocam_publisher) to read and publish image
By using the library they provides us in [Examples/opencv-basic_1MGN](https://github.com/withrobot/oCam/tree/master/Examples/opencv-basic_1MGN),
I wrote the [ocam_publisher](https://github.com/yangautumn/ar_go_ws/tree/master/src/ocam_publisher) ROS node to publish the image read from oCam to a ROS topic ```/camera/image```.
    
#### 2. Run Steve's [simple_opencv](https://github.com/AdvancedRoboticsCUBoulder/simple_opencv) node
With it, we get the image from camera/image topic, and apply some OpenCV functions to the image.

There is also tutorial about publishing and subscribing images on http://wiki.ros.org/image_transport/Tutorials    

#### 3. Set the udev rules

Copy the udev rules from ```libuvc_camera/53-uvc.rules``` in [libuvc_ros](https://github.com/AdvancedRoboticsCUBoulder/libuvc_ros) to ```/etc/udev/rules.d```, then run:
``` 
udevadm control -R
```

as root to reload the hotplug rules. Your camera should be detected as /dev/video[0-9]

### METHOD 2: Use libuvc_ros package

**This should be the common method, but I can't get image when I run the package.**

Use the updated version mentioned in the libuvc_camera folder of [libuvc_ros](https://github.com/AdvancedRoboticsCUBoulder/libuvc_ros). **Read the readme file to set permission rule to the camera.**

As mentioned in http://answers.ros.org/question/204840/libuvc_ros-not-building,
libuvc is a library that supports enumeration, control and streaming for USB Video Class (UVC) devices, such as consumer webcams.

```bash
$ git clone https://github.com/ktossell/libuvc.git
$ cd libuvc
$ mkdir build
$ cd build
$ cmake ..
$ make && sudo make install
```

#### Install libuvc_ros

Download the souce code from [libuvc_ros](https://github.com/ktossell/libuvc_ros) to your ROS workspace and build it.

The documentation is in http://wiki.ros.org/libuvc_camera

```bash
lsusb
Bus 003 Device 002: ID 04b4:00f8 Cypress Semiconductor Corp.
```
To get the vendor and product IDs
```bash
lsusb -d 04b4:00f8 -v

Bus 003 Device 002: ID 04b4:00f8 Cypress Semiconductor Corp.
Couldn't open device, some information will be missing
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               2.00
  bDeviceClass          239 Miscellaneous Device
  bDeviceSubClass         2 ?
  bDeviceProtocol         1 Interface Association
  bMaxPacketSize0        64
  idVendor           0x04b4 Cypress Semiconductor Corp.
  idProduct          0x00f8
  bcdDevice           16.11
...
```

```bash
roslaunch libuvc_camera libuvc.launch
```

```xml
<launch>
  <arg name="debug" default="false"/>
  <arg name="launch_prefix" if="$(arg debug)" default="gdb -e run --args"/>
  <arg name="launch_prefix" unless="$(arg debug)" default=""/>
  <!-- output="screen" -->
  <group ns="camera">
    <node pkg="libuvc_camera" type="camera_node" name="ocam" output="screen" launch-prefix="$(arg launch_prefix)">
      <!-- Parameters used to find the camera -->
      <param name="vendor" value="0x04b4"/>
      <param name="product" value="0x00f8"/>
      <param name="serial" value=""/>
      <!-- If the above parameters aren't unique, choose the first match: -->
      <param name="index" value="0"/>

      <!-- Image size and type -->
      <param name="width" value="640"/>
      <param name="height" value="480"/>
      <!-- choose whichever uncompressed format the camera supports: -->
      <param name="video_mode" value="gray8"/> <!-- or yuyv/nv12/jpeg -->
      <param name="frame_rate" value="80"/>

      <param name="timestamp_method" value="start"/> <!-- start of frame -->
      <!-- <param name="camera_info_url" value="file:///tmp/cam.yaml"/> -->

<!--       <param name="auto_exposure" value="3"/> use aperture_priority auto exposure
      <param name="auto_white_balance" value="false"/> -->
    </node>
  </group>
</launch>
```

**Topics got from running the libuvc_camera**
```bash
yang@colab:~$ rostopic list
/camera/camera_info
/camera/image_raw
/camera/image_raw/compressed
/camera/image_raw/compressed/parameter_descriptions
/camera/image_raw/compressed/parameter_updates
/camera/image_raw/compressedDepth
/camera/image_raw/compressedDepth/parameter_descriptions
/camera/image_raw/compressedDepth/parameter_updates
/camera/image_raw/theora
/camera/image_raw/theora/parameter_descriptions
/camera/image_raw/theora/parameter_updates
/camera/ocam/parameter_descriptions
/camera/ocam/parameter_updates
/rosout
/rosout_agg
```

**Results from running the launch file**
```bash
yang@colab:~$ roslaunch libuvc_camera libuvc.launch
... logging to /home/yang/.ros/log/d49538ee-10d9-11e7-9400-d43d7eb70ebb/roslaunch-colab-15588.log
Checking log directory for disk usage. This may take awhile.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://localhost:44780/

SUMMARY
========

PARAMETERS
 * /camera/ocam/frame_rate: 80
 * /camera/ocam/height: 480
 * /camera/ocam/index: 0
 * /camera/ocam/product: 0x00f8
 * /camera/ocam/serial:
 * /camera/ocam/timestamp_method: start
 * /camera/ocam/vendor: 0x04b4
 * /camera/ocam/video_mode: gray8
 * /camera/ocam/width: 640
 * /rosdistro: kinetic
 * /rosversion: 1.12.6


NODES
  /camera/
    ocam (libuvc_camera/camera_node)

auto-starting new master
process[master]: started with pid [15599]
ROS_MASTER_URI=http://localhost:11311

setting /run_id to d49538ee-10d9-11e7-9400-d43d7eb70ebb
process[rosout-1]: started with pid [15612]
started core service [/rosout]
log4cxx: Could not read configuration file [~/rosconsole.config].
process[camera/ocam-2]: started with pid [15629]
log4cxx: Could not read configuration file [~/rosconsole.config].
 INFO ros.libuvc_camera: Opening camera with vendor=0x4b4, product=0xf8, serial="", index=0
unsupported descriptor subtype: 13
 WARN ros.libuvc_camera: Unable to set auto_exposure to 8
 WARN ros.libuvc_camera: Unable to set auto_exposure_priority to 0
 WARN ros.libuvc_camera: Unable to set auto_focus to 1
 WARN ros.libuvc_camera: Unable to set focus_absolute to 0
 WARN ros.libuvc_camera: Unable to set gain to 0
 WARN ros.libuvc_camera: Unable to set iris_absolute to 0
 WARN ros.libuvc_camera: Unable to set pantilt to 0, 0
```

## IR sensors - Radhen
SHARP 68 2Y0A710 F

Driver for SharpIR sensor.
https://github.com/guillaume-rico/SharpIR

Pin layout/product manual
file:///Users/macbookpro15/Downloads/SharpGP2Y0A710K0F_Manual.pdf


## IMU - Jay
```bash
TODO
```

## Servo controller - Radhen
Initial setup:
Install Linux driver and control center for Pololu Maestro board
https://www.pololu.com/docs/0J40/3.b

Pololu Maestro Servo Controller User’s Guide
https://www.pololu.com/docs/0J40

Servo Controller programming:
ros_pololu_servo package for servo control via USB
https://github.com/geni-lab/ros_pololu_servo

PID controller
http://wiki.ros.org/pid


## Electronic speed control (ESC)

(From wikipedia) An electronic speed control or ESC is an electronic circuit with the purpose to vary an electric motor's speed, its direction and possibly also to act as a dynamic brake. ESCs are often used on electrically powered radio controlled models, with the variety most often used for brushless motors essentially providing an electronically generated three-phase electric power low voltage source of energy for the motor.

PWM (Pulse Width Modulation / High rate control): The control of motor speed is obtained by switching the power to the motor on and off in various ratios e.g. maximum throttle is permanently on, half throttle is on half time, off half time etc. This switching on and off is done many times a second. The speed at which the switching takes place has a large effect on overall efficiency. Early speed controls used what is known as "frame rate" switching, which means that they switched approximately 50 times a second, the same rate as frames of information are delivered over the radio. Most modern ESCs switch at a much higher rate which makes them much more efficient i.e. they lose less power as heat in the controller. Switching rates around 3000 Hz (times a second) are about optimum. Anywhere between 1000 Hz and 5000Hz is acceptable.

## Buck converter

As I remembered: Input 5.6+ v --> Output 5.0 v

## Visual-inertial SLAM - Yang Li

### ORB-SLAM2
https://github.com/yangautumn/ORB_SLAM2

#### Pangolin

We use Pangolin for visualization and user interface. Dowload and install instructions can be found at: https://github.com/stevenlovegrove/Pangolin.
One issue (Fix librealsense include path finding): https://github.com/stevenlovegrove/Pangolin/pull/190/commits/ce7ded2a0701609401b9f9df308d12540e6891a7


#### Build ORB-SLAM2
```
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
```
The three libraries are used to solve the failure on "usleep not in the scopse" in System.cc, Tracking.cc, LocalMapping.cc, LoopClosing.cc


Some advise on the project slam: https://github.com/raulmur/ORB_SLAM2/issues/279 (How to do SLAM with RaspberryPi PiCam and IMU Sensor?)

**Now I successfully compiled Pangolin and ORB-SLAM2 and I try to run the examples**

#### TUM Dataset

1. Download a sequence from http://vision.in.tum.de/data/datasets/rgbd-dataset/download and uncompress it.

2. Execute the following command. Change TUMX.yaml to TUM1.yaml,TUM2.yaml or TUM3.yaml for freiburg1, freiburg2 and freiburg3 sequences respectively. Change PATH_TO_SEQUENCE_FOLDERto the uncompressed sequence folder.
```
./Examples/Monocular/mono_tum Vocabulary/ORBvoc.txt Examples/Monocular/TUMX.yaml PATH_TO_SEQUENCE_FOLDER
```
One I used:
```
./Examples/Monocular/mono_tum Vocabulary/ORBvoc.txt Examples/Monocular/TUM1.yaml ~/Downloads/freiburg1_xyz 
```
#### Building the nodes for mono, monoAR, stereo and RGB-D

Add the path including `Examples/ROS/ORB_SLAM2` to the `ROS_PACKAGE_PATH` environment variable. Open `.bashrc` file and add at the end the following line. Replace `PATH` by the folder where you cloned ORB_SLAM2:
```
export ROS_PACKAGE_PATH=${ROS_PACKAGE_PATH}:PATH/ORB_SLAM2/Examples/ROS
```
Execute `build_ros.sh` script:
```
chmod +x build_ros.sh
./build_ros.sh
```
#### Running Monocular Node

For a monocular input from topic `/camera/image_raw` run node `ORB_SLAM2/Mono`. You will need to provide the vocabulary file and a settings file. See the monocular examples above.

```
rosrun ORB_SLAM2 Mono PATH_TO_VOCABULARY PATH_TO_SETTINGS_FILE
```

My command is 
```
rosrun ORB_SLAM2 Mono Vocabulary/ORBvoc.txt Examples/Monocular/ocam.yaml
```
The following is copied from `Examples/Monocular/TUM1.yaml`, we need to configure our YAML file for our oCam.
```YAML
  1 %YAML:1.0                                                                                                               
  2 
  3 #--------------------------------------------------------------------------------------------
  4 # Camera Parameters. Adjust them!
  5 #--------------------------------------------------------------------------------------------
  6 
  7 # Camera calibration and distortion parameters (OpenCV) 
  8 Camera.fx: 517.306408
  9 Camera.fy: 516.469215
 10 Camera.cx: 318.643040
 11 Camera.cy: 255.313989
 12 
 13 Camera.k1: 0.262383
 14 Camera.k2: -0.953104
 15 Camera.p1: -0.005358
 16 Camera.p2: 0.002628
 17 Camera.k3: 1.163314
 18 
 19 # Camera frames per second 
 20 Camera.fps: 30.0
 21 
 22 # Color order of the images (0: BGR, 1: RGB. It is ignored if images are grayscale)
 23 Camera.RGB: 1
 24 
 25 #--------------------------------------------------------------------------------------------
 26 # ORB Parameters
 27 #--------------------------------------------------------------------------------------------
 28 
 29 # ORB Extractor: Number of features per image
 30 ORBextractor.nFeatures: 1000
 31 
 32 # ORB Extractor: Scale factor between levels in the scale pyramid   
 33 ORBextractor.scaleFactor: 1.2
 34 
 35 # ORB Extractor: Number of levels in the scale pyramid  
 36 ORBextractor.nLevels: 8
 37 
 38 # ORB Extractor: Fast threshold
 39 # Image is divided in a grid. At each cell FAST are extracted imposing a minimum response.
 40 # Firstly we impose iniThFAST. If no corners are detected we impose a lower value minThFAST
 41 # You can lower these values if your images have low contrast           
 42 ORBextractor.iniThFAST: 20
 43 ORBextractor.minThFAST: 7
 44 
 45 #--------------------------------------------------------------------------------------------
 46 # Viewer Parameters
 47 #--------------------------------------------------------------------------------------------
 48 Viewer.KeyFrameSize: 0.05
 49 Viewer.KeyFrameLineWidth: 1
 50 Viewer.GraphLineWidth: 0.9
 51 Viewer.PointSize:2
 52 Viewer.CameraSize: 0.08
 53 Viewer.CameraLineWidth: 3
 54 Viewer.ViewpointX: 0
 55 Viewer.ViewpointY: -0.7
 56 Viewer.ViewpointZ: -1.8
 57 Viewer.ViewpointF: 500
```

### Camera calibration - oCam
#### Calibration using OpenCV
(not important now) First, [Install OpenCV 3.0 and Python 3.4+ on Ubuntu 14.04](http://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/)

Then follow the [tutorial on Camera calibration With OpenCV](http://docs.opencv.org/3.1.0/d4/d94/tutorial_camera_calibration.html)

**How to compile the camera_calibration.cpp file (It doesn't like monocular camera)**
Use mine as example: find the `example_cmake` folder in your opencv source file: `/home/yang/opencv/samples/cpp/example_cmake`, copy, modify and compile it.

#### Calibration using ROS packages
**Try procedure: libuvc_camera --> camera_calibration (--> orb-slam2)**
Now `libuvc_camera` is working with the newly rebuild `libuvc` 
When I run the node, I got a warning:
```
WARN ros.camera_info_manager: Camera calibration file /home/yang/.ros/camera_info/camera.yaml not found.
```
(the `camera.yaml` file is used to store the calibration data after running `camera_calibration` node)
What I did is trying to follow the instructions in [How to Calibrate a Monocular Camera](http://wiki.ros.org/camera_calibration/Tutorials/MonocularCalibration)
 
And also check [wiki](http://wiki.ros.org/camera_calibration) for camera calibration, [theory](Camera Calibration and 3D Reconstruction) of camera camlibration.

In the termminal running `libuvc_camera`, I got the following information:
```
INFO ros.camera_info_manager: writing calibration data to /home/yang/.ros/camera_info/camera.yaml
```
Following is the content of `camera.yaml`
```yaml
image_width: 640
image_height: 480
camera_name: camera
camera_matrix:
  rows: 3
  cols: 3
  data: [977.6634949347863, 0, 345.7413814757732, 0, 976.9311317181429, 242.6739767243544, 0, 0, 1]
distortion_model: plumb_bob
distortion_coefficients:
  rows: 1
  cols: 5
  data: [-0.4756923568249309, 0.3486987708884488, -0.0008574457582377547, -0.0003268831859127585, 0]
rectification_matrix:
  rows: 3
  cols: 3
  data: [1, 0, 0, 0, 1, 0, 0, 0, 1]
projection_matrix:
  rows: 3
  cols: 4
  data: [926.132568359375, 0, 348.411146231374, 0, 0, 948.2742919921875, 242.6637827664636, 0, 0, 0, 1, 0]
```
Lesson learned (just intuitive):
1. nFeatures should be larger
```
# ORB Extractor: Number of features per image
ORBextractor.nFeatures: 1500
```
2. Environment light should be good (maybe we can also ajust the exposure para of the camera?)

