import pandas as pd
import numpy as np
from statistics import median
import function

list = []

target = np.arange(380, 511, 5)

for x in target:
    list.append({
        "2000m": function.sec_to_time(x),
        "3min *N ave": function.sec_to_time(x/4),
        "インターバルをやめる目安": function.sec_to_time(function.watt_to_pace(function.pace_to_watt(x/4)*0.915))
    })

df = pd.DataFrame(list)

# df.to_csv('../dst/1500_predict_time.csv')