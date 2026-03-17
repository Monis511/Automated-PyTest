import pytest
from student_grading import calculate_grade

def test_grade_a():
    assert calculate_grade(95) == "A"

def test_grade_b():
    assert calculate_grade(85) == "B"

def test_grade_c():
    assert calculate_grade(75) == "C"

def test_grade_f():
    assert calculate_grade(50) == "F"

def test_invalid_high():
    assert calculate_grade(105) == "Invalid"

def test_invalid_low():
    assert calculate_grade(-1) == "Invalid"

def test_non_numeric():
    assert calculate_grade("ninety") == "Invalid"