'''
    file:   model.py
    date:   2018_05_03
    author: zhangxiong(1025679612@qq.com)
'''

class HMRNetBase(nn.Module):
  def __init__(self):
    super(HMRNetBase,self).__init__()
    self._read_configs()
    
    print('start creating sub modules...')
    self._create_sub_modules()
  def _create_sub_modules(self):
    ''' smpl model, SMPL can create a mesh from beta & theta '''
    self.smpl = SMPL(self.smpl_model, obj_saveable = True)
    ''' only resnet50 과 hourglass is allowed currently, maybe other encoder will be allowed later. '''
    
    if self.encoder_name == 'resnet50':
        print('creating resnet50')
        self.encoder = Resnet.load_Res50Model()
     elif self.encoder_name == 'hourglass':
        print('creating hourglass')
        self.encoder = _create_hourglass_net()
     elif self.encoder_name.startswith('densenet'):
        print('creating densenet')
        self.encoder = load_denseNet(self.encoder_name)
     else:
        assert 0
  
  def forward(self, inputs):
        ### Encoder 는 ResNet50, densenet, hourglass등이 쓰임 (각 encoder들은 _create_sub_modules 에서 생김)
        
    if self.encoder_name == 'resnet50':
       ## Encoder 넣어서 feature 추출 
      feature = self.encoder(inputs)
       ## 추출된 Feature 뽑아서 Regressor삽입 parameter 추출
      thetas = self.regressor(feature)
        
      detail_info = []
      for theta in thetas:
            detail_info.append(self._calc_detail_info(theta))
            return detail_info
     

if __name__ == '__main__':
  cam = np.array([[0.9, 0, 0]], dtype = np.float)
  pose = np.array([[-9.44920200e+01, -4.25263865e+01, -1.30050643e+01, -2.79970490e-01,
        3.24995661e-01,  5.03083125e-01, -6.90573755e-01, -4.12994214e-01,
       -4.21870093e-01,  5.98717416e-01, -1.48420885e-02, -3.85911139e-02,
        1.13642605e-01,  2.30647176e-01, -2.11843286e-01,  1.31767149e+00,
       -6.61596447e-01,  4.02174644e-01,  3.03129424e-02,  5.91100770e-02,
       -8.04416564e-02, -1.12944653e-01,  3.15045050e-01, -1.32838375e-01,
       -1.33748209e-01, -4.99408923e-01,  1.40508643e-01,  6.10867911e-02,
       -2.22951915e-02, -4.73448564e-02, -1.48489055e-01,  1.47620442e-01,
        3.24157346e-01,  7.78414851e-04,  1.70687935e-01, -1.54716815e-01,
        2.95053507e-01, -2.91967776e-01,  1.26000780e-01,  8.09572677e-02,
        1.54710846e-02, -4.21941758e-01,  7.44124075e-02,  1.17146423e-01,
        3.16305389e-01,  5.04810448e-01, -3.65526364e-01,  1.31366428e-01,
       -2.76658949e-02, -9.17315987e-03, -1.88285742e-01,  7.86409877e-03,
       -9.41106758e-02,  2.08424367e-01,  1.62278709e-01, -7.98170265e-01,
       -3.97403587e-03,  1.11321421e-01,  6.07793270e-01,  1.42215980e-01,
        4.48185010e-01, -1.38429048e-01,  3.77056061e-02,  4.48877661e-01,
        1.31445158e-01,  5.07427503e-02, -3.80920772e-01, -2.52292254e-02,
       -5.27745375e-02, -7.43903887e-02,  7.22498075e-02, -6.35824487e-03]])
  
  beta = np.array([[-3.54196257,  0.90870435, -1.0978663 , -0.20436199,  0.18589762, 0.55789026, -0.18163599,  0.12002746, -0.09172286,  0.4430783 ]])
  real_shapes = torch.from_numpy(beta).float().cuda()
  real_poses  = torch.from_numpy(pose).float().cuda()
  
  net = HMRNetBase().cuda()
  nx = torch.rand(2,3,224,224).float().cuda()
