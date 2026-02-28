def find_pairs(arr, target):
    """Find all pairs in array that sum to target"""
    result = []
    seen = set()

    for num in arr:
        complement = target - num
        if complement in seen:
            result.append((complement, num))
        seen.add(num)

    return result


# ===== PYTEST TEST CASES =====
import pytest


class TestFindPairs:

    def test_normal_case(self):
        assert find_pairs([1, 2, 3, 4, 5], 6) == [(2, 4), (1, 5)]

    def test_empty_array(self):
        assert find_pairs([], 5) == []

    def test_no_pairs(self):
        assert find_pairs([1, 2, 3], 10) == []

    def test_negative_numbers(self):
        assert find_pairs([-1, -2, 3, 4], 2) == [(-2, 4)]

    def test_single_element(self):
        assert find_pairs([5], 5) == []

    def test_zero_target(self):
        assert find_pairs([-3, 3, -1, 1], 0) == [(-3, 3), (-1, 1)]

    def test_duplicate_elements(self):
        result = find_pairs([3, 3, 3], 6)
        assert len(result) == 2