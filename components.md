# Components of the autonomous car

## Camera
oCam-iMGN-U by www.withrobot.com

- 1MP USB 3.0 Mono Camera
- Global shutter
- High speed up to 160 frames-per-second at the 320 x 240 resolution
- UVC compliance

### How to run
https://github.com/withrobot/oCam/tree/master/Software/oCam_viewer_Linux

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

**Before installing libuvc_ros, we should install libuvc first.**

As talked in http://answers.ros.org/question/204840/libuvc_ros-not-building
libuvc is a library that supports enumeration, control and streaming for USB Video Class (UVC) devices, such as consumer webcams.

```bash
$ git clone https://github.com/ktossell/libuvc.git
$ cd libuvc
$ mkdir build
$ cd build
$ cmake -DCMAKE_BUILD_TYPE=Release ..
$ make && make install
```

**Install libuvc_ros**

Download the souce code from https://github.com/ktossell/libuvc_ros to your ROS workspace and build it.

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

**uvcdynctrl**

libwebcam command line tool

```bash
roslaunch libuvc_camera libuvc.launch 
```

```xml
<launch>
  <group ns="camera">
    <node pkg="libuvc_camera" type="camera_node" name="ocam" output="screen">
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
      <param name="video_mode" value="uncompressed"/> <!-- or yuyv/nv12/jpeg -->
      <param name="frame_rate" value="80"/>

      <param name="timestamp_method" value="start"/> <!-- start of frame -->
      <!-- <param name="camera_info_url" value="file:///tmp/cam.yaml"/> -->

      <param name="auto_exposure" value="3"/> <!-- use aperture_priority auto exposure -->
      <param name="auto_white_balance" value="false"/>
    </node>
  </group>
</launch>
```

## IR sensors
SHARP 68 2Y0A710 F

Two ground and 5V are needed.


## IMU
```bash
TODO
```
