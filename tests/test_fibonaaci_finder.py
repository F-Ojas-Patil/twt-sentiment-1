import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from other_files.fibonaaci_finder import fib

def test_fib_basic():
    assert fib(5) == 5  # Assuming fib returns nth Fibonacci number

def test_fib_edge_case():
    assert fib(0) == 0  # Edge case for Fibonacci

def test_fib_error_handling():
    with pytest.raises(TypeError):
        fib("a")  # Error handling for invalid input
