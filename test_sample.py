# def func(x):
#     return x + 1


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
# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert "h" in x

#     def test_two(self):
#         x = "hello"
#         # assert hasattr(x, "check")  # False
#         assert hasattr(x, "__len__")

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

# testing two sets with assert
def test_set_comparison():
    set1 = set("1308")
    set2 = set("8035")
    assert set1 == set2

#Testing with parameterization  Which can also be used in a class to apply to all methods in the class
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), pytest.param("6*9", 15, marks=pytest.mark.xfail)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

# # To get all the combinations of inputs.
# @pytest.mark.parametrize("x", [0, 2])
# @pytest.mark.parametrize("y", [2, 3])
# def test_foo(x, y):
#     assert x < y




