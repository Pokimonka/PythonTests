
import pytest

from task2_tests.task2 import vote


@pytest.mark.parametrize(
    'list_votes, result',
    (
        ([1,1,1,2,3], 1),
        ([1,2,3,2,2], 2)
    )
)
def test_vote(list_votes, result):
    check = vote(list_votes)
    assert result == check

@pytest.mark.parametrize(
    'list_votes, result',
    (
        ([-1,-1,-1,2,-3], -1),
        ([-1,2,-3,2,2], 2)
    )
)
def test_negative_numbers_vote(list_votes, result):
    check = vote(list_votes)
    assert result == check

@pytest.mark.parametrize(
    'list_votes, result',
    (
        ([1,1,1,2,2,2], 1),
        ([-1,2,-1,2,-1,2], -1)
    )
)
def test_equal_count_votes(list_votes, result):
    check = vote(list_votes)
    assert result == check