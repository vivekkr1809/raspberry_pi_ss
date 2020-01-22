import pytest

from modules.strain_calculator_file import StrainCalculator

def test_no_strain():
	_eps = 1.0e-4
	v_out_baseline = 1.
	v_in_baseline = 1.
	v_out_current = 1.+_eps
	v_in_current = 1.-_eps
	strain = StrainCalculator(v_out_baseline, v_in_baseline, v_out_current, v_in_current).compute_strain()
	assert(strain==pytest.approx(0, abs=1.0e-5, rel=1.0e-5))