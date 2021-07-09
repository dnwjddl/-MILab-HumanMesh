# [MILab] HumanMesh 
Efficient Human behavior understanding_3d pose estimate

## Schedule
|date|works|-|
|----|----|----|
||pose estimate|O|
||OpenPose(CVPR2017)||
||DensePose(CVPR2018)||
||TotalCapture||
||Baseline1||
||Baseline2(HMR)|https://github.com/MandyMo/pytorch_HMR/tree/master/src|
||개발||


## WORKS
- 논문 하루에 하나씩

## 목표
논문을 공부하고 HMR을 기반으로하여, 백본 네트워크를 본인의 아이디어로 아키텍처를 재구성하고 학습시켜 성능을 유지하면서 속도 올리기(RealTime)
- Single Image 기반 Human Mesh Recovery에서 더 도전적으로 [VIBE, CVPR2020]
- Bounding Box를 detection하면서 동시에 human mesh recovery가 가능한 형태로 Mask R-CNN이나 Yolo등의 Two/One stage방법등으로 확장 시도

## References

### 3D human mesh Recovery
- SMPL:A Skinned Multi-Person Linear Model, ACM Trans. Graphics (Proc. SIGGRAPH Asia), 2015
- Keep it {SMPL}: Automatic Estimation of {3D} Human Pose and Shape from a Single Image, ECCV 2016
- End-to-end Recovery of Human Shape and Pose, CVPR 2018
- VIBE: Video Inference for Human Body Pose and Shape Estimation, CVPR 2020
- End-to-End Human Pose and Mesh Reconstruction with Transformers, CVPR 2021
[참고](https://learning-sarah.tistory.com/entry/METROEnd-to-End-Human-Pose-and-Mesh-Reconstruction-with-Transformers)

### Models and Light-weight models
- Mask R-CNN, ICCV 2017 
- Focal Loss for Dense Object Detection, ICCV 2017(RetinaNet) 
- YOLACT:Real-time Instance Segmentation, ICCV 2019
- MobileNets: Efficient Convolutional Neural Neetworks for Mobile Vision Applications, arXiv 2017
- CONVOLUTIONAL NEURAL NETWORKS WITH LOWRANK REGULARIZATION, ICLR 2016

