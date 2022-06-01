import pandas as pd
import numpy as np
import math

def sec_to_time(time):
    m = math.floor(time / 60)
    s = round((time % 60), 1)
    if s < 10:
        return str(m) + ':0' + str(s)
    return str(m) + ':' + str(s)

def watt_to_pace(watt):
    pace = 500 * (2.80 / watt) ** (1/3)
    return pace

def pace_to_watt(pace):
    watt = 2.80 / (pace / 500) ** 3
    return watt