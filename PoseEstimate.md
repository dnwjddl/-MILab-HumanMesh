# pose estimate


## (Markless) Human Pose Estimation 종류

||2D pose|3D pose|
|---|----|---|
|Single-Person|Input: Image| Input: Image/Depth|
|Multi-Person|Input: Image| Input: Image/Depth]

## Human Pose Estimation의 접근방식
- **Top-Down방식**
사람을 먼저 감지를 한 다음, 각 사람의 자세를 추정  
문제점1: 사람을 인식하지 못하면 측정할 수 없음  
문제점2: 사람의 수가 많아지면 계산량도 많아짐  
(Mask RCNN, Multi-Person Pose Estimation with Local Joint-to-Person Associations, Covolutional Pose Machines)

- **Bottom-Up방식**
관절 부위(키 포인트)를 먼저 감지하여 서로 연결해 모든 사람의 자세를 추정함  
문제점1: 찾은 관절을 매칭 할 수 있는 조합이 매우 많고 이를 적절하게 매칭하는데 시간이 많이 걸리고 정확도를 높이는 것이 힘듦  
(DeepCut: Joint Subset Partition and Labeling for Multi Person Pose Estimation)  
(ArtTrack: Articulated Multi-person Tracking in the Wild)


## OpenPose, CVPR 2017
- Caffe, OpenCV 기반 구성, 사람의 얼굴, 신체부위, 손가락을 실시간으로 추정
- 단일 모델, 다중 모델 검출 가능

**사람을 감지하고 각 사람에 각각 pose estimation을 수행하는 Top-Down방식 대신 관절을 먼저 찾아 여러 사람의 pose estimation을 수행하는 Bottom-Up접근으로도 pose estimation의 정확성고 속도를 개선할 수 있음**

[paper](https://arxiv.org/abs/1611.08050)

인간의 관절부위인 Keypoint Detection 하는 문제부터 시작해서 그 point들을 어떻게 연결할 것인지, 어떻게 관절 부위(joint or landmark)들을 산출할 거신지

[OpenPose 홈페이지](https://github.com/CMU-Perceptual-Computing-Lab/openpose)


- Keypoint를 localization하는 자세 추정기인 CPM(Convolutional Pose Machine)의 주된 내용
- 관절 간의 비 모수적 관계인 Part affinity Field(PAFs)를 계산하여 자세를 추정


## DensePose, CVPR 2018
Openpose는 2D좌표만을 추정함, **DensePose**는 RGB이미지 상의 인간의 모든 픽셀을 3D 표면에 매핑하는 것  
각 인간 영역 내의 신체부위 좌표를 여러 프레임마다 회귀시킨다.
또한, 지역기반 모델(Region-based model)과 fully convolutional networks 로 이루어져있으며 Cascading을 통해서 정확도를 향상시킴.

- DensePose는 자세추정(pose estimation), 객체탐지(Object Detection) 분야와 관련되어 있고, Part와 Intanse를 분할하는 문제를 해결하는 것이 목적
- 3D 기반의 객체 이해를 향한 발판이 될 수 있고, 증가현실, 그래픽, 인간-컴퓨터 상호작용고 같은 단순한 관절 위치 에측(landmark localalization)을 넘어서는 문제에 응용 간ㅇ


보통 이미지에서 표면 기반 모델(surface-based model)로 Dense Correspondence 를 설정하는 작업은 주로 깊이 센서 환경에서 처리  
대조적으로 여기서는 이미지 픽셀과 surface point사이에 correspondence가 성립되는 단일 RGB이미지를 입력으로 함  

3D 표면 모델은 제일 유명한 SMPL모델을 사용함. 네트워크는 mask RCNN에 의존하며, Deeplan을 기반으로 함

