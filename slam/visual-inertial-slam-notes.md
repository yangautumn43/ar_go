# Visual inertial SLAM notes

## Open Sources
* [Awesome SLAM](https://github.com/kanster/awesome-slam/blob/master/README.md): Simultaneous Localization and Mapping, also known as SLAM, is the computational problem of constructing or updating a map of an unknown environment while simultaneously keeping track of an agent's location within it.
* [ORB-SLAM](https://github.com/yangautumn/ORB_SLAM)ORB-SLAM is a versatile and accurate Monocular SLAM solution able to compute in real-time the camera trajectory and a sparse 3D reconstruction of the scene in a wide variety of environments, ranging from small hand-held sequences to a car driven around several city blocks. It is able to close large loops and perform global relocalisation in real-time and from wide baselines. Check out the new [ORB-SLAM2](https://github.com/yangautumn/ORB_SLAM2)(Monocular, Stereo and RGB-D). See the [project webpage](http://webdiis.unizar.es/~raulmur/orbslam/). And [youtube](https://www.youtube.com/watch?v=ufvPS5wJAx0) for the exiting video.
* [LSD-SLAM](https://github.com/tum-vision/lsd_slam) is a novel, direct monocular SLAM technique: Instead of using keypoints, it directly operates on image intensities both for tracking and mapping. The camera is tracked using direct image alignment, while geometry is estimated in the form of semi-dense depth maps, obtained by filtering over many pixelwise stereo comparisons. We then build a Sim(3) pose-graph of keyframes, which allows to build scale-drift corrected, large-scale maps including loop-closures. LSD-SLAM runs in real-time on a CPU, and even on a modern smartphone. (LSD-SLAM: Large-Scale Direct Monocular SLAM)
* [OKVIS](https://github.com/yangautumn/okvis): Open Keyframe-based Visual-Inertial SLAM. This is the Author's implementation of the [1] and [3] with more results in [2].
    * [1] Stefan Leutenegger, Simon Lynen, Michael Bosse, Roland Siegwart and Paul Timothy Furgale. Keyframe-based visual–inertial odometry using nonlinear optimization. The International Journal of Robotics Research, 2015.
    * [2] Stefan Leutenegger. Unmanned Solar Airplanes: Design and Algorithms for Efficient and Robust Autonomous Operation. Doctoral dissertation, 2014.
    * [3] Stefan Leutenegger, Paul Timothy Furgale, Vincent Rabaud, Margarita Chli, Kurt Konolige, Roland Siegwart. Keyframe-Based Visual-Inertial SLAM using Nonlinear Optimization. In Proceedings of Robotics: Science and Systems, 2013.
    * Note that the codebase that you are provided here is free of charge and without any warranty. This is bleeding edge research software.
* [SVO](https://github.com/uzh-rpg/rpg_svo): This code implements a semi-direct monocular visual odometry pipeline. SVO has been tested under ROS Groovy, Hydro and Indigo with Ubuntu 12.04, 13.04 and 14.04. This is research code, any fitness for a particular purpose is disclaimed. [Video](http://youtu.be/2YnIMfw6bJY) [Paper](http://rpg.ifi.uzh.ch/docs/ICRA14_Forster.pdf) 




## Papers

### ORB-SLAM: A Versatile and Accurate Monocular SLAM System

#### Abstract

This paper presents ORB-SLAM, a feature-based
monocular simultaneous localization and mapping (SLAM) system
that operates in real time, in small and large indoor and outdoor
environments. The system is robust to severe motion clutter, allows
wide baseline loop closing and relocalization, and includes full automatic
initialization. Building on excellent algorithms of recent
years, we designed from scratch a novel system that uses the same
features for all SLAM tasks: tracking, mapping, relocalization, and
loop closing. A survival of the fittest strategy that selects the points
and keyframes of the reconstruction leads to excellent robustness
and generates a compact and trackable map that only grows if
the scene content changes, allowing lifelong operation. We present
an exhaustive evaluation in 27 sequences from the most popular
datasets. ORB-SLAM achieves unprecedented performance with
respect to other state-of-the-art monocular SLAM approaches. For
the benefit of the community, we make the source code public.

#### INTRODUCTION
BUNDLE adjustment (BA) is known to provide accurate estimates of camera localizations as well as a sparse geometrical reconstruction [1], [2], given that a strong network of matches and good initial guesses are provided. For a long time, this approach was considered unaffordable for real-time applications such as visual simultaneous localization and mapping (visual SLAM). Visual SLAM has the goal of estimating the camera trajectory while reconstructing the environment. Now, we know that to achieve accurate results at nonprohibitive computational cost, a real-time SLAM algorithm has to provide BA with the following.
1. Corresponding observations of scene features (map
points) among a subset of selected frames (keyframes).
2. As complexity grows with the number of keyframes, their
selection should avoid unnecessary redundancy.
3. A strong network configuration of keyframes and points
to produce accurate results, that is, a well spread set of
keyframes observing points with significant parallax and
with plenty of loop closure matches.
4. An initial estimation of the keyframe poses and point
locations for the nonlinear optimization.
5. A local map in exploration where optimization is focused
to achieve scalability.
6. The ability to perform fast global optimizations (e.g., pose
graph) to close loops in real time.

The first real-time application of BA was the visual odometry
work of Mouragon et al. [3], followed by the ground-breaking
SLAM work of Klein and Murray [4], known as parallel tracking and mapping (PTAM). This algorithm, while limited to
small-scale operation, provides simple but effective methods
for keyframe selection, feature matching, point triangulation,
camera localization for every frame, and relocalization after
tracking failure. Unfortunately, several factors severely limit its
application: lack of loop closing and adequate handling of occlusions, low invariance to viewpoint of the relocalization, and
the need of human intervention for map bootstrapping.
In this study, we build on the main ideas of PTAM, the place
recognition work of Galvez-L ´ opez and Tard ´ os [5], the scale- ´
aware loop closing of Strasdat et al. [6], and the use of covisibility information for large-scale operation [7], [8], to design
from scratch ORB-SLAM, i.e., a novel monocular SLAM system whose main contributions are as follows.
1. Use of the same features for all tasks: tracking, mapping,
relocalization, and loop closing. This makes our system
more efficient, simple, and reliable. We use ORB features
[9], which allow real-time performance without GPUs,
providing good invariance to changes in viewpoint and
illumination.
2. Real-time operation in large environments. Thanks to the
use of a covisibility graph, tracking and mapping are focused in a local covisible area, independent of global map
size.
3. Real-time loop closing based on the optimization of a pose
graph that we call the Essential Graph. It is built from
a spanning tree maintained by the system, loop closure
links, and strong edges from the covisibility graph.
4. Real-time camera relocalization with significant invariance to viewpoint and illumination. This allows recovery
from tracking failure and also enhances map reuse.
5. A new automatic and robust initialization procedure based
on model selection that permits to create an initial map of
planar and nonplanar scenes.
6. A survival of the fittest approach to map point and
keyframe selection that is generous in the spawning but
very restrictive in the culling. This policy improves tracking robustness and enhances lifelong operation because
redundant keyframes are discarded.

Pipeline of ORB-SLAM:
![Pipeline of ORB-SLAM][orb-slam]

### LSD-SLAM: Large-Scale Direct Monocular SLAM
#### Abstract
We propose a direct (feature-less) monocular SLAM algorithm
which, in contrast to current state-of-the-art regarding direct methods,
allows to build large-scale, consistent maps of the environment.
Along with highly accurate pose estimation based on direct image alignment,
the 3D environment is reconstructed in real-time as pose-graph of
keyframes with associated semi-dense depth maps. These are obtained by
filtering over a large number of pixelwise small-baseline stereo comparisons.
The explicitly scale-drift aware formulation allows the approach to
operate on challenging sequences including large variations in scene scale.
Major enablers are two key novelties: (1) a novel direct tracking method
which operates on sim(3), thereby explicitly detecting scale-drift, and
(2) an elegant probabilistic solution to include the effect of noisy depth
values into tracking. The resulting direct monocular SLAM system runs
in real-time on a CPU.

#### Introduction
Real-time monocular Simultaneous Localization and Mapping (SLAM) and 3D
reconstruction have become increasingly popular research topics. Two major
reasons are (1) their use in robotics, in particular to navigate unmanned aerial
vehicles (UAVs) [10, 8, 1], and (2) augmented and virtual reality applications
slowly making their way into the mass-market.
One of the major benefits of monocular SLAM – and simultaneously one of
the biggest challenges – comes with the inherent scale-ambiguity: The scale of
the world cannot be observed and drifts over time, being one of the major error
sources. The advantage is that this allows to seamlessly switch between differently
scaled environments, such as a desk environment indoors and large-scale
outdoor environments. Scaled sensors on the other hand, such as depth or stereo
cameras, have a limited range at which they can provide reliable measurements
and hence do not provide this flexibility.

Pipeline of LSD-SLAM:
![Pipeline of LSD-SLAM][lsd-slam]

### SVO: Fast Semi-Direct Monocular Visual Odometry

#### Abstract

We propose a semi-direct monocular visual odometry
algorithm that is precise, robust, and faster than current
state-of-the-art methods. The semi-direct approach eliminates
the need of costly feature extraction and robust matching
techniques for motion estimation. Our algorithm operates
directly on pixel intensities, which results in subpixel precision
at high frame-rates. A probabilistic mapping method that
explicitly models outlier measurements is used to estimate 3D
points, which results in fewer outliers and more reliable points.
Precise and high frame-rate motion estimation brings increased
robustness in scenes of little, repetitive, and high-frequency
texture. The algorithm is applied to micro-aerial-vehicle stateestimation
in GPS-denied environments and runs at 55 frames
per second on the onboard embedded computer and at more
than 300 frames per second on a consumer laptop. We call our
approach SVO (Semi-direct Visual Odometry) and release our
implementation as open-source software.

Methods that simultaneously recover camera pose and
scene structure from video can be divided into two classes:

- Feature-Based Methods: The standard approach is
to extract a sparse set of salient image features (e.g. points,
lines) in each image; match them in successive frames using
invariant feature descriptors; robustly recover both camera
motion and structure using epipolar geometry; finally, refine
the pose and structure through reprojection error minimization.

- Direct Methods: Direct methods [13] estimate structure
and motion directly from intensity values in the image.
The local intensity gradient magnitude and direction is used
in the optimisation compared to feature-based methods that
consider only the distance to some feature-location. Direct
methods that exploit all the information in the image, even
from areas where gradients are small, have been shown to
outperform feature-based methods in terms of robustness in
scenes with little texture [14] or in the case of cameradefocus
and motion blur [15].


Pipeline of SVO-SLAM:
![Pipeline of SVO-SLAM][svo-slam]


### Visual-Inertial Monocular SLAM with Map Reuse
Abstract— In recent years there have been excellent results
in Visual-Inertial Odometry techniques, which aim to compute
the incremental motion of the sensor with high accuracy
and robustness. However these approaches lack the capability
to close loops, and trajectory estimation accumulates drift
even if the sensor is continually revisiting the same place. In
this work we present a novel tightly-coupled Visual-Inertial
Simultaneous Localization and Mapping system that is able to
close loops and reuse its map to achieve zero-drift localization in
already mapped areas. While our approach can be applied to
any camera configuration, we address here the most general
problem of a monocular camera, with its well-known scale
ambiguity. We also propose a novel IMU initialization method,
which computes the scale, the gravity direction, the velocity,
and gyroscope and accelerometer biases, in a few seconds with
high accuracy. We test our system in the 11 sequences of a
recent micro-aerial vehicle public dataset achieving a typical
scale factor error of 1% and centimeter precision. We compare
to the state-of-the-art in visual-inertial odometry in sequences
with revisiting, proving the better accuracy of our method due
to map reuse and no drift accumulation.
Index Terms— SLAM, Sensor Fusion, Visual-Based Navigation


### Visual-Inertial Direct SLAM

#### Abstract

The so-called direct visual SLAM methods have
shown a great potential in estimating a semidense or fully
dense reconstruction of the scene, in contrast to the sparse
reconstructions of the traditional feature-based algorithms. In
this paper, we propose for the first time a direct, tightly-coupled
formulation for the combination of visual and inertial data.
Our algorithm runs in real-time on a standard CPU. The
processing is split in three threads. The first thread runs
at frame rate and estimates the camera motion by a joint
non-linear optimization from visual and inertial data given a
semidense map. The second one creates a semidense map of
high-gradient areas only for camera tracking purposes. Finally,
the third thread estimates a fully dense reconstruction of the
scene at a lower frame rate. We have evaluated our algorithm
in several real sequences with ground truth trajectory data,
showing a state-of-the-art performance.

### Keyframe-Based Visual-Inertial SLAM Using Nonlinear Optimization

#### Abstract
The fusion of visual and inertial cues has become popular in robotics due to the complementary nature of the two sensing modalities. While most fusion strategies to date rely on filtering schemes, the visual robotics community has recently turned to non-linear optimization approaches for tasks such as visual Simultaneous Localization And Mapping (SLAM), following the discovery that this comes with significant advantages in quality of performance and computational complexity. Following this trend, we present a novel approach to tightly integrate visual measurements with readings from an Inertial Measurement Unit (IMU) in SLAM. An IMU error term is integrated with the landmark reprojection error in a fully probabilistic manner, resulting to a joint non-linear cost function to be optimized. Employing the powerful concept of ‘keyframes’ we partially marginalize old states to maintain a bounded-sized optimization window, ensuring real-time operation.  Comparing against both vision-only and loosely-coupled visual-inertial algorithms, our experiments confirm the benefits of tight fusion in terms of accuracy and robustness.




Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo")

Reference-style: 
![alt text][logo]

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"
[orb-slam]:orb-slam-pipeline.png
[svo-slam]:svo-slam-pipeline.png
[lsd-slam]:lsd-slam-pipeline.png

