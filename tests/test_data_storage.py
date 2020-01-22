import pytest
import numpy as np
import pickle

from modules.save_data_file import SaveData


def test_save_data_file():
  
  filename = 'baseline_vector_15_14_01'
  pickle_file = './baseline_vectors/'+filename+'.pickle'
  gain = 200.
  gauge_factor = 2.1
  
  np.random.seed(42) # Fix the seed

  out_mean_base = np.random.rand(400,8)
  reference = 0
  reference_mean_base = np.random.rand(1,8)
  sig_neg_mean_base = np.random.rand(1,8)
  sig_pos_mean_base = np.random.rand(1,8)
  time_bin_base = np.random.rand(400,1)
  v_in_mean_base = np.random.rand(1,8)
  v_out_mean_base =  np.random.rand(1,8)

  save_file_object = SaveData()
  save_file_object.save_baseline_vector(filename, pickle_file, gain, gauge_factor, out_mean_base, reference, reference_mean_base, sig_neg_mean_base, sig_pos_mean_base, time_bin_base, v_in_mean_base, v_out_mean_base)

  with open(pickle_file, 'rb') as handle:
    read_baseline_vector = pickle.load(handle)

  assert(read_baseline_vector['filename']=='baseline_vector_15_14_01')