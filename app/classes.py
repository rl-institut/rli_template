import itertools
import functools
import operator
from app import constants


class Household:
    id_counter = itertools.count()

    @classmethod
    def from_persons(cls, persons, name=None):
        return cls(
            annual_heat_demand=persons * constants.ANNUAL_HEAT_DEMAND_PER_PERSON,
            name=name,
        )

    def __init__(self, annual_heat_demand, name=None):
        self.__id = next(self.id_counter)
        self.name = f"Household #{self.__id}" if name is None else name
        self.__annual_heat_demand = annual_heat_demand
        self.__heat_profile = self.__get_profile(annual_heat_demand)

    @staticmethod
    def __get_profile(heat_demand):
        return constants.HEAT_PROFILE * heat_demand

    @property
    def heat_profile(self):
        return constants.HEAT_PROFILE * self.__annual_heat_demand

    @property
    def annual_heat_demand(self):
        return self.__annual_heat_demand

    @annual_heat_demand.setter
    def annual_heat_demand(self, heat_demand):
        self.__annual_heat_demand = heat_demand
        self.__heat_profile = self.__get_profile(heat_demand)

    def __add__(self, other):
        district = District()
        return district.add_households(self, other)

    def __str__(self):
        return self.name


class District:
    def __init__(self):
        self.__households = []

    def add_households(self, *households):
        self.__households += households

    @property
    def annual_heat_demand(self):
        return functools.reduce(
            operator.add,
            [household.annual_heat_demand for household in self.__households],
        )

    @property
    def heat_profile(self):
        return functools.reduce(
            operator.add,
            [household.heat_profile for household in self.__households],
        )
