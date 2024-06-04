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

def predict_time(t_m, t_s, r_m):
    return t_s*(r_m/t_m)**(1/18)

def predict_m(t_m, t_s, r_s):
    return r_s / (t_m*(r_s/t_s)**(17/18)/500)

t_m = 2000
race = [950, 2000, 5000]
dt_l = [3600, 4800]
d = {}
l = []
target_seconds_l = np.arange(370, 548, 1)

for t_s in target_seconds_l:
    d["target_time"] = sec_to_time(t_s)
    # t_s = t_s / 4
    for r in race:
        d[str(r) + "m"] = sec_to_time(predict_time(t_m, t_s/4, r))
    for dt in dt_l:
        d[str(round(dt/60)) + "min"] = sec_to_time(predict_m(t_m, t_s, dt))
    l.append(d)
    d = {}

df = pd.DataFrame(l)
df
# df.to_csv('../dst/ergo_predict_time.csv')