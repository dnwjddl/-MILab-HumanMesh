# Transformer 선행 공부
- Encoding, Decoding, connection
- Encoding: 여러개의 Encoder를 쌓아 올려 만든 것
- Decoding: encoder과 동일한 개수만큼의 decoder 쌓아 올림

## Encoder
- 모두 똑같은 구조
- 그들 간의 weight은 공유하지 않음
- 하나의 encoder에는 두개의 sub-layer 있음
  - Self-Attention : encoder가 하나의 특정한 단어를 encode하기 위해서 입력 내의 모든 다른 단어들간의 관계를 살펴봄
  - Feed Forward Neural Network: 각 위치의 단어마다 독립적으로 적용돼 출력을 만듦

## Decoder
- 세개의 layer
  - Self-Attention
  - Encoder-Decoder Attention: decoder가 입력 문장 중에서 각 타임 스텝에서 가장 관련있는 부분에 집중할 수 있도록 해줌
  - Feed Forward NN

## Self-Attention
Self-Attention의 가장 첫 단계는 encoder에 입력된 벡터들에게서부터 각 3개의 벡터를 만들어내는 일  
각 단어에 대하여 ```Query 벡터```, ```Key 벡터```, ```Value 벡터``` > 입력 벡터에 대해서 세 개의 학습 가능한 행렬들을 각각 곱함으로써 만들어짐  

#### Query 벡터




# End-to-End Human Pose and Mesh Reconstruction with Transformers

# Abstract

- **```METRO(Mesh TRansfOrmer)```** 이라는 새로운 방법 제시(single image로 3D human pose&mesh vertices 재구성)
- **transformer encoder**를 이용해 vertex-vertex 와 vertex-joint **iteraction**를 jointly model함

**OUTPUT** : 3D joint coordinates와 mesh vertices 를 동시에 뽑아냄

- 차별점
  - 기존 모델: pose와 shape parameter를 regress함
  - 기존 모델(SMPL): parametric mesh models에 의존
  - ```METRO```: 파라미터에 의존하지 않음 -> 덕분에 hands와 같은 다른 object로도 확장이 용이

- 장점
  - transformer self-attention mechanism이 mesh topology 필요성을 줄이고 두 vertices 사이에서 freely attend 하게 함
    - 저렇게 함으로써, mesh vertices 와 joints 사이의 **non-local relationships**을 학습하는 것이 가능해짐
- proposed **masked vertex modeling**를 통해 **robust**하고 **partial occlusion**같은 challenging situation를 다루는데 효과적임


```parametric mesh model > masked vertex modeling```

- Human3.6M과 3DPW 데이터셋에서 human mesh reconstruction에 대한 SOTA 결과를 냄
- 3D human reconstruction에서 현재 SOTA인 FreiHAND 데이터셋을 능가하는 범용성을 보임

# Introduction

### CONTRIBUTION [4가지]
- NEW transformer-based method(METRO)
  - 3D human pose and mesh reconstruction from a single image
  - single image로부터 3D human pose and mesh를 reconstruction을 하는 새로운 transformer-based method 도입
- the Masked Vertex Modeling objective
  - better reconstruction을 위해 vertex-vertex 와 vertex-joint interaction을 모델링하기 위해 multi-layer transformer encoder을 포함한 Masked Vertex Modeling objective 디자인함 
- METRO : human mesh (Human3.6M과 challenging 3DPW 데이터셋에서 SOTA)
- METRO : hands (FreiHAND 리더보드에서 1위) - Generalization
  - 다른 타입의 3D mesh를 예측할 수 있음

---


- VR, 스포츠 모션 분석, 신경퇴행성 진단 분석 등에서 3D human pose/mesh reconstruction의 관심이 높아짐
- 그러나 complex articulated motion과 occlusion으로 인해 challenging 함


### 이 분야의 work는 **두가지 범주**로 나눌 수 있음

#### 1. ```SMPL```과 같은 **parametric model**를 이용
- **강점**: shape와 pose coefficients를 예측하도록 학습되는데 environment variations에 robust 함
- **단점**: pose와 shape space가 parametric model을 구축하는데 사용되는 limited exemplars에 의해 제한된다는 것
  - 이것을 극복하기 위한 두번째 방법이 고안

#### 2. **Graph convolution neural network(GCNN)나 1D heatmap**를 이용
graph convolutional neural network(to model neighborhood vertex-vertex interactions)  
1D heatmap(to regress vertex coordinates)

- **단점**: non-local vertex-vertex interaction을 모델하는데 효과적이지 않음


---

