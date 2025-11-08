"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean, daily_min, daily_max, patient_normalise

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_min_simple():
    """Test that mean function works for a simple example array."""

    test_input = np.array([[0, 0],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test_input), test_result)
    
def test_daily_max_simple():
    """Test that mean function works for a simple example array."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [15, 16]])
    test_result = np.array([15, 16])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)
    
def test_daily_min_string():
    """Test for TypeError when passing strings"""

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])
        

# Let's add an automated testing function
@pytest.mark.parametrize("test", # requires only one input argument
                         [
                             ([['Hello', 'there'], ['General', 'Kenobi']]), # tuple with the one input
                             ([['Apple', 'pie'], ['my', 'favorite']])
                         ])
def test_daily_min_string_auto(test):
    """Test for TypeError when passing strings"""

    with pytest.raises(TypeError):
        _ = daily_min([['Hello', 'there'], ['General', 'Kenobi']])
        
# Example from materials with automated test function        
@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
    ])
def test_daily_mean_auto(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))
    


@pytest.mark.parametrize(
    "test, expected, expect_raises",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], None),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]], None),
        (
            [[-1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            ValueError,
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            None,
        ),
    ])
def test_patient_normalise(test, expected, expect_raises):
    """Test normalisation works for arrays of one and positive integers."""

    if expect_raises is not None:
        # in case error is expected outcome of test, use pytest.raises()
        with pytest.raises(expect_raises):
            patient_normalise(np.array(test))
                # note: no assert needed here, as error is now expected (and manually coded desired) outcome
    else:
        result = patient_normalise(np.array(test))
        npt.assert_allclose(result, np.array(expected), rtol=1e-2, atol=1e-2)
            # assert_allclose tests whether comparison equal within margin delta (rtol, atol)
                # rtol = relative tolerance
                # atol = absolute tolerance                            
                            