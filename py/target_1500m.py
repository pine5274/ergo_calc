import pandas as pd
import numpy as np
import math
import function

def sec_to_time(time):
    m = math.floor(time / 60)
    s = round((time % 60), 1)
    if s < 10:
        return str(m) + ':0' + str(s)
    return str(m) + ':' + str(s)

def calc_1500m_target(target_time_2000m):
    distance = 1500
    distance_factor = 0.475
    sets = 5

    single_distance_conversion = distance * (1 + (sets - 1) * distance_factor)

    result = (target_time_2000m * (2000 / single_distance_conversion)/((2000/single_distance_conversion)**(19/18))) / 4

    return result

print(sec_to_time(calc_1500m_target(420)))

list = []

target = np.arange(380, 511, 5)

for x in target:
    list.append({
        "2000m": sec_to_time(x),
        "2000m ave": sec_to_time(x/4),
        "1500m *5 ave": sec_to_time(calc_1500m_target(x)),
        "インターバルをやめる目安": sec_to_time(function.watt_to_pace(function.pace_to_watt(calc_1500m_target(x))*0.94))
    })

df = pd.DataFrame(list)

df.to_csv('../dst/1500_predict_time.csv')