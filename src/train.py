import torch
import torch.nn as nn

import config
from config import args

from model import HMRNetBase

class HMRTrainer(object):
  def __init__(self):
    
    self._build_model()
    self._create_data_loader()
  
  def _create_data_loader(self):
    '''dataloader'''
    
  def _build_model(self):
    print('start building model')
    
    '''
    load pretrain model
    '''
    generator = HMRNetBase()
    #model_path = config.pre_trained_model['generator']
    discriminator = Discriminator()
    #model_path = config.pre_trained_model['discriminator']
    self.generator = nn.DataParallel(generator).cuda()
    self.discriminator = nn.DataParallel(discriminator).cuda()
    
    print('finished build model.')
    
  def train(self):
    def save_model(result):

      
def main():
  trainer = HMRTrainer()
  trainer.train()
  
if __name__ == '__main__':
  main()
      
