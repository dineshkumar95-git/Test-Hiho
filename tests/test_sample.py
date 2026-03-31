import time
import pytest

# -------------------------
# ✅ BASIC PASSING TESTS
# -------------------------

def test_addition_1():
    assert 1 + 1 == 2
    
def test_addition_0():
    assert 1 + 1 == 2
def test_addition_2():
    assert 5 + 10 == 15

def test_subtraction_1():
    assert 10 - 5 == 5

def test_subtraction_2():
    assert 100 - 50 == 50

def test_multiplication_1():
    assert 2 * 3 == 6

def test_multiplication_2():
    assert 7 * 8 == 56

def test_division_1():
    assert 10 / 2 == 5

def test_division_2():
    assert 9 / 3 == 3

# -------------------------
# ❌ INTENTIONAL FAILURES
# -------------------------

def test_addition_fail():
    assert 1 + 1 == 3  # ❌ FAIL

def test_subtraction_fail():
    assert 10 - 3 == 20  # ❌ FAIL

def test_multiplication_fail():
    assert 3 * 3 == 10  # ❌ FAIL

def test_division_fail():
    assert 8 / 2 == 10  # ❌ FAIL

# -------------------------
# ✅ BOOLEAN / EDGE CASES
# -------------------------

def test_zero_addition():
    assert 0 + 0 == 0

def test_zero_multiplication():
    assert 10 * 0 == 0

def test_negative_addition():
    assert -5 + 5 == 0

def test_negative_multiplication():
    assert -3 * 3 == -9

def test_large_numbers():
    assert 1000000 + 2000000 == 3000000

# -------------------------
# ⏳ SLOW TESTS (for duration charts)
# -------------------------

def test_slow_1():
    time.sleep(0.05)
    assert 2 + 2 == 4

def test_slow_2():
    time.sleep(0.1)
    assert 3 * 3 == 9

def test_slow_3():
    time.sleep(0.15)
    assert 4 - 1 == 3

# -------------------------
# ❌ FAILING SLOW TESTS
# -------------------------

def test_slow_fail_1():
    time.sleep(0.05)
    assert 5 + 5 == 20  # ❌ FAIL

def test_slow_fail_2():
    time.sleep(0.1)
    assert 6 * 6 == 10  # ❌ FAIL

# -------------------------
# ✅ PARAMETERIZED TESTS
# -------------------------

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (2, 3, 5),
        (10, 20, 30),
        (-5, 5, 0),
        (100, 200, 300),
    ]
)
def test_param_addition(a, b, expected):
    assert a + b == expected

# -------------------------
# ✅ MORE PASSING TESTS
# -------------------------

def test_modulus_1():
    assert 10 % 2 == 0

def test_modulus_2():
    assert 9 % 2 == 1

def test_power():
    assert 2 ** 3 == 8

def test_floor_division():
    assert 7 // 2 == 3
