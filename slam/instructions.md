# Instructions of installing SLAM packages

## Todos
    * what is ORB Vocabulary?
    * how to setup yaml file for the camera?


## ORB-SLAM
https://github.com/yangautumn/ORB_SLAM2

### Pangolin

We use Pangolin for visualization and user interface. Dowload and install instructions can be found at: https://github.com/stevenlovegrove/Pangolin.
One issue (Fix librealsense include path finding): https://github.com/stevenlovegrove/Pangolin/pull/190/commits/ce7ded2a0701609401b9f9df308d12540e6891a7


### Build ORB-SLAM2
```
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
```
The three libraries are used to solve the failure on "usleep not in the scopse" in System.cc, Tracking.cc, LocalMapping.cc, LoopClosing.cc


Some advise on the project slam: https://github.com/raulmur/ORB_SLAM2/issues/279 (How to do SLAM with RaspberryPi PiCam and IMU Sensor?)

**Now I successfully compiled Pangolin and ORB-SLAM2 and I try to run the examples**

### TUM Dataset

1. Download a sequence from http://vision.in.tum.de/data/datasets/rgbd-dataset/download and uncompress it.

2. Execute the following command. Change TUMX.yaml to TUM1.yaml,TUM2.yaml or TUM3.yaml for freiburg1, freiburg2 and freiburg3 sequences respectively. Change PATH_TO_SEQUENCE_FOLDERto the uncompressed sequence folder.
```
./Examples/Monocular/mono_tum Vocabulary/ORBvoc.txt Examples/Monocular/TUMX.yaml PATH_TO_SEQUENCE_FOLDER
```
One I used:
```
./Examples/Monocular/mono_tum Vocabulary/ORBvoc.txt Examples/Monocular/TUM1.yaml ~/Downloads/freiburg1_xyz 
```
