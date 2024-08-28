from exercises.challenge_01 import find_peak
from exercises.challenge_02 import blur_image
from exercises.challenge_03 import merge_receipts
from exercises.challenge_04 import reverse_matrix
from exercises.challenge_05 import interval_intersection
from exercises.challenge_06 import find_first_missing_positive
from exercises.challenge_07 import pascals_triangle
from exercises.challenge_08 import tail
from exercises.challenge_09 import diagonal_sum
from exercises.challenge_10 import find_element_more_than_25_percent
from exercises.challenge_11 import tribonacci
from exercises.challenge_12 import num_pairs_divisible_by_60
from exercises.challenge_13 import is_monotonic
from exercises.challenge_14 import add_matrices
from exercises.challenge_15 import transpose_matrix
from exercises.challenge_16 import is_word_in_matrix
from exercises.challenge_17 import compare_versions
from exercises.challenge_18 import NestedIterator
from exercises.challenge_19 import count_servers
from exercises.challenge_20 import integer_to_roman
from exercises.challenge_21 import compute_ip_addresses


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


def test_challenge_16():
    assert is_word_in_matrix([], "") is False
    assert (
        is_word_in_matrix(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
        )
        is True
    )
    assert (
        is_word_in_matrix(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"
        )
        is True
    )
    assert (
        is_word_in_matrix(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
        )
        is False
    )
    assert (
        is_word_in_matrix(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCESEEDAS",
        )
        is True
    )
    assert (
        is_word_in_matrix(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCESEDAS",
        )
        is False
    )


def test_challenge_17():
    assert compare_versions("1.01", "1.001") == 0
    assert compare_versions("1.0", "1.0.0") == 0
    assert compare_versions("0.1", "1.1") == -1
    assert compare_versions("1.0.1", "1") == 1
    assert compare_versions("1.0.1", "1.0.10") == -1
    assert compare_versions("1.0.1", "1.0.1") == 0
    assert compare_versions("1.0.1", "1.0.2") == -1
    assert compare_versions("1.0.1", "1.0.0") == 1


def test_challenge_18():
    iterator0 = NestedIterator([[1, [2, [3, [4]]]]])
    assert iterator0.next() == 1
    assert iterator0.next() == 2
    assert iterator0.next() == 3
    assert iterator0.next() == 4
    assert iterator0.hasNext() is False

    iterator1 = NestedIterator([[1, 2], [3], [4, 5, 6]])
    assert iterator1.next() == 1
    assert iterator1.next() == 2
    assert iterator1.next() == 3
    assert iterator1.next() == 4
    assert iterator1.next() == 5
    assert iterator1.next() == 6
    assert iterator1.hasNext() is False

    iterator2 = NestedIterator([[1, 2, 3], [4, [5, 6]], [7, 8, 9]])
    assert iterator2.next() == 1
    assert iterator2.next() == 2
    assert iterator2.next() == 3
    assert iterator2.next() == 4
    assert iterator2.next() == 5
    assert iterator2.next() == 6
    assert iterator2.next() == 7
    assert iterator2.next() == 8
    assert iterator2.next() == 9
    assert iterator2.hasNext() is False


def test_challenge_19():
    assert count_servers([[1, 0], [0, 1]]) == 0
    assert count_servers([[1, 0], [1, 1]]) == 3
    assert count_servers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) == 4
    assert count_servers([[1, 0, 0], [0, 0, 1], [0, 0, 1]]) == 3
    assert count_servers([[1, 0, 0], [0, 1, 1], [0, 0, 1]]) == 4
    assert count_servers([[1, 0, 0], [0, 1, 1], [0, 0, 0]]) == 2


def test_challenge_20():
    assert integer_to_roman(3) == "III"
    assert integer_to_roman(4) == "IV"
    assert integer_to_roman(9) == "IX"
    assert integer_to_roman(58) == "LVIII"
    assert integer_to_roman(1994) == "MCMXCIV"
    assert integer_to_roman(3999) == "MMMCMXCIX"
    assert integer_to_roman(39999) == "MMM"


def test_challenge_21():
    assert interval_intersection(
        [[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]
    ) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    assert interval_intersection([[1, 3], [5, 9]], []) == []
    assert interval_intersection([[1, 7]], [[3, 10]]) == [[3, 7]]
    assert interval_intersection([[1, 7]], [[8, 10]]) == []
    assert interval_intersection([[1, 7]], [[7, 10]]) == [[7, 7]]
