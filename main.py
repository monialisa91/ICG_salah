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


sample_rate = 500
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
fs = 500


#  ICG parameters

cutoff_lowICG = 20
order_lowICG = 4
cutoff_highICG = 5
order_highICG = 4

# 3. LOAD OF THE PREPROCESSED FILES

icg = icg_preprocess(files[0], lim, sampling_rate=fs, cutoff_low=cutoff_lowICG, cutoff_high=cutoff_highICG, order_low=order_lowICG, order_high=order_highICG)
data_icg = icg.baseline()

icg_points = points(data_icg, fs)
C_points = icg_points.C_point_detection()

plt.plot(np.arange(len(data_icg)), data_icg)
plt.scatter(C_points, data_icg[C_points])
plt.show()


exit()

fig = plt.figure(figsize=(8, 6))

ax1 = plt.subplot2grid((3, 4), (0, 0), colspan=4)
ax2 = plt.subplot2grid((3, 4), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 4), (1, 2), colspan=2)
ax4 = plt.subplot2grid((3, 4), (2, 0), colspan=2)
ax5 = plt.subplot2grid((3, 4), (2, 2), colspan=2)
# ax6 = plt.subplot2grid((3, 4), (1, 4), colspan=2)
# ax7 = plt.subplot2grid((3, 4), (2, 0), colspan=3)
# ax8 = plt.subplot2grid((3, 4), (2, 3), colspan=3)

ax1.plot(np.arange(len(icg_raw)), icg_raw)
ax1.set_title("Raw ICG data", weight='bold')
ax1.axes.yaxis.set_ticklabels([])

ax2.plot(np.arange(len(icg_data)), icg_data)
ax2.set_title("Filtered ICG data", weight='bold')
ax2.axes.yaxis.set_ticklabels([])


ax3.plot(np.arange(len(icg_data_der)), icg_data_der)
ax3.set_title("Derivative filter", weight='bold')
ax3.axes.yaxis.set_ticklabels([])


ax4.plot(np.arange(len(icg_square)), icg_square)
ax4.set_title("Squaring", weight='bold')
ax4.axes.yaxis.set_ticklabels([])


ax5.plot(np.arange(len(icg_mov_w_int)), icg_mov_w_int)
ax5.set_title("Moving window integration", weight='bold')
ax5.axes.yaxis.set_ticklabels([])


fig.tight_layout()
plt.show()


# axs[0].plot(np.arange(len(icg_data)), icg_data)
# axs[1].plot(np.arange(len(icg_data_der)), icg_data_der)
# axs[2].plot(np.arange(len(icg_square)), icg_square)
# axs[3].plot(np.arange(len(icg_mov_w_int)), icg_mov_w_int)
#
# # plt.plot(np.arange(len(icg_data)), icg_data)
# plt.plot(np.arange(len(icg_data)), icg_square)
# plt.show()



