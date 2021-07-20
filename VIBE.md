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

![image](https://user-images.githubusercontent.com/72767245/126318090-27362a58-d49c-4288-8c16-796cf831e46f.png)  

The question is how can we obtain realistic 3D human motions from our generator?  
To achieve this, we train a motion discriminator using a large-scale 3D motion capture dataset called AMASS  

The motion discriminator takes predicted pose sequences along with pose sequenxes sampled from AMASS.  

The motion discriminator is trained to tell which sequence is real or fake.  

If the motion generator is able to fool the discriminator, the predicted motion is realistic.  
Training both the generator and discriminator together results in a method that achieves state-of-the-art performance.  

The motion discriminator uses a stack of GRU layers to process poses sequentially.  
Then, a self attention mechanism dynamically aggregates features and amplifies the contribution of important frames.  


## Datasets
During Training, we use a mix of 2D and 3D datasets

## Results

For evaluation, we use challenging 3DPW dataset because it contains in the wild sequences with reference 3D pose and shape data  

We report the 3D distance between ground truth and predicted joints in millimeters  

> EVAL Metrics: **MPJPE** (Mean per joint position error)  

![image](https://user-images.githubusercontent.com/72767245/126319178-9670e720-7b2d-44bf-b74d-2d88fb2fc7b1.png)

This chart shows the reconstruction error of recent state-of-art methods on the 3DPW dataset.   

HMR and SPIN are **frame based** methods.  
Whereas, temporal HMR and our VIBE method use video sequences    

VIBE* uses the same datasets as others during training.  
While, VIBE benefits from additional 3DPW training data.  

VIBE reduces reconstruction error relative to the state-of-the art by a significant margin.  

VIBE outperforms both video and frame based methods.  


---

## Qualitative Results
 
we qualitatively compare VIBE with t-HMR   
  
temporal HMR represents the recent state-of-the-art in video based human pose estimation.  
 
Compared to temporal HMR, VIBE captures pose and shape more accurately.  
temporal HMR are usally over smoothes the pose predictions while sacrificing accuracy.  

On the other hand, VIBE predictions align significantly better with the human body.  


---

VIBE fails in the cases of heavy occlusion, fast motions and multi person occlusion.  


---

In conclusion, we introduce a recurrent architecture that propagates information overtime.  

To obtain realistic motions, we introduced discriminative training of motion sequences using the AMASS dataset.  

We introduced self-attention mechanism in the motion discriminator.  
so it learns to focus on the important temporal structure of human motion.  

VIBE produces 3D body shapes and poses that are realistic and kinematically plausible.  
VIBE achieve state-of-art results on challenging datasets  
