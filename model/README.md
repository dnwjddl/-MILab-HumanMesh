## Parameter 비교

|Model|# Parameters|Input Size(MB)|Forward/Backward pass size(MB)|Params size(MB)|Estimated Total Size(MB)|
|:----:|:----:|:----:|:----:|:----:|:----:|
|MobileNetv1|4,231,976|0.57|115.43|16.14|132.15|
|MobileNetv2|3,504,872|0.57|157.24|13.37|171.19|
|MobileNetv3|2,938,368|0.57|40.17|11.21|51.95|
|ShuffleNet|1,877,920|0.57|62.08|7.16|69.82|
|ShuffleNetv2|2,278,604|0.57|47.94|8.69|57.21|

- MobileNet에서 MobileNetv2에서 ```Bottleneck Residual Block```을 설계
- MobileNetv3은 앞의 버전들 보다 훨씬 더 적은 파라미터랑 좋은 성능을 띄고있음
  - MobileNetv3은 ```AutoML```을 사용

## 새로운 Architecture 제안
- 3x3을 전부 1x1 -> 3x3로 바꿈
- 5x5는 차라리 3x3, 3x3 이 더 좋음
- 1x1의 pointwise Convolution의 연산이 많아지게 될 때, ```Bottleneck Residual Block```을 사용하여 개선한다

- ShuffleNet은 MobileNet보다 더 적은 paramter을 가짐
  - 여기서 MobileNetv3에서 쓴 것 처럼 ```AutoML```을 쓴다면 더 적은 파라미터를 가질 수 있지 않을까?

## 제안 (Pruning, Quantization, Knowledge Distillation 모두 적용)
- 주요로 사용하는 block들을 수정하면서 model 만들어봄
1. MobileNetv3 사용
2. ShuffleNet
3. ShuffleNet + AutoML
4. ShuffleNet + Residual Block 사용
 
- SqueezeNet에서 쓰인 Fire Module을 사용?
  - ShuffleNet에 FireModule 사용
  - MobileNet에 FireModule 사용
- SqueezeNet에서 FireModule 대신 ```Bottleneck Residual Block```사용


### 실험 결과

|모델|pt|#paramters|MPJPE|ReconstructionError|InferenceTime|
|:---:|:---:|:---:|:---:|:---:|:---:|
|hmr|(12)210808-064723|26,977,501|315|172|0.07067|
|pre_resnet|(20)210813-075405|26,977,501|445|194|0.07028|
|pre_resnet|(19)210813-075030|26,977,501|443|192|0.06059|
|pre_resnet|(11)210813-031301|26,977,501||||
