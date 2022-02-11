import numpy as np
import matplotlib.pyplot as plt
from icg_preprocess import icg_preprocess
from point_detection import points
import re
from glob import glob



def atof(text):
    try:
        retval = float(text)
    except ValueError:
        retval = text
    return retval

def natural_keys(text):
    return [ atof(c) for c in re.split(r'[+-]?([0-9]+(?:[.][0-9]*)?|[.][0-9]+)', text) ]


sample_rate = 300
# lim1 = 1000
# lim2 = 2000
thr = 0.2
radius = 3
window_size = 31
order_sg = 11
cutoff_f = 40
order_low_pass = 4

# 1. DATA LOAD

files = glob("01_RawData/*BL.mat")
files.sort(key=natural_keys)

# 2. DATA PARAMETERS

lim = 1000
fs = 300

# 3. LOAD OF THE PREPROCESSED FILES

icg = icg_preprocess(files[0], lim, sampling_rate=fs)
data_icg = icg.baseline()

pt = points(data_icg, fs)

C_points = pt.C_point_detection()
B_points = pt.B_point_detection()
X_points = pt.X_point_detection()

plt.plot(np.arange(len(data_icg)), data_icg)
plt.scatter(C_points, data_icg[C_points])
plt.scatter(B_points, data_icg[B_points])
plt.scatter(X_points, data_icg[X_points])

plt.show()




