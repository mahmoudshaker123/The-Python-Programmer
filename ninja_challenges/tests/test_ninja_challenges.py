from ..exercises.challenge_01 import find_peak
from ..exercises.challenge_02 import blur_image
from ..exercises.challenge_03 import merge_receipts
from ..exercises.challenge_04 import reverse_matrix
from ..exercises.challenge_05 import compute_ip_addresses
from ..exercises.challenge_06 import find_first_missing_positive
from ..exercises.challenge_07 import pascals_triangle
from ..exercises.challenge_08 import tail
from ..exercises.challenge_09 import diagonal_sum
from ..exercises.challenge_10 import find_element_more_than_25_percent
from ..exercises.challenge_11 import tribonacci
from ..exercises.challenge_12 import num_pairs_divisible_by_60
from ..exercises.challenge_13 import is_monotonic
from ..exercises.challenge_14 import add_matrices
from ..exercises.challenge_15 import transpose_matrix


def test_challenge_01():
    assert find_peak([]) == -1
    assert find_peak([1, 2, 3, 4, 5, 6, 7]) == 7
    assert find_peak([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) == 7


def test_challenge_02():
    assert blur_image([]) == []


def test_challenge_03():
    assert merge_receipts([]) == {}


def test_challenge_04():
    assert reverse_matrix([]) == []


def test_challenge_05():
    assert compute_ip_addresses("") == []


def test_challenge_06():
    assert find_first_missing_positive([]) == 1


def test_challenge_07():
    assert pascals_triangle(0) == []


def test_challenge_08():
    assert tail([]) == []


def test_challenge_09():
    assert diagonal_sum([]) == 0


def test_challenge_10():
    assert find_element_more_than_25_percent([]) == -1


def test_challenge_11():
    assert tribonacci(0) == 0


def test_challenge_12():
    assert num_pairs_divisible_by_60([]) == 0


def test_challenge_13():
    assert is_monotonic([]) is True


def test_challenge_14():
    assert add_matrices([], []) == []


def test_challenge_15():
    assert transpose_matrix([]) == []
