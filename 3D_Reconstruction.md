# [3D Reconstruction]

다양한 3차원 재구성(reconstruction)방법 중에서 3차원 주석이 달린 이미지에 의존적이지 않으면서 3차원 재구성을 수행할 수 있는 방법

- **SMPLify**같은 최적화 기반 방법은 Parametric human models에 의존하며, 몇가지 모델 매개변수만 에측하면 됨
- 이러한 방법들은 estimate된 pose가 2차원으로 투영시키는데 일어나는 오차를 최소화하는데만 신경을 쓰기 때문에 추정된 자세가 유효한지를 보장할 수 없다.
- 실제로, output quality는 초기화에 크게 의존하게 된다.
- 여기서 초기화란 2차원 자세에 body model을 처음에 fit하게 맞추는 작업을 의미하는 것 같다.


- 그렇기 때문에 비교적 까다로운 자세를 추정하지 못하는 문제점이 존재.
- 학습 시킬 때, 많은 수의 다양한 자세들로 이루어진 데이터세트들을 이용하여 모델을 만들 수도 있지만, 이는 다른 자세들을 그럴듯하고, 올바르게 모델링할 수 없다는 문제점을 가짐



---

SPIN(SPIN: SMPL oPtimization IN the loop)이라는 논문에서는 최적화기반 방법으로 initial solution을 개선하여 fitting 문제를 개선
