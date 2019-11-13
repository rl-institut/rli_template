"""
run these tests with `pytest tests/test_something.py` or `pytest tests` or simply `pytest`
pytest will look for all files starting with "test_" and run all functions
within this file. For basic example of tests you can look at our workshop
https://github.com/rl-institut/workshop/tree/master/test-driven-development.
Otherwise https://docs.pytest.org/en/latest/ and https://docs.python.org/3/library/unittest.html
are also good support.
"""
import pytest

from app import classes
from app import constants


household = classes.Household(annual_heat_demand=5000)
household_2_persons = classes.Household.from_persons(2, name='Haus von Hänsel und Gretel')
household_change = classes.Household(2000)


def test_init():
    assert household.annual_heat_demand == 5000


def test_init_by_persons():
    assert (
        household_2_persons.annual_heat_demand
        == constants.ANNUAL_HEAT_DEMAND_PER_PERSON * 2
    )


def test_id():
    # Note: These tests depend on testing order and is not recommended in real tests!
    assert household._Household__id == 3
    assert household_2_persons._Household__id == 4
    assert household_change._Household__id == 5


def test_named_household():
    # Note: Next test depends on testing order and is not recommended in real tests!
    assert household.name == 'Household #3'
    assert household_2_persons.name == 'Haus von Hänsel und Gretel'
    household_change.name = 'Haus von Henner'
    assert household_change.name == 'Haus von Henner'


def test_profile():
    assert len(household.heat_profile) == 24
    assert household.heat_profile.sum() == pytest.approx(5000)


def test_change_heat_demand():
    household_change.annual_heat_demand = 3000
    assert household_change.annual_heat_demand == 3000
    assert household_change.heat_profile.sum() == pytest.approx(3000)


def test_str():
    assert str(household) == 'Household #3'
    assert str(household_2_persons) == 'Haus von Hänsel und Gretel'
    assert str(household_change) == 'Haus von Henner'
