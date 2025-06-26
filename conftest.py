import pytest
from pytest import fixture

def pytest_configure():
    pytest.weekdays1 = ["mon", "tue", "wed"]
    pytest.weekdays2 = ["mon", "tue", "wed"]


@pytest.fixture()
def setup01():
    wk1 = pytest.weekdays1.copy()
    wk1.append("thur")
    yield wk1
    print("\n\n After yield in the function\n")
    wk1.clear()
    # wk1.pop()

@pytest.fixture()
def setup02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0, "thur")
    yield wk2