- 선행 연구에서 다른 body part(ex. hand-foot)에 소속된 non-local vertices 사이에 strong correlation이 있다고 보여짐
- [Computer Graphics & Robotics] inverse kinetics techniques(역운동학 기술) 는 hand tip과 같은 end effector의 position을 받은 articulated figure의 Internal joint position을 estimate 하도록 개발됨

---

### 필요성
- 우리는 short range와 long range를 포함하여 ```body joints와 mesh vertices 사이의 correlation을 학습```하는 것이 challenging한 pose와 occlusions를 핸들링하는데 필요하다 생각

### METRO 모델
- 본 논문에서는 **global vertex-vertex interactions**를 모델링하는 심플하지만 효과적인 프레임워크 제시 -> **주구성요소는 transformer**임


### Transformer(자연어 처리)
- 최근의 연구는 transformer의 **self-attention mechanism** 덕분에 다양한 task의 성능향상을 보여줌
- transformer은 특히 input과 output사이의 거리 상관없이 **dependencies(or interactions)를 모델링**하는데 효과적
- transformer는 relevant token을 soft-search할 수 있고, 중요한 features에 기반하여 예측함

---

### 본 논문
- (progressive dimension reduction을 사용하는) multi-layer transformer encoder 인 ```METRO```제안
  - input image로부터 **3D body joint**와 **mesh vertices**를 동시적으로 reconstruct함
