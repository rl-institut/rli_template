
import pytest
import pandas

from app import classes


household1 = classes.Household(2000)
household2 = classes.Household(3000)
household3 = classes.Household(1000)

district = classes.District()
district.add_households(household1, household2, household3)


def test_add_household_to_district():
    single_district = classes.District()
    single_district.add_households(household1)
    assert len(single_district._District__households) == 1


def test_add_households_to_district():
    assert len(district._District__households) == 3


def test_district_heat_demand():
    assert district.annual_heat_demand == 6000


def test_district_heat_profile():
    assert isinstance(district.heat_profile, pandas.Series)
    assert district.heat_profile.sum() == pytest.approx(6000)
