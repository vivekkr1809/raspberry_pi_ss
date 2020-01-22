import numpy
import math
import pickle

class SaveData():
  """docstring for SaveMultiNumpyArray"""
  def __init__(self):
    pass
    
  def save_baseline_vector(self, filename, pickle_file, out_bin_base, reference, reference_mean_base, separated_base, sig_neg_mean_base, sig_pos_mean_base, time_bin_base, v_in_mean_base, v_out_mean_base, gain=None, gauge_factor=None):

    # Set default values for gain and gauge factor
    if gain is None:
      gain = 200
    if gauge_factor is None:
      gauge_factor = 2.1

    baseline_dict = {'filename':None, 'gain':None, 'gauge_factor':None, 'out_bin_base': None, 'reference':None, 'reference_mean_base':None, 'separated_base':None, 'sig_neg_mean_base':None, 'sig_pos_mean_base':None, 'time_bin_base':None, 'v_in_mean_base':None, 'v_out_mean_base':None}
    baseline_dict['filename'] = filename
    baseline_dict['gain'] = gain
    baseline_dict['gauge_factor'] = gauge_factor
    baseline_dict['out_bin_base'] = out_bin_base
    baseline_dict['reference'] = reference
    baseline_dict['reference_mean_base'] = reference_mean_base
    baseline_dict['separated_base'] = separated_base
    baseline_dict['sig_neg_mean_base'] = sig_neg_mean_base
    baseline_dict['sig_pos_mean_base'] = sig_pos_mean_base
    baseline_dict['time_bin_base'] = time_bin_base
    baseline_dict['v_in_mean_base'] = v_in_mean_base
    baseline_dict['v_out_mean_base'] = v_out_mean_base
    
    with open(pickle_file, 'wb') as handle:
      pickle.dump(baseline_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

  def save_measurement_vector():
    pass