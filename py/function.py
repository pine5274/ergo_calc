import pandas as pd
import numpy as np
import math

def sec_to_time(time):
    m = math.floor(time / 60)
    s = round((time % 60), 1)
    if s < 10:
        return str(m) + ':0' + str(s)
    return str(m) + ':' + str(s)

# 怪しい
def time_to_sec(x):
    if (type(x) is float):
        return x
    minutes = int(x[3])
    seconds = int(x[-2:])
    return minutes * 60 + seconds

def watt_to_pace(watt):
    sec = 500 * (2.80 / watt) ** (1/3)
    pace = sec_to_time(sec)
    return pace

def pace_to_watt(pace):
    sec = time_to_sec(pace)
    watt = 2.80 / (sec / 500) ** 3
    return watt