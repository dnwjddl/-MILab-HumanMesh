# Video Inference for Human Body Pose and Shape Estimation
- CVPR2020

```VIBE``` : 움직이는 video sequence가 주어지면 우리의 목표는 3D human pose와 shape을 추정  

대부분의 prior 방법에서는 단일이미지에서 3D shape과 pose를 regress함  
여기에서는 비디오를 활용하여 성능을 크게 향상시키는 방법을 보여줌  

실제 3D ground truth annotation이 있는 이미지 sequence가 별로 없기 때문에 문제는 어려움

Here we show how to significantly improve performance by exploiting video.

The problem is challenging because there are very few real image sequences with ground truth 3D training annotations.

As a result, these methods fail to produce accurate and kinematically plausible motions.
We need additional information to solve the problem.

we solve this problem by exploiting **a large dataset of unpaired 3D human motions.**

The key idea is to train the neural network to produce 3D sequences that are indistinguishable from real human motions.

To achieve this, we adopt an adversarial training approach.

We call the resulting method VIBE which stands for video inference for human body pose and shape estimation.


---


VIBE produces 3D body shapes and poses that are realistic and kinematically plausible.

VIBE first extracts image features using CNN and processes these features with a recurrent neural network to exploit the sequential nature of human motion.
Then, a regressor predicts the parameters of the SMPL body model for the whole input sequence.

We refer to this part of the model as the pose generator
