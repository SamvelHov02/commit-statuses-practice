from operations import *
import pytest

def test_add(): assert add(3,2) == 5

def test_mul(): assert mul(3,2) == 6

def test_sub(): assert sub(3,2) == 1

def test_add_negative(): assert add(3,2) != 6

def test_mul_negative(): assert mul(3,2) != 7

def test_sub_negative(): assert sub(3,2) != 2

def test_factorial(): assert factorial(4) == 24
 
def test_factorial_negative(): assert factorial(4) != 25

def test_exp_positive(): assert exp(2, 3) == 8

def test_exp_negative(): assert exp(3, 2) != 8

