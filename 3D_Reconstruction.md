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


---

**[SMPLify]**  
SMPLify 는 deep learning 방식이 아님.  
Training time이 없고, Inference time에 이미지에 맞게 optimization을 통해 SMPL parameter를 바로 optimize 하는 방식입니다.      
<br><br>

**[HMR]**  
SMPL GT annotation이 존재하는지 여부에 따라 loss가 다르게 적용
생략 <br><br>

**[SPIN]**    
SPIN에서는 HMR과 SMPLify를 합쳐서 사용
또 이러한 Iterative fitting이 Optimization layer와 Regression network 상호보완적으로 도움을 줌  
<br>
Optimization + Regression을 사용하는 것의 가장 핵심은 대부분의 Human pose dataset에 GT SMPL parameter annotation이 존재하지 않는 경우를 해결하기 위한 것입니다.
HMR에서 아마 SMPL GT annotation이 존재하는지 여부에 따라 loss가 다르게 적용되는 것을 보셨을 것입니다.
만약 SMPLify와 같은 optimization을 통해 학습 시간이 더 걸리더라도, GT SMPL 파라미터를 가지고 있지 않은 training image에 대해 꽤 괜찮은 annotation을 얻어낼 수 있다면, regression 성능을 올릴 수 있겠죠 (추가적인 annotation을 사용할 수 있으니까요).  

따라서 SPIN의 경우에는 학습 시간이 조금 더 걸리더라도, SMPLify를 HMR의 CNN에 이어붙여, pseudo-GT SMPL parameter annotation을 얻어낼 수 있었고,
이를 통해 regression network 학습에 추가적인 Supervision을 제공하여 SMPL parameter regression 성능을 끌어올릴 수 있다는 점이 제 생각에는 가장 큰 contribution입니다. (Optimization layer가 Regression network를 도와주는 방향)
또한, 반대 방향으로, Regression network 뒤에 붙는 SMPLify 와 같은 opt. layer는, 학습 초반에는 HMR에서 추정하는 SMPL parameter가 아직 오류가 많아, optimize time이 오래 걸립니다.
하지만 regression network의 학습이 진행될수록, SMPLify 에 제공되는 Initial SMPL parameter가 조금 더 좋아지게 되고, optimize를 위해 이전처럼 많은 step이 필요하지는 않게 됩니다. (Regression network가 Optimization layer를 도와주는 방향)
<br>
<br>
마지막으로 헷갈리시면 안되는 점은, SPIN에서는 학습 중에만 Optimization layer를 사용한다는 점입니다.   
Inference time에는 단순히 한번 feed forward 하여 (HMR 처럼) SMPL parameter를 추정하게 됩니다.

**[VIBE]**  
Video domain에 가지고 옴  
한계점 설명 | occlusion, Noisy observation cases  
- inference time에 optimization이 필요하지 않음

**[HuMoR]**
Motion prior를 따로 학습하여 inference time에 이 prior를 활용한 optimization이 따로 필요합니다.     
진자의 운동, 사람의 운동(물리적인 것들을) modeling해서 occlusion에 robust하게 만들 수 있음

> Real-time application 을 위한 연구에는 vibe가 용이할 것으로 보입니다.   

VIBE 이외에도 video에서 SMPL fitting을 위한 다양한 연구가 많습니다. (https://akanazawa.github.io/human_dynamics/ 등등 찾아보시면 많습니다.)  

또한 HuMoR에서 얘기한 motion prior는 자체적으로 정의를 내린 Human motion state와, markov assumption을 통해 학습한 prior이고, VIBE에서 사용한 motion prior와는 다르다고 보시면 될 것 같습니다.  


