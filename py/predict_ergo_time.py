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

# ボツ
def i2s(t_m, t_s, seconds):
    mps = 4
    i = 1
    g_m = mps * seconds
    g_s = predict_time(t_m, t_s, g_m)
    while i < 10:
        g_m += mps * (seconds - g_s*g_m/500)
        g_s = predict_time(t_m, t_s, g_m)
        i += 1
    return sec_to_time(g_s)

def predict_m(t_m, t_s, r_s):
    # return sec_to_time(t_s/4*(r_s/t_s)**(1/18))
    return sec_to_time(r_s / (t_m*(r_s/t_s)**(17/18)/500))

t_m = 2000
# t_m = 1000
race = [1000, 2000, 6000]
dt_l = [1200, 1800, 3600]
d = {}
l = []
target_seconds_l = np.arange(380, 501, 10)
# target_seconds_l = np.arange(180, 240, 10)

for t_s in target_seconds_l:
    d["target_time"] = sec_to_time(t_s)
    # t_s = t_s / 4
    for r in race:
        d[str(r) + "m"] = sec_to_time(predict_time(t_m, t_s/2, r))
    for dt in dt_l:
        d[str(round(dt/60)) + "min"] = predict_m(t_m, t_s, dt)
    l.append(d)
    d = {}

df = pd.DataFrame(l)
df
df.to_csv('../dst/ergo_predict_time.csv')