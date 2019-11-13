
import math
import pandas

ANNUAL_HEAT_DEMAND_PER_PERSON = 3960


def get_heat_profile():
    profile = pandas.Series(
        [math.sin((180 / 23 * x) / 360 * 2 * math.pi) for x in range(24)])
    return profile / profile.sum()


HEAT_PROFILE = get_heat_profile()
