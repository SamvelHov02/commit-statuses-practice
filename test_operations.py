from operations import *
import pytest

def test_add(): assert add(3,2) == 5

def test_mul(): assert mul(3,2) == 6

def test_sub(): assert sub(3,2) == 1

def test_add_negative(): assert add(3,2) != 6
 