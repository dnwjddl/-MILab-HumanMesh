## 모델 압축을 위한 기본적인 접근 방법
1. ```가지치기(Pruning)```  
- 학습 후 불필요한 부분을 제거하는 방식
- 가중치의 크기에 기반한 제거, Attention head 제거, layer 제거
- 몇몇 방법은 prunability를 제거하기 위해 학습 중에 정규화방법을 도입하기도 함(layer dropout)

2. ```가중치 분해(Weight Factorization)```
- 가중치 행렬을 분해하여 두 개의 행렬의 곱으로 근사하는 방법
- 행렬이 낮은 rank을 가지도록 하는 제약조건(low-rank constraint)을 도입
- 가중치 분해는 토큰 임베딩이나 feed-forward/self-attention layer의 파라미터에 적용할 수 있음

3. ```지식 증류(Knowledge Distillation)```
- 미리 잘 학습된 큰 네트워크(teacher Network)로부터 실제로 사용하고자 하는 작은 네트워크(student network)를 학습시키는 방법
- 훨씬 작은 Transformer 모델을 pre-training/downstream-data에 대해 기본부터 학습시킴
- fully-sized model의 값을 soft label로 사용하면 최적화가 잘 이루어짐
- 몇몇 방법들은 추론시간을 빠르게 하기 위해 BERT를 다른 형태의 모델로 증류하기도 함
- 이외 다른 방법들은 teacher에 대해 더 자세히 분석하여 출력 값 뿐만 아니라 가중치 행렬이나 hidden activation값들을 사용하기도 함

4. ```가중치 공유(Weight Sharing)```
- 모델의 일부 가중치들을 다른 파라미터들과 공유하는 방식


5. ```양자화(Quantization)```
- 부동 소수점 값을 잘라내서 더 적은 비트만을 사용하는 방식입니다.
- 양자화된 값은 학습 과정중에 배울 수도 있고, 학습 후에 양자화 될 수도 있음

6. ```Pre-train vs Downstream```
- 일부 방법들은 BERT를 특정 downstream task에만 맞게 압축하지만, BERT를 task와 무관하게 압축하는 방법들도 있음

