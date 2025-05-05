import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from other_files.primt_no_finder import is_prime, count_primes_in_range

def test_is_prime_basic():
    assert is_prime(5) is True

def test_is_prime_edge_case():
    assert is_prime(0) is False

def test_is_prime_error_handling():
    with pytest.raises(TypeError):
        is_prime("a")

def test_count_primes_in_range_basic():
    assert count_primes_in_range(1, 10) == 4  # Assuming 2, 3, 5, 7 are primes

def test_count_primes_in_range_edge_case():
    assert count_primes_in_range(0, 0) == 0

def test_count_primes_in_range_error_handling():
    with pytest.raises(ValueError):
        count_primes_in_range(10, 1)  # Invalid range
