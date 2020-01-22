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

  out_bin_base = np.random.rand(2000,7)
  reference = 0
  reference_mean_base = np.random.rand(1,8)
  separated_base = {'sensor_1':np.random.rand(160,7),
                    'sensor_2':np.random.rand(160,7),
                    'sensor_3':np.random.rand(160,7),
                    'sensor_4':np.random.rand(160,7),
                    'sensor_5':np.random.rand(160,7),
                    'sensor_6':np.random.rand(160,7),
                    'sensor_7':np.random.rand(160,7),
                    'sensor_8':np.random.rand(160,7),
                    'time_1':np.random.rand(160,1),
                    'time_2':np.random.rand(160,1),
                    'time_3':np.random.rand(160,1),
                    'time_4':np.random.rand(160,1),
                    'time_5':np.random.rand(160,1),
                    'time_6':np.random.rand(160,1),
                    'time_7':np.random.rand(160,1),
                    'time_8':np.random.rand(160,1)}
  sig_neg_mean_base = np.random.rand(1,8)
  sig_pos_mean_base = np.random.rand(1,8)
  time_bin_base = np.random.rand(2000,1)
  v_in_mean_base = np.random.rand(1,8)
  v_out_mean_base =  np.random.rand(1,8)

  save_file_object = SaveData()
  save_file_object.save_baseline_vector(filename, pickle_file, out_bin_base, reference, reference_mean_base, separated_base, sig_neg_mean_base, sig_pos_mean_base, time_bin_base, v_in_mean_base, v_out_mean_base, gain, gauge_factor)

  with open(pickle_file, 'rb') as handle:
    read_baseline_vector = pickle.load(handle)
  
  assert(read_baseline_vector['filename'] == 'baseline_vector_15_14_01')

def test_no_gage_factor_no_gain():
  filename = 'baseline_vector_15_14_01'
  pickle_file = './baseline_vectors/'+filename+'.pickle'
  np.random.seed(42) # Fix the seed
  
  out_bin_base = np.random.rand(2000,7)
  reference = 0
  reference_mean_base = np.random.rand(1,8)
  separated_base = {'sensor_1':np.random.rand(160,7),
                    'sensor_2':np.random.rand(160,7),
                    'sensor_3':np.random.rand(160,7),
                    'sensor_4':np.random.rand(160,7),
                    'sensor_5':np.random.rand(160,7),
                    'sensor_6':np.random.rand(160,7),
                    'sensor_7':np.random.rand(160,7),
                    'sensor_8':np.random.rand(160,7),
                    'time_1':np.random.rand(160,1),
                    'time_2':np.random.rand(160,1),
                    'time_3':np.random.rand(160,1),
                    'time_4':np.random.rand(160,1),
                    'time_5':np.random.rand(160,1),
                    'time_6':np.random.rand(160,1),
                    'time_7':np.random.rand(160,1),
                    'time_8':np.random.rand(160,1)}
  sig_neg_mean_base = np.random.rand(1,8)
  sig_pos_mean_base = np.random.rand(1,8)
  time_bin_base = np.random.rand(2000,1)
  v_in_mean_base = np.random.rand(1,8)
  v_out_mean_base =  np.random.rand(1,8)

  save_file_object = SaveData()
  save_file_object.save_baseline_vector(filename, pickle_file, out_bin_base, reference, reference_mean_base, separated_base, sig_neg_mean_base, sig_pos_mean_base, time_bin_base, v_in_mean_base, v_out_mean_base)

  with open(pickle_file, 'rb') as handle:
    read_baseline_vector = pickle.load(handle)
  
  assert(read_baseline_vector['gauge_factor'] == 2.1)
  assert(read_baseline_vector['gain'] == 200)
