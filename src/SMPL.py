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
  
