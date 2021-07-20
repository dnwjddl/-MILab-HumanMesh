# SPIN: Learning to Reconstruct 3D Human Pose and Shape via Model-fitting in the Loop

**model-based human pose estimations** -> 2가지 패러다임

1. Optimization based methods
- parametric body model를 2D observation에 반복적(iterative)으로 적합시켜서 정확한 image model alignments로 이어짐
- 단점: 속도가 느리고, 초기화에 민감함

2. Regression based methods
- 픽셀에서 model paramters들을 직접 estimate하기 위해 deep network를 사용
- 엄청난 양의 supervision필요하면서 합리적이지만 픽셀 정확하지 않은 결과를 제공하는 경향이 있음

## SPIN
어떤 접근방법이 더 좋은지 조사하는 대신 두패러다임의 협업, **strong collaboration**

- 네트워크에서 reasonable, directly regressed된 estimate 사용하면 iterative optimization를 initialize하여 fitting을 더 빠르고 정확하게 수행할 수 있음
- iterative optimization에 따른 픽셀의 accurate fit은 네트워크에 대한 strong supervision 역할을 할 수 있음

# SPIN (SMPL oPtimization IN the loop)
- Deep Network는 training loop내의 2D joint에 신체 모델을 맞추는 iterative optimization routine을 초기화하고, fitted estimate은 이후에 네트워크를 supervise 하는데 사용
- Better network estimates은 더 나은 solution으로 optimization을 이끌 수 있고 더 accurate optimization은 network에 대한 더 나은 supervision을 제공하기 때문에 우리의 접근방식은 self-improving by nature
- 3D ground truth이 희박하거나 구할 수 없는 다양한 환경에서 접근방식의 효과를 입증하고 최신 모델 기반 포즈 추정 접근 방식을 상당한 차이로 consistently outperform

![image](https://user-images.githubusercontent.com/72767245/126330142-d825f708-1adf-47b6-9b01-66e9f59d116b.png)
