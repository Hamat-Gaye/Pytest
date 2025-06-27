# def func(x):
#     return x + 1
from pandas import read_json


# def test_func():
#     assert func(3) == 5


# # content of test_sysexit.py
# import pytest

# def f():
#     raise SystemExit(1)

# def test_f():
#     with pytest.raises(SystemExit):
#         f()


# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        # assert hasattr(x, "check")  # False
        assert hasattr(x, "__len__")


import pytest

from get_percentage import get_pass_percentage


@pytest.mark.parametrize("a,b", [
    (5, 1),
    (1, 2),
    (3, 4),
    (3, 2)
])
def test_func(a, b):
    assert a < b


# def test_zero_division():
#     with pytest.raises(ZeroDivisionError):
#         1 / 0

def test_foo_not_implemented():
    def foo():
        raise NotImplementedError

    with pytest.raises(RuntimeError) as excinfo:
        foo()
    assert excinfo.type is RuntimeError


#Testing an imported function from another file
def test_get_pass_percentage():
    val = 50
    assert get_pass_percentage(10, 20) == val


# Testing for regex expressions in an error message
def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError, match=r".* 123 r*."):
        myfunc()

#Fixtures in pytest
@pytest.fixture(params=[1,2,3,4,5])
def test_fixture_param(request):
    return request.param


def test_params_from_fixture(test_fixture_param):
        my_list = [1, 2, 3, 4, 5]
        assert test_fixture_param in my_list, f"{test_fixture_param} is not in {my_list}"


@pytest.fixture()
def sample_fixture():
    print("\n_________You are in the fixture____________\n")
    data = [1, 2, 3, 4, 5]
    return data

def test_sample_fixture(sample_fixture):
    values = sample_fixture
    assert values == [1, 2, 3, 4, 5]

@pytest.mark.xfail(reason = "The return values of the fixtures cannot be accessed if we use the @pytest.mark.usefixtures decorator")
@pytest.mark.usefixtures("sample_fixture")
def test_use_fixtures():
    print("This test uses the sample_fixture without explicitly passing it as an argument.")
    assert sample_fixture == [1, 2, 3, 4, 5]

weekdays1 = ["mon", "tue", "wed"]
weekdays2 = ["fri", "sat", "sun"]

@pytest.fixture()
def setup01():
    wk1 = weekdays1.copy()
    wk1.append("thur")
    yield wk1
    print("\n\n After yield in the function\n")
    wk1.clear()
    # wk1.pop()

@pytest.fixture()
def setup02():
    wk2 = weekdays2.copy()
    wk2.insert(0, "thur")
    yield wk2

class TestFixtures:
    def test_extendList(self, setup01):
        setup01.extend(weekdays2)
        assert setup01 == ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]


    def test_len(self, setup01, setup02):
        assert len(weekdays1 + setup02) == len(setup01 + weekdays2)



# testing two sets by using assert
def test_set_comparison():
    set1 = set("1308")
    set2 = set("8035")
    assert set1 == set2


#Testing with parameterization which can also be used in a class to apply to all methods in the class
@pytest.mark.parametrize("test_input,expected",
                         [("3+5", 8), ("2+4", 6), pytest.param("5*4", 15, marks=pytest.mark.xfail)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

# # To get all the combinations of inputs.
# @pytest.mark.parametrize("x", [0, 2])
# @pytest.mark.parametrize("y", [2, 3])
# def test_foo(x, y):
#     assert x < y
