import random

class Dice:
  facesNumber = 1
  
  def __init__(self, _facesNUmber):
    self.facesNumber = _facesNUmber
    
  def __str__(self):
    return "Faces Number: " + str(self.facesNumber)
    
  def throw(self):
    return random.randint(1, self.facesNumber + 1)
