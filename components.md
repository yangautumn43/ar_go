# Components of the autonomous car

## Camera
oCam-iMGN-U by www.withrobot.com

- 1MP USB 3.0 Mono Camera
- Global shutter
- High speed up to 160 frames-per-second at the 320 x 240 resolution
- UVC compliance

### How to run
https://github.com/withrobot/oCam/tree/master/Software/oCam_viewer_Linux

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

*Before installing libuvc_ros, we should install libuvc first.* as talked in http://answers.ros.org/question/204840/libuvc_ros-not-building
libuvc is a library that supports enumeration, control and streaming for USB Video Class (UVC) devices, such as consumer webcams.
```bash
$ git clone https://github.com/ktossell/libuvc.git
$ cd libuvc
$ mkdir build
$ cd build
$ cmake -DCMAKE_BUILD_TYPE=Release ..
$ make && make install
```

*Install libuvc_ros*
Download the souce code from https://github.com/ktossell/libuvc_ros to your ROS workspace and build it.
The documentation is in http://wiki.ros.org/libuvc_camera

## IR sensors
SHARP 68 2Y0A710 F



## IMU
```bash
TODO
```