- ```transformer encoder architecture```에 **```masked vertex modeling object````**를 추가하여 joints와 vertices사이의 interaction을 강화함
- figure1과 같이 ```METRO```는 joints와 mesh vertices사이의 short-range와 long-range interaction를 발견하도록 학습하여 큰 pose변화와 occlusion을 가진 3D human pose를 reconstruct하는데 도움이 되도록 함

### 실험 결과
- ```METRO```가 vertex-vertex와 vertex-joint interaction을 하는데 효과적이고, human mesh reconstruction에 있어서 large margin을 두고 이전 연구를 뛰어넘는 것을 보여줌
- METRO는 single image로부터 3D human pose와 mesh reconstruction을 jointly learn하는데에 **transformer encoder**를 사용한 첫번째 시도
- 또한, METRO는 input image로부터 3D hand를 reconstruct하는 등 다른 3D mesh를 에측하는데 쉽게 적용되는 general framework



![image](https://user-images.githubusercontent.com/72767245/126170999-70c2706f-ff1c-42fe-a0ef-c570411c1cec.png)

- ```METRO```는 human mesh reconstruction을 위해 body joints와 mesh vertices사이의 non-local interactions를 학습
- (a) input image, ```METRO```는 non-local interactions을 고려하여 human mesh를 예측한다
- (b) occluded wrist joint와 mesh vertices의 attention (brighter color일 수록 강한 attention 의미)
- (c) reconstruct mesh 

# Related Works
## Human Mesh Reconstruction(HMR)
3D human body shape를 reconstruct하는 Task  
초기 연구는 다양한 센서를 이용해서 reconstruction을 수행함 -> 점차 효과적이고 간편한 monocular camera 이용하려함  
하지만, single image로부터의 HMR은 **pose variation, occlusions, limited 3D training data**로 어려움

1. 이전 연구들(SMPL, STAR, MANO)등의 사전학습된 ```parametric human models```를 제안함
- HMR에 대한 parametric model의 pose와 shape coefficient를 estimate함
  - 그러나 input image로부터 바로 pose와 shape coefficients를 regress하는 것은 어렵기 때문에 human skeletons 나 segmentation map과 같은 human body를 다루기도 함

2. parametric human model을 채택하는 것 대신, input image를 통해 human body를 directly하게 regress하는 방법
(방법) **3D mesh, volumetric space, occupancy field**등을 이용해서 represent  
- **GraphCMR**:  3D mesh vertices를 graph convolutional neural networks(GCNN)를 이용해 regress하는 것이 목표
- **pose2Mesh**(최근): GCNN을 이용한 cascaded model임
  - Pose2Mesh는 주어진 human pose representation을 기반으로 human mesh을 재구성함

### GCNN based method
**GCNN** based method는 pre-specified mesh topology를 이용하여 neighborhood vertex-vertex interactions를 모델링하도록 디자인했는데 longer range interactions를 모델링하는데 덜 효과적임

> 반면에 METRO models는 어떠한 mesh topology에 국한되지 않고 joints와 mesh vertices사이의 global interactions를 모델링 가능

## Attentions and Transformers
- 최근의 연구들은 **attention mechanism**이 다양한 language tasks의 성능향상을 보여줌
- ```key insight```는 output을 예측하는데에 있어서 더 중요한 **relevant inputs를 soft-search해서 attention**한다는 것
- Vaswani et al. 은 attention mechanisms 만을 기반으로 한 transformer architecture을 제안함
- Transformer은 (효율적인 train과 inference을 위하여) multi-head self-attention을 이용하여 highly parallelized(고도로 병렬화 됨)함 -> NLP분야에서 높은 성능을 보임
- BERT와 GPT에서 살펴본 것 처럼 규모에 맞는 언어 모델링에서 탁월한 성능을 이끌어 냄
- NLP 분야의 성공으로 인해 **vision분야**에서도 image generation에 있어서 pixel distributions를 학습하거나 분류, detection등의 task에 transformer를 이용해보려는 시도가 있음
  - 하지만 3D human reconstruction에서는 이러한 방향으로의 시도가 없었음


> we present a multi-layer transformer architecture with progressive dimensionality reduction to regress the 3D coordinates of the joints and vertices.

- 해당 논문에서는 progressive dimensionality reduction을 이용해서 joints와 vertices를 regress하는 multi-layer transformer architecture를 제시함


# Method

![image](https://user-images.githubusercontent.com/72767245/126182117-1dad009d-69fb-4aa6-89d2-649ea13f48ad.png)

- ```INPUT```: 224x224 image
- ```OUTPUT```: body joints J and mesh vertices V
- 두가지 ```MODULES```:
  - 1. Convolutional Neural Networks: input image로부터 feature vector를 뽑아냄
  - 2. Multi-Layer Transformer Encoder: feature vector를 input으로 받아서 body joints와 mesh vertex의 3D coordinates로 받음
     
     
     
     
- 1. CNN사용: input image을 통해 to extract an image feature vector
- 2. Multi-Layer Transformer Encoder: takes as input the feature vector and outputs the 3D coordinates of the body joint and mesh vertex in parallel.



## 1. Convolutional Neural Networks
- feature extraction을 위하여 사용
- ImageNet 분류 문제로 사전 학습되어 있음
- 마지막 Hidden layer에서 feature vectore를 추출(2048d)
- 추출된 feature vector X를 Transformer에 input으로 사용해 regress
- Transformer은 end-to-end training for human pose and mesh reconstruction을 가능하게 함
- Transformer은 HRNETs와 같이 large-scale pre-trained CNN으로 이득을 얻음
- 본 실험에서 우리는 input feature를 분석해, high resolution image features가 3D coordinates(body joints & mesh vertices)들을 regress하는데 유용하다는 것을 발견

## 2. Multi-Layer Transformer Encoder with Progressive Dimensionality Reduction
- 우리는 **3D coordinates**를 output으로 하기 때문에, 현재의 transformer architecture을 그대로 적용할 수 없음
  - 지금의 transformer은 모든 transformer layers에 **같은** dimensionality의 hidden embedding를 사용하기 때문임
  - because they use a constant dimensionality of the hidden embedding for all the transformer layers.
- 따라서 우리는 **progressive dimensionality reduction scheme**을 가진 new architecture를 고안함


![image](https://user-images.githubusercontent.com/72767245/126279115-32e66b66-16a6-41ff-b13c-0473c31ad1d5.png)


- **Linear projections**을 이용하여 encoder layer 뒤의 hidden embedding의 dimensionality을 줄임
- **Multiple encoder layer**를 추가함으로써, 모델은 self-attention과 dimensionality reduction을 차례로 수행
- Transformer encoder의 마지막 output vector은 **joints와 mesh vertices의 3D coordinates**임



---

### Input Query
- Transformer encoder의 **INPUT**: body joints & mesh vertex queries
- **Positional Encoding**:  Template Human Mesh 사용 > 입력 sequence에서 각 query의 위치 정보를 보존하기 위해서
  - Image Feature vector ```X (2048d)``` 를 every ```body joint i``` 의 ```3D coordinates(x_i, y_i, z_i)``` 와 concat하여 ```Q_J={Q^J_1, Q^J_2...}의 joint queries set```을 만듦
  - 모든 ```mesh vertex j``` 의 positional encoding을 수행해, Q_V = {q^V_1, q^V_2,..} 의 vertex queries set을 만듦

---


## 3. Masked Vertex Modeling
- 선행 연구에선 Masked Language Modeling (MLM)을 사용해 training corpus의 linguistic properties를 학습하였음
  - BUT, MLM은 input을 recover하는게 목적이기 때문에 our regression task에 바로 적용하기 어려움
- Bi-directional attentions을 활성화시키기 위하여 **Masked vertex Modeling(MVM)**을 고안함
  - input queries를 random으로 일정 percentages를 mask함
- MLM처럼 masked input을 recovering 하는 것과 달리 transformer에게 all the joints and vertices를 regress하도록 함

- missing query와 상응하는 output을 predict하기 위해 model은 **다른 relevant queries**를 이용함
  - 부분적으로 body parts가 안보이는 occlusions를 simulating하는 것과 비슷


- **결과적으로** MVM은 transformer가 distances나 mesh topology와 상관없이 다른 **관련 있는 vertices 나 joints를 고려**하여 3D coordinates를 regress하도록 함
  - 더 나은 human body modeling을 위한 joints와 vertices간의 short range와 long range interactions를 facilitates함



## 4. Training
- transformer encoder을 train하기 위해서, loss functions을 transformer output에 적용하여 predictios과 groud truth간의 error을 줄이려함
- dataset $D = \{I^i, \bar{V}^i_{3D}, \bar{J}^i_{3D}, \bar{J}^i_{2D} \}^T_{i=1}$
  - $T$ = training images의 total number
  - $I \in R^{w \times h \times 3}$ = RGB image
  - $\bar{V}_{3D} \in R^{M\times3}$ = mesh vertices의 ground truth 3D coordinates, M은 number of vertices
  - $\bar{J}_{3D} \in R^{K\times3}$ = body joints의 ground truth 3D coordinates, K는 number of joints of a person
  - $\bar{J}_{3D} \in R^{K \times 2}$= body joints의 ground truth 2D coordinates

## 5. Implementation Details


# Experimental Results

## Datasets
- 3D/ 2D training data를 이용해서 mix-training을 진행
- **Human3.6M**
  - 2D/3D annotations를 가진 large-scale dataset
  - 각 image는 different action을 보임
  - 라이센스 이슈로 3D annotations는 사용이 불가능함
    - 학습을 위해 pseudo 3D mesh을 사용
    - pseudo labels는 SMPLify-X모델을 사용하여 생성
  - 평가를 위해 Human3.6M에 제공된 groundtruth 3D pose labels를 이용함
  - subjects S1, S5, S6, S7, S8을 이용해 train하고 S9, S11 로 test
- **3DPW**
  - 2D/3D annotations를 가진 outdoor image dataset
  - training set은 22K images, test set은 35K images
    - training data를 이용해서 3DPW 실험 진행
- **UP-3D**
  - outdoor-image dataset
  - 모델 fitting을 통해 3D annotations를 생성함
  - training set은 7K images를 가지고 있음
- **MuCo-3DHP**
  - MPI-INF-3DHP 데이터셋을 기반으로 synthesize된 dataset
  - real-world background를 가진 200k의 training data를 가짐
- **COCO**
  - 2D annotations를 가진 large-scale dataset
  - SMPLify-X모델로 얻은 pseudo 3D mesh labels을 사용
- **MPII**
  - 2D pose label을 가진 outdoor-image dataset
  - training set은 14K images를 가짐
- **FreiHAND**
  - 3D hand dataset
  - training data는 130K의 images로 test set은 4K images로 구성
  - 본 데이터셋을 이용해 METRO의 genealizability 를 보여줌

## Evaluation Metrics
- metric단위는 milimetter(mm)
- **MPJPE**
  - Mean-Per-Joint-Position-Error(MPJPE)
  - human 3D pose를 평가하기 위한 metric
  - ground truth joints와 predicted joints사이의 유클라디안 거리를 측정
- **PA-MP JPE**
  - Procrustes Analysis(PA)를 이용해서 3D alignment를 수행하고 MPJPE를 계산함
  - 3D reconstruction을 평가하기에 잘 사용됨
    - scale과 rigid pose 상관없이(ex. translations and rotations) reconstructed structure error를 측정함
- **MPVE**
  - Mean-Per-Vertex-Error(MPVE)
  - ground truth vertices와 predicted vertices사이의 유클라디안 거리

## Main Results

## Ablation Study

# Conclusion
- 우리는 심플하지만 효과적인 mesh transformer framework을 이용해서 single input image로부터 human pose와 mesh를 추정
- Masked Vertex Modeling objective을 이용해 body joints와 mesh vertices의 non-local interactions를 학습함
- 3DPW, Human3.6M, FreiHAND datasets에서 SOTA 성능을 보임
- input-dependent한 non-local interactions을 학습해 성능향상이 되었음
  - 이는 mesh topology와 상관없이 important joints and vertices에 기반하여 예측을 가능하게 함
- 3D hand reconstruction을 이용하여 generalization capability을 증명함

--

# Appendices

