import torch
from config import args
import json
import sys
import numpy as np
from util import batch_global_rigid_transformation, batch_rodrigues, batch_lrotmin, reflect_pose
import torch.nn as nn

class SMPL(nn.Module):
  def __init__(self, model_path, joint_type = 'cocoplus', obj_saveable = False):
    super(SMPL, self).__init__()
    
    if joint_type not in ['cocoplus', 'lsp']:
      msg = 'unknow joint type: {}, it must be either "cocoplus" or "lsp"'.format(joint_type)
      sys.exit(msg)
    
    self.model_path = model_path
    self.joint_type = joint_type
    with open(model_path, 'r') as reader:
      model = json.load(reader)
     
    if obj_saveable:
      self.faces = model['f']
    else:
      self.faces = None
    
if __name__ == '__main__':
  device = torch.device('cuda', 0)
  smpl = SMPL(args.smpl_model, obj_saveable = True).to(device)
  pose = np.array([1.22162998e+00,   1.17162502e+00,   1.16706634e+00,
            -1.20581151e-03,   8.60930011e-02,   4.45963144e-02,
            -1.52801601e-02,  -1.16911056e-02,  -6.02894090e-03,
            1.62427306e-01,   4.26302850e-02,  -1.55304456e-02,
            2.58729942e-02,  -2.15941742e-01,  -6.59851432e-02,
            7.79098943e-02,   1.96353287e-01,   6.44420758e-02,
            -5.43042570e-02,  -3.45508829e-02,   1.13200583e-02,
            -5.60734887e-04,   3.21716577e-01,  -2.18840033e-01,
            -7.61821344e-02,  -3.64610642e-01,   2.97633410e-01,
            9.65453908e-02,  -5.54007106e-03,   2.83410680e-02,
            -9.57194716e-02,   9.02515948e-02,   3.31488043e-01,
            -1.18847653e-01,   2.96623230e-01,  -4.76809204e-01,
            -1.53382001e-02,   1.72342166e-01,  -1.44332021e-01,
            -8.10869411e-02,   4.68325168e-02,   1.42248288e-01,
            -4.60898802e-02,  -4.05981280e-02,   5.28727695e-02,
            3.20133418e-02,  -5.23784310e-02,   2.41559884e-03,
            -3.08033824e-01,   2.31431410e-01,   1.62540793e-01,
            6.28208935e-01,  -1.94355965e-01,   7.23800480e-01,
            -6.49612308e-01,  -4.07179184e-02,  -1.46422181e-02,
            4.51475441e-01,   1.59122205e+00,   2.70355493e-01,
            2.04248756e-01,  -6.33800551e-02,  -5.50178960e-02,
            -1.00920045e+00,   2.39532292e-01,   3.62904727e-01,
            -3.38783532e-01,   9.40650925e-02,  -8.44506770e-02,
            3.55101633e-03,  -2.68924050e-02,   4.93676625e-02],dtype = np.float) #(72,)
   
  beta = np.array([-0.25349993,  0.25009069,  0.21440795,  0.78280628,  0.08625954,
            0.28128183,  0.06626327, -0.26495767,  0.09009246,  0.06537955 ]) #(10,)
   
  vbeta = torch.tensor(np.array([beta])).float().to(device)
  vpose = torch.tensor(np.array([pose])).float().to(device)
  
  verts, j, r = smpl(vbeta, vpose, get_skin = True)
  
  
