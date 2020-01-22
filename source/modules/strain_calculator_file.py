import math
import numpy

class StrainCalculator():
  """docstring for StrainCalculator"""
  def __init__(self, v_out_baseline, v_in_baseline, v_out_current, v_in_current, gain=200, gage_factor = 2):
    
    self.v_out_baseline = v_out_baseline
    self.v_in_baseline = v_in_baseline
    self.v_out_current = v_out_current
    self.v_in_current = v_in_current
    self.gain = gain
    self.gage_factor = gage_factor

  def compute_strain(self):
    strain = 2.0*((self.v_out_current/self.v_in_current) - (self.v_out_baseline/self.v_in_baseline))/(self.gain*self.gage_factor)
    return strain